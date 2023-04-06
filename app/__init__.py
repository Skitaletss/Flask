from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
babel = Babel()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    babel.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from app.routes import MyMainView
    admin = Admin(app, 'Sam creat', index_view=MyMainView(), template_mode='bootstrap4', url='/')

    return app
