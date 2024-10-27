from flask import Blueprint


blueprint = Blueprint('posts', __name__)


@blueprint.route('/q')
def hello():
    return "hllo page"
