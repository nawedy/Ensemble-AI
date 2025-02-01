import unittest
from app import app

class ReasoningServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_reason_task(self):
        response = self.app.post('/reason', json={'prompt': 'What is the capital of France?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json)

if __name__ == '__main__':
    unittest.main()
