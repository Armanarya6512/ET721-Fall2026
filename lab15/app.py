from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': '127.0.0.1',
    'user': 'flaskuser',
    'password': 'password123',
    'database': 'todo_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_tasks', methods=["GET"])
def get_tasks():
    try:
        conn = get_db_connection()
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tasks')
            tasks = cursor.fetchall()
        conn.close()
        return jsonify(tasks)
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")
    if task:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"status": "success"})
        except mysql.connector.Error as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    return jsonify({"status": "error"}), 400

@app.route("/delete_task", methods=["POST"])
def delete_task():
    data = request.get_json()
    task_id = data.get("id")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "deleted"})
    except mysql.connector.Error as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)