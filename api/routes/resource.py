from flask import Blueprint
from ..helpers.authentication import token_required

resource = Blueprint('resource', __name__)


@resource.route('/resource', methods=['GET'])
@token_required
def route(user):
    return {
        'success': True,
        'message': 'Successfully retrieved /protected'
    }, 200