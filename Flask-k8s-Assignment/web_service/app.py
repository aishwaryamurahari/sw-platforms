import os
import requests
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)
app.config['SECRET_KEY'] = 'mykeyforflaskapp'

DB_SERVICE_URL = 'http://db-service:5432'

@app.route('/')
def index():
    response = requests.get(f'{DB_SERVICE_URL}/posts')
    posts = response.json()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<int:post_id>')
def post(post_id):
    response = requests.get(f'{DB_SERVICE_URL}/posts/{post_id}')
    if response.status_code == 404:
        abort(404)
    post = response.json()
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            response = requests.post(f'{DB_SERVICE_URL}/posts', json={'title': title, 'content': content})
            if response.status_code == 201:
                return redirect(url_for('index'))
            else:
                flash('An error occurred while creating the post.')
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    response = requests.get(f'{DB_SERVICE_URL}/posts/{id}')
    if response.status_code == 404:
        abort(404)
    post = response.json()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            response = requests.put(f'{DB_SERVICE_URL}/posts/{id}', json={'title': title, 'content': content})
            if response.status_code == 200:
                return redirect(url_for('index'))
            else:
                flash('An error occurred while updating the post.')

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    response = requests.delete(f'{DB_SERVICE_URL}/posts/{id}')
    if response.status_code == 200:
        flash('"{}" was successfully deleted!'.format(id))
    else:
        flash('An error occurred while deleting the post.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)