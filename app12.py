from flask import Flask,render_template,request,jsonify
import json
import os

app= Flask(__name__)

DATABASE = "students.json"

def load_students():
    if os.path.exists(DATABASE):
        with open(DATABASE , 'r') as file:
            return json.load(file)

    return[]

def save_students(data):
    with open (DATABASE , 'w') as file:
        json.dump(data, file ,indent =4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('formbs.html')

@app.route('/register' , methods =['POST'])
def register_student():

    students = load_students()
    student={
        "name":request.form['studentName'],
        "email": request.form['studentEmail'],
        "phone" : request.form['studentPhone'],
        "department": request.form['departmentSelect'],
        "gender": request.form.get('gender'),
        "skills": request.form.getlist('skills')
        }
    students.append(student)
    save_students(students)

    return render_template(
        "success.html",
        student =student 
    )

@app.route('/students')

def get_students():
    students = load_students
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)

