from flask import Flask, render_template, redirect, request, url_for
import mysql.connector

app = Flask(__name__)


# database connection
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="flaskuser",
        password="password123",
        database="blogDB"
    )


# home page: shows the form to create a blog
@app.route('/')
def index():
    return render_template('index.html')


# collects all data in the blog and users tables and displays it on blogs.html
@app.route('/blogs')
def blogs():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT blog.id, users.username, blog.title, blog.content, blog.created_at
                FROM blog
                JOIN users ON blog.user_id = users.userid
            """)
            # get all the data and store it in 'data'
            data = cursor.fetchall()
        finally:
            cursor.close()
    finally:
        connection.close()

    return render_template('blogs.html', blogs=data)


# add a new blog post to the database
@app.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    # if someone opens /add_blog directly, send them to the form
    if request.method != 'POST':
        return redirect(url_for('index'))

    title = request.form['title']
    content = request.form['content']
    username = request.form['username']
    email = request.form['email']

    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        try:
            # insert the user first
            cursor.execute(
                "INSERT INTO users(username, email) VALUES (%s, %s)",
                (username, email)
            )
            connection.commit()

            # id of the user we just inserted
            user_id = cursor.lastrowid

            # insert the blog post linked to that user
            cursor.execute(
                "INSERT INTO blog(user_id, title, content) VALUES (%s, %s, %s)",
                (user_id, title, content)
            )
            connection.commit()
        finally:
            cursor.close()
    finally:
        connection.close()

    return redirect(url_for('blogs'))


if __name__ == '__main__':
    app.run(debug=True)