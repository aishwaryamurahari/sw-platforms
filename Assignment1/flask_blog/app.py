import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mykeyforflaskapp'

    @app.route('/')
    def index():
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template('index.html', posts=posts)

    @app.route("/about")
    def about():
        return render_template('about.html', title="About FlaskBlog", description="FlaskBlog is a simple blogging platform built with Flask, allowing users to create, edit, and manage blog posts.")

    @app.route('/<int:post_id>')
    def post(post_id):
        post = get_post(post_id)
        return render_template('post.html', post=post)

    @app.route('/create', methods=('GET', 'POST'))
    def create():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('Title is required!')
            else:
                conn = get_db_connection()
                conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                             (title, content))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
        return render_template('create.html')

    @app.route('/<int:id>/edit', methods=('GET', 'POST'))
    def edit(id):
        post = get_post(id)

        if post is None:
            flash('Post not found.', 'error')
            return redirect(url_for('index'))

        if request.method == 'POST':
            if 'cancel' in request.form:
                flash('Edit cancelled.', 'info')
                return redirect(url_for('index'))

            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('Title is required!')
            else:
                conn = get_db_connection()
                conn.execute('UPDATE posts SET title = ?, content = ?'
                             ' WHERE id = ?',
                             (title, content, id))
                conn.commit()
                conn.close()
                flash('Post "{}" was successfully updated.'.format(post['title']), 'success')
                return redirect(url_for('index'))

        return render_template('edit.html', post=post)

    @app.route('/<int:id>/delete', methods=['GET', 'POST'])
    def delete(id):
        post = get_post(id)
        if post is None:
            flash('Post not found.', 'error')
            return redirect(url_for('index'))

        if request.method == 'POST':
            if request.form.get('confirm') == 'yes':
                conn = get_db_connection()
                conn.execute('DELETE FROM posts WHERE id = ?', (id,))
                conn.commit()
                conn.close()
                flash('"{}" was successfully deleted!'.format(post['title']), 'success')
                return redirect(url_for('index'))
            else:
                flash('Deletion cancelled.', 'info')
                return redirect(url_for('index'))

        return render_template('delete.html', post=post)

    return app


if __name__ == "__main__":
    app = create_app()
    print("Running the app")
    app.run(debug=True)
