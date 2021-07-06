import jwt
from flask import jsonify, request
from functools import wraps

from app import app


# GUIDE: This function ensures that a url endpoint is authenticated
# This is actually defining a function decorator!
# https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
# the decorator checks to see if there is a valid jwt token
# https://jwt.io
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "Authorization" in request.headers:
            # Check whether token was sent
            authorization_header = request.headers["Authorization"]

            # Check whether token is valid
            try:
                token = authorization_header.split(" ")[1]
                user = jwt.decode(token, app.config["SECRET_KEY"])
            # TODO: Use correct error
            except ZeroDivisionError:
                return jsonify({"error": "You are not logged in"}), 401

            return f(username=user["username"], *args, **kwargs)
        else:
            return jsonify({"error": "You are not logged in"}), 401
    return wrap

def confirm_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "Authorization" in request.headers:
            # Check whether token was sent
            authorization_header = request.headers["Authorization"]

            # Check whether token is valid
            try:
                token = authorization_header.split(" ")[1]
                user = jwt.decode(token, app.config["SECRET_KEY"])
            # TODO: Use correct error
            except ZeroDivisionError:
                return jsonify({"error": "You are not logged in"}), 401
            if isverified:
                return f(username=user["username"], *args, **kwargs)
            else:
                return jsonify({"error": "Your account is not verified"}), 401
        else:
            return jsonify({"error": "You are not logged in"}), 401
            
    return wrap
