from datetime import datetime, timedelta
from flask import Blueprint, request
from ..models.users import User
from ..config import Development
import jwt


login = Blueprint('login', __name__)

@login.route('/users/login', methods=['POST'])
def route():

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.get_by_email(email)

    if not user:
        return {
            'success': False,
            'status': 'Conflict',
            'statusCode': 409,
            'message': 'User does not exist'
        }, 409

    if not user.check_password(password):
        return {
            'success': False,
            'status': 'Forbidden',
            'statusCode': 403,
            'message': 'Password incorrect'
        }, 403

    token = jwt.encode({'email': email, 'exp': datetime.utcnow() + timedelta(minutes=30)}, Development.SECRET_KEY)

    user.set_jwt_auth(True)
    user.save()

    return {
        'success': True,
        'status': 'Success',
        'statusCode': 200,
        'message': 'User logged in',
        'token': token
    }, 200