from flask import Blueprint

bp = Blueprint('bp_categories', __name__)

bp.post("/categories")
