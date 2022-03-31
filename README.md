# Flask User API

## Description

A simple [Flask](https://flask.palletsprojects.com/) User API that uses [JSON Web Tokens](https://jwt.io/) for user authentication. [SQLite](https://www.sqlite.org/index.html) is leveraged for persistent storage of user information.

## Usage

Input:
```
git clone https://github.com/foprel/flask-user-api.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

Output:
```
 * Serving Flask app 'api' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
```

## Todo
- Implement JWT authentication
- Implement user changes
- Standardize API responses
- Dockerize application
