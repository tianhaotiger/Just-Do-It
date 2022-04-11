from flask import render_template, redirect, url_for, request, jsonify
from ..models import Todo
from . import task
from .forms import TaskForm
from .. import db


@task.route('/create-task', methods=["GET", "POST"])
def tasks():
    form = TaskForm()

    # when the request method is post
    if request.method == "POST":
        # editing
        if form.id.data is not None:
            try:
                tID = int(form.id.data)
                print(tID)
                title = form.title.data
                date = form.date.data
                todo = db.session.query(Todo).filter(Todo.id == tID).first()
                todo.title = title
                todo.date = date
                db.session.commit()
                return redirect(url_for('task.tasks'))
            except Exception as e:
                print(e)
                return redirect(url_for('task.tasks'))
        # creating
        elif form.validate_on_submit():
            todo = Todo(title=form.title.data, date=form.date.data, status="To Do")
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('task.tasks'))

    # sort by ddl ascending
    query = Todo.query.order_by(Todo.date)
    items = query.all()

    return render_template('tasks.html', title='Create Tasks', items=items, form=form)


@task.route('/delete/<int:task_id>', methods=["POST"])
def delete(task_id):
    try:
        todo = Todo.query.filter_by(id=int(task_id)).one()
        print(todo)
        db.session.delete(todo)
        db.session.commit()
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@task.route('/progress/<int:task_id>', methods=["POST"])
def progress(task_id):
    try:
        todo = Todo.query.filter_by(id=int(task_id)).one()
        print(todo)
        data = request.get_json()
        todo.status = data['status']
        db.session.commit()
        result = {'success': True, 'response': 'updated task progress'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@task.route('/edit/<int:tID>', methods=["GET", "POST"])
def edit(tID):
    if tID != 0:
        form = TaskForm(id=tID)

    if request.method == "POST":
        # editing
        if request.form.get('id') is not None:
            try:
                tID = int(request.form.get('id'))
                print(tID)
                title = request.form.get('title')
                date = request.form.get('date')
                print(title)
                print(date)
                todo = db.session.query(Todo).filter(Todo.id == tID).first()
                todo.title = title
                todo.date = date
                db.session.commit()
                return redirect(url_for('task.tasks'))
            except Exception as e:
                print(e)
                return redirect(url_for('task.tasks'))
        # creating
        elif form.validate_on_submit():
            todo = Todo(title=form.title.data, date=form.date.data, status="To Do")
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('task.tasks'))
    else:
        result = {'success': True, 'response': tID}
        # return jsonify(result)
        return render_template('tasks.html', title='Edit Tasks', form=form, ind=tID)
