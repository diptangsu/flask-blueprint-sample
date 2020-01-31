from flask import Blueprint


sample_blueprint = Blueprint('sample', __name__)


@sample_blueprint.route('/sample')
def sample():
    return 'Sample'
