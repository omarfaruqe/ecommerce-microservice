# order_service/tests/test_order_service.py
import unittest
from order_service import app
from unittest.mock import patch

class OrderServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('order_service.requests.get')
    def test_create_order(self, mock_get):
        # Mock the responses for user and product services
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200),  # User service response
            unittest.mock.Mock(status_code=200)   # Product service response
        ]

        response = self.app.post('/orders', json={'user_id': '1', 'product_id': '1'})
        self.assertEqual(response.status_code, 201)

    @patch('order_service.requests.get')
    def test_get_order(self, mock_get):
        # Mock the responses for user and product services
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200),  # User service response
            unittest.mock.Mock(status_code=200)   # Product service response
        ]

        self.app.post('/orders', json={'user_id': '1', 'product_id': '1'})
        response = self.app.get('/orders/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
