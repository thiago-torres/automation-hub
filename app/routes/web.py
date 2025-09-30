from flask import Blueprint, render_template

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def index():
    return render_template('index.html')

@web_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404