from flask import jsonify, app
from flask import Blueprint
from lookup.fabrics.model import Fabric
from .serializer import fabric_schema, fabrics_schema

blueprint = Blueprint('profiles', __name__)


@blueprint.route('/fabrics', methods=['GET'])
def get_textiles():
    all_textiles = Fabric.query.all()
    result = fabrics_schema.dump(all_textiles)

    return jsonify(result)


@blueprint.route('/fabrics/<id>', methods=['GET'])
def get_textile(id):
    fabric = Fabric.query.get(id)
    result = fabric_schema.dump(fabric)

    return jsonify(result)
