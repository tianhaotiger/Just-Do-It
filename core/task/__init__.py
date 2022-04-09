from flask import Blueprint

task = Blueprint('task', __name__, template_folder='task')


from . import views