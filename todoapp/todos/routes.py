from flask import Blueprint, render_template
from flask_login import login_required, current_user
from todoapp import db
from todoapp.models import User, Todo
from .forms import TodoForm

todos = Blueprint('todos', __name__)

@todos.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = TodoForm()
    if form.validate_on_submit():
        print('1')
        todo = Todo(title=form.title.data, description=form.description.data, author=current_user)
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', todos=todos, form=form)