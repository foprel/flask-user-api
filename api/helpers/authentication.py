from datetime import datetime
from functools import wraps
from flask import request
from ..config import Development
from ..models.users import User
from ..models.users import TokenBlocklist
import jwt

def token_required(f):
    
    @wraps(f)
    
    def decorator(*args, **kwargs):

        try:
            token = request.headers['authorization']
        except:
            token = None
            return {
                'success': False,
                'message': 'No token found'
            }, 400

        try:
            payload = jwt.decode(token, Development.SECRET_KEY, algorithms=['HS256'])
            email = payload['email']
            exp = payload['exp']
            
            # Check if user exists
            user = User.get_by_email(email)

            if not user:
                return {
                    'success': False,
                    'message': 'User does not exist'
                }, 400

            if datetime.utcnow() > datetime.utcfromtimestamp(exp):
                return {
                    'success': False,
                    'message': 'Token has expired'
                }, 400                  

            token_expired = TokenBlocklist.check_jwt_active(token)

            if token_expired:
                return {
                    'success': False,
                    'message': 'Token has been revoked'
                }, 400

            if not user.check_jwt_auth():
                return {
                    'success': False,
                    'message': 'User has no token'
                }, 400

        except Exception:
            return {
                'success': False,
                'message': 'Invalid token'
            }, 400

        return f(user, *args, **kwargs)

    return decorator


        
