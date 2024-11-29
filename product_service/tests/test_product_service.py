# product_service/tests/test_product_service.py
import unittest
from product_service import app

class ProductServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_product(self):
        response = self.app.post('/products', json={'id': '1', 'name': 'Laptop'})
        self.assertEqual(response.status_code, 201)

    def test_get_product(self):
        self.app.post('/products', json={'id': '1', 'name': 'Laptop'})
        response = self.app.get('/products/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
