from flask import Blueprint
from ..helpers.authentication import token_required

protected = Blueprint('protected', __name__)


@protected.route('/protected')
@token_required
def route():
    return {
        'success': True,
        'message': 'Successfully retrieved /protected'
    }, 200