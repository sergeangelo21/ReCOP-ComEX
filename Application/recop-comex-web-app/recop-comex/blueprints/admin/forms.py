from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, DecimalField, DateField, RadioField, IntegerField, validators
from wtforms.validators import DataRequired, EqualTo, ValidationError, NumberRange, Email, Length
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

class NewInventoryForm(FlaskForm):
    item_type = RadioField('Item to be added', choices=[('1','New'), ('2','Existing')], validators=[DataRequired()])
    name = StringField('Item Name', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    is_donation = RadioField('From Donation?', choices=[('1','Yes'), ('2','No')], validators=[DataRequired()])
    give_to = RadioField('Given To', choices=[('1','Community'), ('2','Event')])
    sponsee = SelectField('Communities', choices=[('','ReCOP')])
    sponsor = SelectField('Sponsor', choices=[('1','Anonymous')])
    event = SelectField('Events', choices=[('', 'Please Choose One')])
    items = SelectField('Item Name', choices=[('', 'Please Choose One')])
    trans_slip   = FileField('Transaction Slip', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Invalid file!')])   
    submit = SubmitField('Submit')

class AddInventoryForm(FlaskForm):
    type_select = SelectField('Select Type', choices=[('', 'Please Choose Here')])
    quantity = StringField('Quantity')
    types = StringField('Types', validators=[DataRequired()])
    quantities = StringField('Quantities', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProfilePersonalUpdateForm(FlaskForm):
    firstname = StringField('First Name', [validators.Length(min=0, max=30)])
    middlename = StringField('Middle Name', [validators.Length(min=0, max=20)])
    lastname = StringField('Last Name', [validators.Length(min=0, max=20)])
    gender = RadioField('Gender', choices=[("M","Male"),("F","Female")])
    birthday = DateField('Birthday')
    bio = StringField('Bio', [validators.Length(min=0, max=160)])
    submit = SubmitField('Update')

class ProfileContactUpdateForm(FlaskForm):
    address = StringField('Address', [validators.Length(min=10, max=100)])
    telephone = StringField('Telephone Number', [validators.Length(min=7, max=15)])
    mobile = StringField('Mobile Number', [validators.Length(min=11, max=25)])
    email = StringField('Email Address', [validators.Length(min=0, max=30)] )
    submit = SubmitField('Update')

class ProfileUsernameUpdateForm(FlaskForm):
    username = StringField('Username')
    oldpassword = PasswordField('Old Password')
    submit = SubmitField('Update')

class PasswordUpdateForm(FlaskForm):
    oldpassword = PasswordField('Old Password')
    password = PasswordField('Password', [validators.Length(min=0, max=60)])
    submit = SubmitField('Update')


class PaginationForm(FlaskForm):
    page = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')