"""
Name :- Arman Arya
Homework1
Student ID : 24754624
"""

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'apps_user',       
    'password': 'Password123!', 
    'database': 'employee_data'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    new_salary = None
    
    if request.method == 'POST':
        
        name = request.form['employee_name']
        emp_id = int(request.form['employee_id'])
        salary = int(request.form['salary'])
        
        
        new_salary = salary * 1.05
        
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        query = "INSERT INTO employee_salary (employee_name, employee_id, salary) VALUES (%s, %s, %s)"
        values = (name, emp_id, salary)
        
        cursor.execute(query, values)
        conn.commit()
        
        
        cursor.close()
        conn.close()
        
    
    return render_template('index_ArmanArya.html', new_salary=new_salary)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
