import unittest
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestGraphQLAPIIntegration(unittest.TestCase):
    URL = "http://localhost:5000/graphql"

    def setUp(self):
        self.headers = {'Content-Type': 'application/json'}

    def execute_query(self, query):
        response = requests.post(self.URL, json={'query': query}, headers=self.headers)
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response content: {response.text}")
        return response.json()

    def test_create_user_missing_fields(self):
        query = """
        mutation {
          createUser(id: "4", name: "", email: "", password: "") {
            user {
              id
              name
              email
            }
          }
        }
        """
        result = self.execute_query(query)
        self.assertIn('createUser', result['data'])
        self.assertIsNone(result['data']['createUser']['user'], "User should be None for missing fields")

    def test_delete_nonexistent_user(self):
        query = """
        mutation {
          deleteUser(id: "999") {
            user {
              id
            }
          }
        }
        """
        result = self.execute_query(query)
        self.assertIn('deleteUser', result['data'])
        self.assertIsNone(result['data']['deleteUser']['user'])

    def test_update_user_invalid_email(self):
        query = """
        mutation {
          updateUser(id: "1", email: "not-an-email") {
            user {
              id
              email
            }
          }
        }
        """
        result = self.execute_query(query)
        self.assertIn('updateUser', result['data'])
        self.assertIsNone(result['data']['updateUser']['user'], "User should be None for invalid email")

if __name__ == '__main__':
    unittest.main()
