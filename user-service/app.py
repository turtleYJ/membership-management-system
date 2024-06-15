from flask import Flask

app = Flask(__name__)

@app.route('/user/', methods=['GET'])
def user():
    return "User Service is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)