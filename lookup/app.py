from flask import Flask
from lookup import tasks
from lookup.fabrics import model
from lookup.settings import ProdConfig
from lookup.extensions import db, migrate
from lookup import fabrics

def create_app(config_object=ProdConfig):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_blueprints(app)
    register_extensions(app)
    register_shellcontext(app)
    register_commands(app)
    return app


def register_blueprints(app):
    app.register_blueprint(fabrics.views.blueprint)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_shellcontext(app):
    def shell_context():
        return {
            'db': db,
            'Fabric': model.Fabric
        }

    app.shell_context_processor(shell_context)


def register_commands(app):
    app.cli.add_command(tasks.test)
    app.cli.add_command(tasks.setup_database)
