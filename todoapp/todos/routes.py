from flask import Blueprint, render_template
from flask_login import login_required

todos = Blueprint('todos', __name__)

@todos.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')