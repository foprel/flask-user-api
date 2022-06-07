# Flask User API

> :warning: **Security warning**: This project is experimental and provided as-is (see MIT license).

## Description

A simple [Flask](https://flask.palletsprojects.com/) User API that leverages [JSON Web Tokens](https://jwt.io/) for user authentication. [SQLite](https://www.sqlite.org/index.html) is used for persistent storage of user information.

## Usage

Input:

``` console
git clone https://github.com/foprel/flask-user-api.git
cd flask-user-api
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
flask run
```

Output:

``` console
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

## Docker

Follow these steps to run the application in docker:

``` console
docker build --tag flask-user-api .
docker run --publish 5000:5000 flask-user-api
```
