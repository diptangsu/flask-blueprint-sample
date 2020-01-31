from flask import Blueprint


pages_blueprint = Blueprint('pages', __name__)


@pages_blueprint.route('/<int:page_id>')
def sample(page_id):
    return f'Page {page_id}'
