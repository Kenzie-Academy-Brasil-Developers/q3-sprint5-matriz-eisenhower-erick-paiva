from flask import Blueprint

bp = Blueprint('bp_tasks', __name__)

bp.post("/tasks")