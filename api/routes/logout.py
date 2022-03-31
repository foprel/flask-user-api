from flask import Blueprint


logout = Blueprint('logout', __name__)

@logout.route('/users/logout', methods=['POST'])
def route():
    return {}, 200