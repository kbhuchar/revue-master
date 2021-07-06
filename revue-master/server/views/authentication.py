import jwt

from flask import jsonify, request, Flask, url_for
from models import User
from schema import Schema, Regex
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from authorization import login_required
from app import app

#config for the flask_mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'knoxrateaservice@gmail.com' 
app.config['MAIL_PASSWORD'] = 'team5@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
s = URLSafeTimedSerializer('Nooneknow')

MAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@knox+\.+edu+$)"

# GUIDE: requests to api endpoints, such as /api/signup are dealt with by individual functions
# The route function wrapper here has an argument, methods=["POST"]. This tells Flask that this function
# will only respond to POST requests. POST requests are used to send data to the server.
# https://www.w3schools.com/tags/ref_httpmethods.asp
@app.route("/api/signup", methods=["POST"])
def sign_up():
    schema = Schema({
        "username": str,
        "email": Regex(MAIL_REGEX, error="Mail address is invalid"),
        "password": str
    })
    validated = schema.validate(request.json)

    if User.objects(username=validated["username"]):
        return jsonify({"error": "Username not available"}), 409
    if User.objects(email=validated["email"]):
        return jsonify({"error": "There is already an account with your email address"}), 409

    # Hash password with sha256
    hashed_password = generate_password_hash(validated["password"])

    user = User(
        username=validated["username"],
        email=validated["email"],
        password=hashed_password
    ).save()


    token = jwt.encode({
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "created": str(user.created)
    }, app.config["SECRET_KEY"])

    return jsonify({
        "success": True,
        "user": {
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "created": str(user.created)
        },
        "token": token.decode("UTF-8")
    })



@app.route("/api/login", methods=["POST"])
def login():
    schema = Schema({
        "username": str,
        "password": str
    })
    validated = schema.validate(request.json)

    users = User.objects(username=validated["username"])

    if len(users) == 0:
        return jsonify({"error": "User not found"}), 403

    user = users.first()

    if not check_password_hash(user.password, validated["password"]):
        return jsonify({"error": "Invalid password"}), 401

    token = jwt.encode({
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "created": str(user.created)
    }, app.config["SECRET_KEY"])

    return jsonify({
        "success": True,
        "user": {
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "created": str(user.created)
        },
        "token": token.decode("UTF-8")
    })


@app.route("/api/confirmation", methods=["GET"])
@login_required
def send_email(username: str):
#send email
    user = User.objects(username=username).first()
    email = str(user.email)
    conf = s.dumps(email, salt = 'email-confirm')
    msg = Message('Confirm Email', sender='knoxrateaservice@gmail.com', recipients=[email])
    link = url_for('confirm_email', token=conf, _external=True)
    msg.body = 'Please click the link {} to verify your email'.format(link)
    mail.send(msg)
    return 'success'

@app.route("/api/confirm_email/<token>")
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        user = User.objects(email=email).first()
        user.confirmed = True;
        user.save();
    except SignatureExpired:
        return '<h1>The link is expired!</h1>'
    return '<h1>Your email has been verified please go back to the login page!</h1>'
