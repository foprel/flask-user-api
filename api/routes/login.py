from flask import Blueprint, request
from datetime import datetime, timedelta
from ..models.users import User
from ..config import Development
# Todo: Import jwt

login = Blueprint('login', __name__)

@login.route('/users/login', methods=['POST'])
def route():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not User.email_exists(email):
        return {
            'status': 'Conflict',
            'statusCode': 409,
            'message': 'User does not exist'
        }, 409

    if not User.check_password(password, email):
        return {
            'status': 'Forbidden',
            'statusCode': 403,
            'message': 'Password incorrect'
        }, 403

    return {
        'status': 'Success',
        'statusCode': 200,
        'message': 'User logged in'
    }, 200