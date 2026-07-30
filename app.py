
#render_template - used to go through the folder called template.It can access the files inside it.


from flask import Flask , render_template ,request
from pymongo import MongoClient

  #imports flask class from flask module

client = MongoClient('mongodb://127.0.0.1:27017')
db= client['student_db']
collection = db['students']

app= Flask(__name__)    # we created an instance of flask class(we r creating a application)
@app.route('/')   # creates  the URL/ route for the home page
def home():    #home page..maybe..?
    return render_template('index.html')    # response to be sent to client

@app.route('/about')
def about():
    return "This page contains details of my project"

@app.route('/contacts')
def contacts():
    return "Contact me through email: 25cb@ngp.ac.in"

@app.route('/skills')
def skills():
    return "I have learnt few skils like :python , c, django , flask ,html , css"

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        sname= request.form['studentName']
        semail= request.form['studentEmail']
        sphone = request.form['studentPhone']
        sdepartment = request.form['departmentSelect']
        sgender = request.form.get('gender')
        sskills = request.form.getlist('skills')
        student_data={
            'name':sname,
            'email':semail,
            'phone':sphone,
            'department': sdepartment,
            'gender':sgender,
            'skills': sskills
        }
        collection.insert_one(student_data)
        return render_template('success.html', name=sname,email=semail,phone=sphone,department=sdepartment,gender=sgender,skills=sskills)
    return render_template('formbs.html')

if __name__=="__main__":

    app.run(debug=True)         #automatically reloads server for evry changes
