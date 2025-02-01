import unittest
from app import app

class MathServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_solve_equation(self):
        response = self.app.post('/solve', json={'equation': '2+2'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json)

if __name__ == '__main__':
    unittest.main()
