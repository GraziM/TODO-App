from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
from flask_login import login_required, current_user
from todoapp import db
from todoapp.models import User, Todo
from .forms import TodoForm, UpdateTodoForm

todos = Blueprint('todos', __name__)

@todos.route('/', methods=['GET', 'POST'])
@todos.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(title=form.title.data, description=form.description.data, author=current_user)
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', todos=todos, form=form, title="Dashboard")

@todos.route('/delete/<int:todo_id>', methods=['POST'])
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if todo.author != current_user:
        abort(403)
    db.session.delete(todo)
    db.session.commit()
    flash('Your todo has been deleted!', 'success')
    return redirect(url_for('todos.dashboard'))

@todos.route('/update/<int:todo_id>', methods=['GET','POST'])
@login_required
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if todo.author != current_user:
        abort(403)
    form = UpdateTodoForm()
    if form.validate_on_submit():
        todo.title = form.title.data
        todo.description = form.description.data
        db.session.commit()
        flash('Your Todo has been updated!', 'success')
        return redirect(url_for('todos.dashboard'))
    elif request.method == 'GET':
        form.title.data = todo.title
        form.description.data = todo.description
        return render_template('dashboard.html', form=form)
