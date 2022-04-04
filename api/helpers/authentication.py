from functools import wraps
from flask import request
from ..config import Development
from ..models.users import User
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
            payload = jwt.decode(token, Development.SECRET_KEY)
            email = payload['email']
            exp = payload['exp']

        except Exception:
            return {
                'success': False,
                'message': 'Invalid token'
            }, 400

        return f(user, *args, **kwargs)

    return decorator


        
