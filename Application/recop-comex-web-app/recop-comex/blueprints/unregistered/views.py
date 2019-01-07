from flask import Blueprint, render_template
from data_access.models import event_information

import os

unregistered = Blueprint('unregistered', __name__, template_folder="templates")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@unregistered.route('/')
def index():

	#value = [1,1,1,'LALALA','1','1','1998-01-21','1','A'] 
	#event_information.add(value)
	event_information.show('A')

	return render_template('/unregistered/index.html', result=result)

@unregistered.route('/events')
def events():

	return render_template('/unregistered/events.html')

@unregistered.route('/partners')
def partners():

	return render_template('/unregistered/partners.html')

@unregistered.route('/contactus')
def contactus():

	return render_template('/unregistered/contactus.html')

@unregistered.route('/signup')
def signup():

	return render_template('/unregistered/signup.html')

@unregistered.route('/login')
def login():

	return render_template('/unregistered/login.html')