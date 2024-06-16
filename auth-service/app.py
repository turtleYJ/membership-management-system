import os
import logging
import jwt
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app, resources={r"/*": {"origins": "*"}})

# In-memory database for demonstration purposes
users = {}

# 로그 설정
log_dir = '/tmp/log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, 'flask.log'),
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)

@app.route('/auth/register', methods=['POST', 'OPTIONS'])
@cross_origin()
def register():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'Options request successful'}), 200
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    app.logger.debug(f"Register attempt for username: {username}")

    if username in users:
        app.logger.warning(f"User already exists: {username}")
        return jsonify({'message': 'User already exists!'}), 400

    users[username] = generate_password_hash(password)
    return jsonify({'message': 'User created successfully!'}), 201

@app.route('/auth/login', methods=['POST', 'OPTIONS'])
@cross_origin()
def login():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'Options request successful'}), 200
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    app.logger.debug(f"Login attempt for username: {username}")

    if username not in users or not check_password_hash(users[username], password):
        app.logger.warning(f"Invalid credentials for username: {username}")
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    token = jwt.encode(
        {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    app.logger.info(f"User logged in successfully: {username}")
    return jsonify({'token': token}), 200

if __name__ == '__main__':
    app.logger.info("hello, auth-service!")
    app.run(debug=True, host='0.0.0.0', port=5001)
