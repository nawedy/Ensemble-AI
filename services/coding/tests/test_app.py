import unittest
from app import app

class CodingServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_generate_code(self):
        response = self.app.post('/generate', json={'prompt': 'print("Hello, World!")'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json)

if __name__ == '__main__':
    unittest.main()
