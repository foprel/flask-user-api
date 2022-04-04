from flask import Blueprint, request
from ..models.users import User


register = Blueprint('register', __name__)

@register.route('/users/register', methods=['POST'])
def route():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.email_exists(email):
        return {
            'success': False,
            'status': 'Conflict',
            'statusCode': 409,
            'message': 'User does already exist'
        }, 409

    password = User.hash_password(password)

    user = User(
        username=username,
        email = email,
        password=password
    )

    try:
        user.create()
    except Exception as e:
        return {
            'success': False,
            'status': 'Unknown error',
            'statusCode': 520,
            'message': 'User not created'
        }, 520
    else:
        return {
            'success': True,
            'status': 'Success',
            'statusCode': 201,
            'message': 'User created'
        }, 201