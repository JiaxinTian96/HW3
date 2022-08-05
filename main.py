from flask import Flask, render_template, session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from crud import *

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_key'
# db:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app, db)
# class Myform(FlaskForm):
#     std_id = StringField('Student ID:', validators=[DataRequired()])
#     std_name = StringField('Name:')
#     std_grade = StringField('Grade:')
#     submit = SubmitField('Submit')
class Student(db.Model):
    __tablename__="students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    grade= db.Column(db.Integer)

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def __repr__(self):
        return f"Student: {self.name} Grage: {self.grade}"

@app.route ('/',methods=['GET'])

def index():
    # lable = ['Student ID','Name','Grade']
    return render_template('home.html')

@app.route ('/add', methods=['GET','POST'])

def add():
    form = add_student()
    if form.validate_on_submit():

        name = form.name.data
        grade = form.grade.data #
        new_student = Student(name,grade) #
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('list_student'))

    return render_template('add.html', form=form)

@app.route('/full')

def list_student():
    students = Student.query.all()
    return render_template('full.html', students=students)


@app.route('/delete', methods=['GET', 'POST'])

def delete():
    form = del_student()
    if form.validate_on_submit():
        id = form.id.data
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('list_student'))

    return render_template('delete.html', form=form)

@app.route('/pass')

def pass_student():
    students = Student.query.filter(Student.grade>=85)
    return render_template('full.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)