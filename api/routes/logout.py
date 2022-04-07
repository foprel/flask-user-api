from datetime import datetime
from flask import Blueprint, request
from ..helpers.authentication import token_required
from ..models.users import User, TokenBlocklist

logout = Blueprint('logout', __name__)

@logout.route('/users/logout', methods=['POST'])
@token_required
def route(user):

    # Disable user token
    user.jwt_auth = False
    user.save()

    # Revoke user token
    token = request.headers['authorization']

    blocklist = TokenBlocklist(
        token = token,
        created_at = datetime.utcnow()
    )

    blocklist.save()

    return {
        'success': True,
        'message': 'User logged out' 
    }, 200