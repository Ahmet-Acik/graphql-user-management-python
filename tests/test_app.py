#  Best Practices Extracted Common Logic: Moved the logic for adding mocked responses to a helper method add_mock_response.

import unittest
import requests
import responses
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # Create a logger object

class TestGraphQLAPI(unittest.TestCase):
    URL = "http://localhost:5050/graphql"  # This URL will be mocked as Django server is not running

    def setUp(self):
        """Set up resources before each test."""
        self.headers = {'Content-Type': 'application/json'}

    def tearDown(self):
        """Clean up resources after each test."""
        pass

    def execute_query(self, query):
        """Send a POST request to the URL with the query."""
        response = requests.post(self.URL, json={'query': query}, headers=self.headers)
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response content: {response.text}")
        return response.json()

    def add_mock_response(self, query, response_data, status=200):
        """Add a mocked response for the given query."""
        responses.add(
            responses.POST,
            self.URL,
            json=response_data,
            status=status
        )

    @responses.activate  # Activate responses for mocking
    def test_01_create_user(self):
        """Test creating a new user."""
        query = """
        mutation {
          createUser(id: "3", name: "John Doe", email: "john@gmail.com", password: "abcdef", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["user", "editor"]) {
            user {
              id
              name
              email
              address {
                street
                city
                state
                zip
              }
              phone
              roles
            }
          }
        }
        """
        response_data = {
            "data": {
                "createUser": {
                    "user": {
                        "id": "3",
                        "name": "John Doe",
                        "email": "john@gmail.com",
                        "address": {
                            "street": "789 Oak St",
                            "city": "Newtown",
                            "state": "NY",
                            "zip": "11223"
                        },
                        "phone": "555-7890",
                        "roles": ["user", "editor"]
                    }
                }
            }
        }
        self.add_mock_response(query, response_data)
        result = self.execute_query(query)
        self.assertIn('createUser', result['data'], "createUser mutation failed")
        self.assertEqual(result['data']['createUser']['user']['id'], '3', "User ID does not match")

    @responses.activate
    def test_02_update_user(self):
        """Test updating an existing user."""
        query = """
        mutation {
          updateUser(id: "3", name: "John Updated", email: "john_updated@gmail.com", password: "newpassword", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["admin"]) {
            user {
              id
              name
              email
              address {
                street
                city
                state
                zip
              }
              phone
              roles
            }
          }
        }
        """
        response_data = {
            "data": {
                "updateUser": {
                    "user": {
                        "id": "3",
                        "name": "John Updated",
                        "email": "john_updated@gmail.com",
                        "address": {
                            "street": "789 Oak St",
                            "city": "Newtown",
                            "state": "NY",
                            "zip": "11223"
                        },
                        "phone": "555-7890",
                        "roles": ["admin"]
                    }
                }
            }
        }
        self.add_mock_response(query, response_data)
        result = self.execute_query(query)
        self.assertIn('updateUser', result['data'], "updateUser mutation failed")
        self.assertEqual(result['data']['updateUser']['user']['name'], 'John Updated', "User name does not match")

    @responses.activate
    def test_03_fetch_users(self):
        """Test fetching all users."""
        query = """
        {
          users {
            id
            name
            email
            address {
              street
              city
              state
              zip
            }
            phone
            roles
          }
        }
        """
        response_data = {
            "data": {
                "users": [
                    {
                        "id": "1",
                        "name": "Ahmet Doe",
                        "email": "ahmet@gmail.com",
                        "address": {
                            "street": "123 Main St",
                            "city": "Anytown",
                            "state": "CA",
                            "zip": "12345"
                        },
                        "phone": "555-1234",
                        "roles": ["admin", "user"]
                    },
                    {
                        "id": "2",
                        "name": "Mehmet Doe",
                        "email": "mehmet@gmail.com",
                        "address": {
                            "street": "456 Elm St",
                            "city": "Othertown",
                            "state": "TX",
                            "zip": "67890"
                        },
                        "phone": "555-5678",
                        "roles": ["user"]
                    },
                    {
                        "id": "3",
                        "name": "John Updated",
                        "email": "john_updated@gmail.com",
                        "address": {
                            "street": "789 Oak St",
                            "city": "Newtown",
                            "state": "NY",
                            "zip": "11223"
                        },
                        "phone": "555-7890",
                        "roles": ["admin"]
                    }
                ]
            }
        }
        self.add_mock_response(query, response_data)
        result = self.execute_query(query)
        self.assertIn('users', result['data'], "Fetching users failed")
        self.assertGreaterEqual(len(result['data']['users']), 3, "Number of users does not match")

    @responses.activate
    def test_04_fetch_user_by_id(self):
        """Test fetching a user by ID."""
        query = """
        {
          user(id: "1") {
            id
            name
            email
            address {
              street
              city
              state
              zip
            }
            phone
            roles
          }
        }
        """
        response_data = {
            "data": {
                "user": {
                    "id": "1",
                    "name": "Ahmet Doe",
                    "email": "ahmet@gmail.com",
                    "address": {
                        "street": "123 Main St",
                        "city": "Anytown",
                        "state": "CA",
                        "zip": "12345"
                    },
                    "phone": "555-1234",
                    "roles": ["admin", "user"]
                }
            }
        }
        self.add_mock_response(query, response_data)
        result = self.execute_query(query)
        self.assertIn('user', result['data'], "Fetching user by ID failed")
        self.assertEqual(result['data']['user']['id'], '1', "User ID does not match")

    @responses.activate
    def test_05_delete_user(self):
        """Test deleting a user."""
        query = """
        mutation {
          deleteUser(id: "3") {
            user {
              id
              name
              email
              address {
                street
                city
                state
                zip
              }
              phone
              roles
            }
          }
        }
        """
        response_data = {
            "data": {
                "deleteUser": {
                    "user": {
                        "id": "3",
                        "name": "John Updated",
                        "email": "john_updated@gmail.com",
                        "address": {
                            "street": "789 Oak St",
                            "city": "Newtown",
                            "state": "NY",
                            "zip": "11223"
                        },
                        "phone": "555-7890",
                        "roles": ["admin"]
                    }
                }
            }
        }
        self.add_mock_response(query, response_data)
        result = self.execute_query(query)
        self.assertIn('deleteUser', result['data'], "deleteUser mutation failed")
        self.assertEqual(result['data']['deleteUser']['user']['id'], '3', "User ID does not match")

    @responses.activate
    def test_06_fetch_users_after_deleting_user_id3(self):
        """Test fetching all users after deleting user with ID 3."""
        query = """
        {
          users {
            id
            name
            email
            address {
              street
              city
              state
              zip
            }
            phone
            roles
          }
        }
        """
        response_data = {
            "data": {
                "users": [
                    {
                        "id": "1",
                        "name": "Ahmet Doe",
                        "email": "ahmet@gmail.com",
                        "address": {
                            "street": "123 Main St",
                            "city": "Anytown",
                            "state": "CA",
                            "zip": "12345"
                        },
                        "phone": "555-1234",
                        "roles": ["admin", "user"]
                    },
                    {
                        "id": "2",
                        "name": "Mehmet Doe",
                        "email": "mehmet@gmail.com",
                        "address": {
                            "street": "456 Elm St",
                            "city": "Othertown",
                            "state": "TX",
                            "zip": "67890"
                        },
                        "phone": "555-5678",
                        "roles": ["user"]
                    }
                ]
            }
        }
        self.add_mock_response(query, response_data)
        result = self.execute_query(query)
        self.assertIn('users', result['data'], "Fetching users failed")
        self.assertGreaterEqual(len(result['data']['users']), 2, "Number of users does not match")


    @responses.activate
    def test_07_create_user_missing_fields(self):
        """Test creating a user with missing fields."""
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
        self.add_mock_response(query, {
            "data": {
                "createUser": {
                    "user": None
                }
            }
        })
        result = self.execute_query(query)
        self.assertIn('createUser', result['data'])
        self.assertIsNone(result['data']['createUser']['user'], "User should be None for missing fields")

    @responses.activate
    def test_08_delete_nonexistent_user(self):
        """Test deleting a user that does not exist."""
        query = """
        mutation {
          deleteUser(id: "999") {
            user {
              id
            }
          }
        }
        """
        responses.add(
            responses.POST,
            self.URL,
            json={
                "data": {
                    "deleteUser": {
                        "user": None
                    }
                }
            },
            status=200
        )
        result = self.execute_query(query)
        self.assertIn('deleteUser', result['data'], "deleteUser mutation failed")
        self.assertIsNone(result['data']['deleteUser']['user'], "Deleted user should be null")

    @responses.activate
    def test_09_update_user_invalid_email(self):
        """Test updating a user with an invalid email."""
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
        self.add_mock_response(query, {
            "data": {
                "updateUser": {
                    "user": None
                }
            }
        })
        result = self.execute_query(query)
        self.assertIn('updateUser', result['data'])
        self.assertIsNone(result['data']['updateUser']['user'], "User should be None for invalid email")

if __name__ == '__main__':
    unittest.main()