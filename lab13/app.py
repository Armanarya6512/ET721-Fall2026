from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blogs')
def blogs():
    cursor.execute("SELECT blog.id, user.username, blog.title, blog.content, blog.created_at FROM blog user ON blog.user_id = users.userid ")

  # get all the data and store them in 'data'
    data = cursor.fetchall()

    return render_template('blogs.html', blogs = data)
if __name__ == '__main__':
    app.run(debug=True)