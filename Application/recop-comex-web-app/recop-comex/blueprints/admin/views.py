from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user, login_required
from data_access.models import user_account, user_information

import os

admin = Blueprint('admin', __name__, template_folder="templates")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@admin.before_request
def before_request():

	if current_user.is_authenticated and not current_user.is_anonymous:

		check = user_information.query.filter_by(id=current_user.id).first()

		if check.type == 1:
			return redirect(url_for('registered.index'))
		if check.type == 2:
			return redirect(url_for('linkages.index'))
		if check.type == 3:
			return redirect(url_for('beneficiaries.index'))

@admin.route('/admin')
@login_required
def index():

	return render_template('/admin/index.html', title="Admin")

@admin.route('/admin/events')
@login_required
def events():

	return render_template('/admin/events.html', title="Admin")

@admin.route('/admin/proposals')
@login_required
def proposals():

	return render_template('/admin/proposals.html', title="Admin")

@admin.route('/admin/partners')
@login_required
def partners():

	return render_template('/admin/partners.html', title="Admin")

@admin.route('/admin/beneficiaries')
@login_required
def beneficiaries():

	return render_template('/admin/beneficiaries.html', title="Admin")

@admin.route('/admin/reports')
@login_required
def reports():

	return render_template('/admin/reports.html', title="Admin")

@admin.route('/admin/feedbacks')
@login_required
def feedbacks():

	return render_template('/admin/feedbacks.html', title="Admin")

@admin.route('/admin/profile')
@login_required
def profile():

	return render_template('/admin/profile.html', title="Admin")
