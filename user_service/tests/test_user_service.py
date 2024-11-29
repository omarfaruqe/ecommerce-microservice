# test_user_service.py
import unittest
from user_service import app

class UserServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.app.post('/users', json={'id': '1', 'name': 'John Doe'})
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        self.app.post('/users', json={'id': '1', 'name': 'John Doe'})
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()