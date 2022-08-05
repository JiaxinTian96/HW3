from flask_wtf import FlaskForm
# from main import db, Student
from wtforms import *

class add_student(FlaskForm):

    name = StringField("Student Name: ")
    grade = IntegerField("Student Grade: ")
    submit = SubmitField("add")

class del_student(FlaskForm):

    id = IntegerField("Student Id: ")
    submit = SubmitField("delete")
