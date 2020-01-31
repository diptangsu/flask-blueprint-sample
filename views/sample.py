from flask import Blueprint
from flask import render_template


sample_blueprint = Blueprint('sample', __name__)


@sample_blueprint.route('/sample')
def sample():
    return 'Sample'


@sample_blueprint.route('/page')
def page():
    return render_template('page.html')
