from flask import Flask

def init_app(app: Flask):
    from .categorie_blueprint import bp as bp_categories
    from .task_blueprint import bp as bp_tasks
    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_tasks)
    