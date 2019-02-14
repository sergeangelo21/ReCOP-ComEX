from flask import Flask, Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user, login_required
from blueprints.registered.forms import *
from data_access.models import donation, user_account, user_information
from data_access.queries import user_views, linkage_views, event_views
from datetime import datetime

from extensions import db, bcrypt
import os


registered = Blueprint('registered', __name__, template_folder="templates")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@registered.before_request
def before_request():

	if current_user.is_authenticated and not current_user.is_anonymous:

		if current_user.type == 3:
			return redirect(url_for('linkages.index'))
		elif current_user.type == 4:
			return redirect(url_for('communities.index'))
		elif current_user.type == 1:
			return redirect(url_for('admin.index'))

		user_account.logout()

@registered.route('/registered')
@login_required
def index():

	return render_template('/registered/index.html')

@registered.route('/registered/events')
@login_required
def events():

	return render_template('/registered/events/index.html')

@registered.route('/registered/events/create')
@login_required
def events_create():

	return render_template('/registered/events/create.html')

@registered.route('/registered/linkages')
@login_required
def linkages():

	return render_template('/registered/linkages/index.html')

@registered.route('/registered/donate',methods=['GET', 'POST'])
@login_required
def donate():

	form = DonationForm()

	communities = linkage_views.target_linkages()

	for c in communities:

		if c.type==4:
			form.sponsee.choices.extend([(str(c.id), c.address)])

	events = event_views.show_list('S', ' ')

	if events:
		form.event.choices.extend(([str(e.id), e.name] for e in events))
		no_event = 0
	else: 
		form.event.data=''
		no_event = 1

	if form.validate_on_submit():

		if form.give_to.data=='1':
			if form.sponsee.data:
				sponsee = form.sponsee.data
			else:
				sponsee = 1

			event = None
		else:
			event = form.event.data
			sponsee= None

		file = form.trans_slip.data
		old, extension = os.path.splitext(file.filename)

		new = donation.last_added()
		filename = str(new)+extension

		trans_path = 'static/output/donate/trans_slip/' + filename

		value = [None,sponsee,event,current_user.info_id,form.amount.data,trans_path]

		donation.add(value)
		file.save(trans_path)

		flash('Donation given!', 'success')
		return redirect(url_for('registered.donate'))

	return render_template('/registered/donate/index.html', form=form, no_event=no_event)

@registered.route('/registered/contactus')
@login_required
def contactus():

	return render_template('/registered/contactus/index.html')

@registered.route('/registered/termsandconditions')
@login_required
def termsandconditions():

	return render_template('/registered/termsandconditions/index.html')

@registered.route('/registered/profile/about/<user>')
@login_required
def profile_about(user):

	registered = user_views.profile_info(current_user.info_id)

	return render_template('/registered/profile/about.html', title="registered", registered=registered)

@registered.route('/registered/profile/eventsattended')
@login_required
def profile_eventsattended():

	return render_template('/registered/profile/eventsattended.html', title="registered")	

@registered.route('/registered/profile/settings/personal', methods=['GET', 'POST'])
@login_required
def profile_settings_personal():

	user_information_update = user_information.profile_info_update(current_user.info_id)

	form = ProfilePersonalUpdateForm()

	if form.validate_on_submit():

		user_information_update.first_name = form.firstname.data
		user_information_update.middle_name = form.middlename.data
		user_information_update.last_name = form.lastname.data
		user_information_update.gender = form.gender.data
		user_information_update.birthday = form.birthday.data
		user_information_update.bio = form.bio.data

		db.session.commit()

		flash('Profile was successfully updated!', 'success')

		return redirect(url_for('registered.profile_settings_personal'))

	else:

		form.firstname.data = user_information_update.first_name
		form.middlename.data = user_information_update.middle_name
		form.lastname.data = user_information_update.last_name
		form.gender.data = user_information_update.gender
		form.birthday.data = user_information_update.birthday
		form.bio.data = user_information_update.bio

	return render_template('/registered/profile/settings/personal.html', form=form)

@registered.route('/registered/profile/settings/contact', methods=['GET', 'POST'])
@login_required
def profile_settings_contact():

	user_information_update = user_information.profile_info_update(current_user.info_id)
	user_account_update = user_account.profile_acc_update(current_user.info_id)

	form = ProfileContactUpdateForm()

	if form.validate_on_submit():

		user_information_update.address = form.address.data
		user_information_update.telephone = form.telephone.data
		user_information_update.mobile_number = form.mobile.data

		db.session.commit()

		user_account_update.email_address = form.email.data

		db.session.commit()

		flash('Profile was successfully updated!', 'success')

		return redirect(url_for('registered.profile_settings_contact'))

	else:

		form.address.data = user_information_update.address
		form.telephone.data = user_information_update.telephone
		form.mobile.data = user_information_update.mobile_number
		form.email.data = user_account_update.email_address

	return render_template('/registered/profile/settings/contact.html', form=form)	

@registered.route('/registered/profile/settings/username', methods=['GET', 'POST'])
@login_required
def profile_settings_username():

	user_account_update = user_account.profile_acc_update(current_user.info_id)

	form = ProfileUsernameUpdateForm()

	if form.validate_on_submit():

		user = user_account.login([current_user.username, form.oldpassword.data])

		if user:

			user_account_update.username = form.username.data

			db.session.commit()

			flash('Username was successfully updated!', 'success')

			return redirect(url_for('registered.profile_settings_username'))

		else:

			flash('Wrong password.', 'error')

	else:

		form.username.data = user_account_update.username

	return render_template('/registered/profile/settings/username.html', form=form)

@registered.route('/registered/profile/update/password', methods=['GET', 'POST'])
@login_required
def profile_settings_password():

	user_account_update = user_account.profile_acc_update(current_user.info_id)

	form = PasswordUpdateForm()

	if form.validate_on_submit():

		user = user_account.login([current_user.username, form.oldpassword.data])

		if user:

			user_account_update.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

			db.session.commit()

			flash('Password was successfully updated!', 'success')

			return redirect(url_for('registered.profile_settings_password'))

		else:

			flash('Wrong password.', 'error')

	return render_template('/registered/profile/settings/password.html', form=form)