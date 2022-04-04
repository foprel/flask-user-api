from flask import Blueprint, request
from ..models.users import User


register = Blueprint('register', __name__)

@register.route('/users/register', methods=['POST'])
def route():

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.get_by_email(email):
        return {
            'success': False,
            'status': 'Conflict',
            'statusCode': 409,
            'message': 'User does already exist'
        }, 409

    user = User(
        username=username,
        email = email,
        password=password
    )

    user.hash_password(password)
    user.save()
    
    return {
        'success': True,
        'status': 'Success',
        'statusCode': 201,
        'message': 'User created'
    }, 201