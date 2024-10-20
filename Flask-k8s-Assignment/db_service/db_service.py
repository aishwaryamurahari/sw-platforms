import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.close()

@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return jsonify([dict(post) for post in posts])

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(dict(post))

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    title = data.get('title')
    content = data.get('content')

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()

    return jsonify({'id': post_id, 'title': title, 'content': content}), 201

# Add similar routes for updating and deleting posts

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5432)