# order_service.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

orders = {}

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data['user_id']
    product_id = data['product_id']

    # Validate user
    user_response = requests.get(f'http://user_service:5001/users/{user_id}')
    if user_response.status_code != 200:
        return jsonify({'message': 'User not found'}), 404

    # Validate product
    product_response = requests.get(f'http://product_service:5002/products/{product_id}')
    if product_response.status_code != 200:
        return jsonify({'message': 'Product not found'}), 404

    order_id = len(orders) + 1
    orders[order_id] = data
    return jsonify({'message': 'Order created successfully', 'order_id': order_id}), 201

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        return jsonify(order), 200
    return jsonify({'message': 'Order not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
