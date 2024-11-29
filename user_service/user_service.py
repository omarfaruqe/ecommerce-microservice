# user_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data['id']
    users[user_id] = data
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
