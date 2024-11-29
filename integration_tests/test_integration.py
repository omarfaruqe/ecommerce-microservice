# test_integration.py
import unittest
import requests

class IntegrationTestCase(unittest.TestCase):
    def test_create_order(self):
        # Create user
        user_response = requests.post('http://localhost:5001/users', json={'id': '1', 'name': 'John Doe'})
        self.assertEqual(user_response.status_code, 201)

        # Create product
        product_response = requests.post('http://localhost:5002/products', json={'id': '1', 'name': 'Laptop'})
        self.assertEqual(product_response.status_code, 201)

        # Create order
        order_response = requests.post('http://localhost:5003/orders', json={'user_id': '1', 'product_id': '1'})
        self.assertEqual(order_response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
