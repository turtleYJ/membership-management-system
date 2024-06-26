import os
import logging
import jwt
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app, resources={r"/*": {"origins": "*"}})

users = {}

log_dir = '/tmp/log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, 'flask.log'),
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            app.logger.warning('Token is missing')
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['username']
        except:
            app.logger.warning('Token is invalid')
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/user', methods=['GET', 'OPTIONS'])
@cross_origin()
@token_required
def get_user(current_user):
    if request.method == 'OPTIONS':
        return jsonify({'message': 'Options request successful'}), 200
    app.logger.debug(f"User info requested for username: {current_user}")

    user_info = {
        'username': current_user
    }
    app.logger.info(f"User info sent successfully: {current_user}")
    return jsonify(user_info), 200

@app.route('/user', methods=['PUT', 'OPTIONS'])
@cross_origin()
@token_required
def update_user(current_user):
    if request.method == 'OPTIONS':
        return jsonify({'message': 'Options request successful'}), 200
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({'message': 'Password is missing!'}), 400
    
    users[current_user] = generate_password_hash(password)
    app.logger.info(f"User updated: {current_user}")
    return jsonify({'message': 'User updated successfully!'}), 200

@app.route('/user/recover', methods=['POST', 'OPTIONS'])
@cross_origin()
def recover_password():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'Options request successful'}), 200
    data = request.get_json()
    username = data.get('username')
    new_password = data.get('new_password')

    if username not in users:
        return jsonify({'message': 'User does not exist!'}), 400

    users[username] = generate_password_hash(new_password)
    app.logger.info(f"Password recovered for: {username}")
    return jsonify({'message': 'Password recovered successfully!'}), 200

if __name__ == '__main__':
    app.logger.info("hello, user-service!")
    app.run(debug=True, host='0.0.0.0', port=5002)
