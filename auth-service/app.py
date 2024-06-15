import os
import debugpy
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app)

# In-memory database for demonstration purposes
users = {}

@app.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'User already exists!'}), 400

    users[username] = generate_password_hash(password)
    return jsonify({'message': 'User created successfully!'}), 201

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/log/flask.log', level=logging.DEBUG)  # 로그 파일 설정
    debugpy.listen(("0.0.0.0", 5680))
    debugpy.wait_for_client()
    app.run(debug=True, host='0.0.0.0', port=5001)