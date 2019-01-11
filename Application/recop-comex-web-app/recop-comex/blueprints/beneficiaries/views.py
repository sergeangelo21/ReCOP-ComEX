from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user, login_required
from data_access.models import user_account, user_information

import os

beneficiaries = Blueprint('beneficiaries', __name__, template_folder="templates")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@beneficiaries.before_request
def before_request():

	if current_user.is_authenticated and not current_user.is_anonymous:

		check = user_information.query.filter_by(id=current_user.id).first()

		if current_user.type != 9:
			if check.type == 1:
				return redirect(url_for('registered.index'))
			if check.type == 2:
				return redirect(url_for('linkages.index'))
		else:
			return redirect(url_for('admin.index'))

@beneficiaries.route('/beneficiaries')
@login_required
def index():

	return render_template('/beneficiaries/index.html', title="Beneficiaries")

@beneficiaries.route('/beneficiaries/events')
@login_required
def events():

	return render_template('/beneficiaries/events.html', title="Beneficiaries")

@beneficiaries.route('/beneficiaries/reports')
@login_required
def reports():

	return render_template('/beneficiaries/reports.html', title="Beneficiaries")

@beneficiaries.route('/beneficiaries/contactus')
@login_required
def contactus():

	return render_template('/beneficiaries/contactus.html', title="Beneficiaries")

@beneficiaries.route('/beneficiaries/termsandconditions')
@login_required
def termsandconditions():

	return render_template('/beneficiaries/termsandconditions.html', title="Beneficiaries")

@beneficiaries.route('/beneficiaries/profile')
@login_required
def profile():

	return render_template('/beneficiaries/profile.html', title="Beneficiaries")
