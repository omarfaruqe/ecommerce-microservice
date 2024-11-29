# product_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)

products = {}

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = data['id']
    products[product_id] = data
    return jsonify({'message': 'Product created successfully'}), 201

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({'message': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
