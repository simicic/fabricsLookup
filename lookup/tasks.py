import os
import click
from flask import current_app
from flask.cli import with_appcontext

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')


@click.command()
def test():
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose'])
    exit(rv)


@click.command()
@with_appcontext
def setup_database():
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import exc
    from lookup.fabrics.model import Fabric
    import csv

    db = SQLAlchemy(current_app)
    with open('data/fabrics.csv') as fabrics_csv:
        csv_reader = csv.reader(fabrics_csv, delimiter=',')

        for row in csv_reader:
            new_fabric = Fabric(row[0], row[1], row[2])
            try:
                db.session.add(new_fabric)
                db.session.commit()
            except exc.IntegrityError:
                db.session.rollback()
                continue
