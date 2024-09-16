import pytest
import sqlite3
from flask_blog.app import create_app, get_db_connection, init_db


app = create_app()


@pytest.fixture(autouse=True)
def get_db_connection():
    if app.config['TESTING']:
        conn = sqlite3.connect(':memory:')
        conn.row_factory = sqlite3.Row
        with app.app_context():
            init_db(conn)  # Initialize the database with required tables
    else:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
    return conn

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to FlaskBlog" in response.data

def test_create_post(client):
    response = client.post('/create', data={
        'title': 'Test Post',
        'content': 'Test Content'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Post' in response.data

def test_edit_post(client):
    # First create a post
    client.post('/create', data={'title': 'Original', 'content': 'Original'})
    
    # Then edit it
    response = client.post('/1/edit', data={
        'title': 'Updated Post',
        'content': 'Updated Content'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Updated Post' in response.data

def test_delete_post(client):
    # First create a post
    client.post('/create', data={'title': 'To Delete', 'content': 'To Delete'})
    
    # Then delete it
    response = client.post('/1/delete', follow_redirects=True)
    print(response.data)
    assert response.status_code == 200
    assert b'To Delete' in response.data
