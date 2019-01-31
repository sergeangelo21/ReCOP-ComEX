from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from blueprints.unregistered.forms import LoginForm, SignupForm
from data_access.models import user_account, user_information, audit_trail
from data_access.queries import user_views, event_views, linkage_views
from datetime import datetime

from static.email import confirm

import os, json

unregistered = Blueprint('unregistered', __name__, template_folder="templates")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@unregistered.route('/')
def index():

	return render_template('/unregistered/index.html')

@unregistered.route('/events')
def events():

	events = event_views.show_list('all', ' ')

	return render_template('/unregistered/events/index.html', events=events)

@unregistered.route('/linkages')
def linkages():

	linkages = linkage_views.show_list('A', ' ')

	return render_template('/unregistered/linkages/index.html', linkages=linkages)

@unregistered.route('/donate')
def donate():

	return render_template('/unregistered/donate/index.html')

@unregistered.route('/contactus')
def contactus():

	return render_template('/unregistered/contactus/index.html')

@unregistered.route('/signup', methods=['GET', 'POST'])
def signup():

	form = SignupForm()

	if form.validate_on_submit():

		id_information = user_information.count()
		id_account = user_account.count()

		value_information = [
			id_information,form.firstname.data,form.middlename.data,
			form.lastname.data,form.company.data,form.bio.data,form.gender.data,form.birthday.data,
			form.address.data,form.telephone.data,form.mobile.data,form.thrust.data
			]

		if form.type.data == '2':
			status = "A"
			flash('Your account was successfully created!', 'success')
		else:
			status = "N"
			flash('Your account has been created! Please wait for MOA.', 'success')

		value_account = [
			id_account,id_information,form.username.data,
			form.password.data,form.email.data,form.type.data,datetime.now(),status
			]

		user_account.add(value_account)
		user_information.add(value_information)	

		return redirect(url_for('unregistered.login'))


	return render_template('/unregistered/signup/index.html', form=form)

@unregistered.route('/login', methods=['GET', 'POST'])
def login():

	form = LoginForm()

	if form.validate_on_submit():
        
		user = user_account.login([form.username.data, form.password.data])

		if user is None or user.type==5:
			flash('Invalid username or password', 'error')
			return redirect(url_for('unregistered.login'))

		if user.status != "A":

			if user.status=="P":
				flash('MOA not yet acknowledged. Please check your email.', 'info')
			else:
				flash('Inactive account. Please contact the Re-COP Director.', 'error')
			
			return redirect(url_for('unregistered.login'))

		login_user(user, remember=form.remember_me.data)

		name = user_views.login_info(current_user.id)

		if current_user.type == 3:
			name = name.company_name
		else:
			name = name.first_name
			
		flash('Welcome ' + name + '!', 'success')

		if current_user.type == 2:
			return redirect(url_for('registered.index'))
		elif current_user.type == 3:
			return redirect(url_for('linkages.index'))
		elif current_user.type == 4:
			return redirect(url_for('communities.index'))
		elif current_user.type == 1:
			return redirect(url_for('admin.index'))	
	
	return render_template('/unregistered/login/index.html', form=form)

@unregistered.route('/logout')
def logout():

	user_account.logout()

	logout_user()

	flash('You are logged out.', 'success')

	return redirect('/')

@unregistered.route('/linkages/<token>')
def confirm_linkage(token, expiration = 3600):

	id = confirm(token)

	if id=='bad':
		flash('Link already expired. Please contact the ReCOP Administrator.', 'error')
		return redirect(url_for('unregistered.index'))

	status = 'A'

	user = user_account.retrieve_user(id)

	if id and user.status=='P':
		
		user_account.update_status(id, status)

		audit_id = audit_trail.count()
		value = [audit_id,id,id,'partner',2]
		audit_trail.add(value)

		flash("MOA acknowledged! Your account is now active.", 'success')

	else:
		flash("MOA already acknowledged. Please login.", 'info')
	
	return redirect(url_for('unregistered.login'))

@unregistered.route('/signing/<action>/<token>')
def event_signing(token, action, expiration = 3600):

	flash('Event was ' + action, 'warning')

	return redirect(url_for('unregistered.login'))

