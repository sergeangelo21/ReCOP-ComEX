from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, DecimalField, DateField, RadioField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError, NumberRange, Email
from datetime import date

class SearchForm(FlaskForm):
	search = StringField("Search", validators=[DataRequired()])
	submit = SubmitField("Search")

class ProposalForm(FlaskForm):
    title = StringField('Title of the Activity', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    objective = StringField('Objective', validators=[DataRequired()])
    budget = IntegerField('Estimated Budget', validators=[DataRequired()])
    location = StringField('Venue', validators=[DataRequired()])
    event_date = DateField('Target Date', validators=[DataRequired()])
    participant_no = IntegerField('No. of Participants', validators=[DataRequired()])
    min_age = IntegerField('Min Age', validators=[DataRequired()])
    max_age = IntegerField('Max Age', validators=[DataRequired()])
    thrust = SelectField('Thrust', choices = [("0","Please Choose One"),("1","Educational"),("2","Environmental"),("3","Health"),("4","Livelihood"),("5","Socio-Political"),("6","Spiritual")], validators=[DataRequired()])
    target_link = StringField('Target Linkages')
    select_link = SelectField('Select Linkages', choices=[("0", "Please Choose Here")])
    budget_plan = FileField('Budget Plan', validators=[FileRequired(), FileAllowed(['doc', 'docx'], 'Invalid file!')])
    programme = FileField('Programme', validators=[FileRequired(), FileAllowed(['doc', 'docx'], 'Invalid file!')])
    submit = SubmitField('Submit')

class AddTypeInventoryForm(FlaskForm):
    name = StringField('Type', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProfilePersonalUpdateForm(FlaskForm):
    firstname = StringField('First Name')
    middlename = StringField('Middle Name')
    lastname = StringField('Last Name')
    gender = RadioField('Gender', choices=[("M","Male"),("F","Female")])
    birthday = DateField('Birthday')
    bio = StringField('Bio')
    submit = SubmitField('Update')

class ProfileContactUpdateForm(FlaskForm):
    address = StringField('Address')
    telephone = IntegerField('Telephone Number')
    mobile = IntegerField('Mobile Number')
    email = StringField('Email Address')
    submit = SubmitField('Update')

class ProfileUsernameUpdateForm(FlaskForm):
    username = StringField('Username')
    oldpassword = PasswordField('Old Password')
    submit = SubmitField('Update')

class PasswordUpdateForm(FlaskForm):
    oldpassword = PasswordField('Old Password')
    password = PasswordField('Password')
    submit = SubmitField('Update')


