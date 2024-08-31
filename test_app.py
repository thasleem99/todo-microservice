import unittest
from app.app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'task': 'Write unit tests'}])  # Update expected output here

if __name__ == '__main__':
    unittest.main()
