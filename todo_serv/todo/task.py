from copy import deepcopy

from flask import Blueprint, request, abort, render_template
from .models import Task
from ..utilits.binary_serch import binary_search
from ..utilits.bubble_sort import bubble_sort
from ..utilits.insertion_sort import *



bp = Blueprint('task', __name__)



@bp.route('/', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        title = request.form['title']
        priority = int(request.form['priority'])
        new_task = Task(title=title, priority=priority)
    else:
        order = request.args.get(
            'order', default='', type=str)
        task = deepcopy(Task.objects)
        if order:
            bubble_sort(task, order)
        else:
            insertion_sort(task)
    return render_template('task_list.html', tasks=Task.objects)


@bp.route('/<int:task_id>')
def task_detail(task_id):
    id_id = [task.id for task in Task.objects]
    # for task in Task.objects:
    #     id_id.append(task.id)
    task = binary_search(id_id, task_id)
    if task:
        return Task.objects[task - 1].to_json()
    else:
        abort(404)



