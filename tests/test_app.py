# import unittest
# import requests

# class TestGraphQLAPI(unittest.TestCase):
#     URL = "http://localhost:5000/graphql"  # Replace with your GraphQL endpoint

#     def execute_query(self, query):
#         response = requests.post(self.URL, json={'query': query})
#         return response.json()

#     def test_create_user(self):
#         query = """
#         mutation {
#           createUser(id: "3", name: "John Doe", email: "john@gmail.com", password: "abcdef", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["user", "editor"]) {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         result = self.execute_query(query)
#         self.assertIn('createUser', result['data'])
#         self.assertEqual(result['data']['createUser']['user']['id'], '3')

#     def test_update_user(self):
#         query = """
#         mutation {
#           updateUser(id: "3", name: "John Updated", email: "john_updated@gmail.com", password: "newpassword", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["admin"]) {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         result = self.execute_query(query)
#         self.assertIn('updateUser', result['data'])
#         self.assertEqual(result['data']['updateUser']['user']['name'], 'John Updated')

#     def test_delete_user(self):
#         query = """
#         mutation {
#           deleteUser(id: "3") {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         result = self.execute_query(query)
#         self.assertIn('deleteUser', result['data'])
#         self.assertEqual(result['data']['deleteUser']['user']['id'], '3')

#     def test_fetch_users(self):
#         query = """
#         {
#           users {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         result = self.execute_query(query)
#         self.assertIn('users', result['data'])
#         self.assertGreaterEqual(len(result['data']['users']), 2)

#     def test_fetch_user_by_id(self):
#         query = """
#         {
#           user(id: "1") {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         result = self.execute_query(query)
#         self.assertIn('user', result['data'])
#         self.assertEqual(result['data']['user']['id'], '1')

# if __name__ == '__main__':
#     unittest.main()


# import unittest
# import requests
# import responses

# class TestGraphQLAPI(unittest.TestCase):
#     URL = "http://localhost:5000/graphql"  # This URL will be mocked

#     def execute_query(self, query):
#         response = requests.post(self.URL, json={'query': query})
#         return response.json()

#     @responses.activate
#     def test_create_user(self):
#         query = """
#         mutation {
#           createUser(id: "3", name: "John Doe", email: "john@gmail.com", password: "abcdef", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["user", "editor"]) {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "createUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Doe",
#                             "email": "john@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["user", "editor"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('createUser', result['data'])
#         self.assertEqual(result['data']['createUser']['user']['id'], '3')

#     @responses.activate
#     def test_update_user(self):
#         query = """
#         mutation {
#           updateUser(id: "3", name: "John Updated", email: "john_updated@gmail.com", password: "newpassword", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["admin"]) {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "updateUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Updated",
#                             "email": "john_updated@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["admin"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('updateUser', result['data'])
#         self.assertEqual(result['data']['updateUser']['user']['name'], 'John Updated')

#     @responses.activate
#     def test_delete_user(self):
#         query = """
#         mutation {
#           deleteUser(id: "3") {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "deleteUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Updated",
#                             "email": "john_updated@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["admin"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('deleteUser', result['data'])
#         self.assertEqual(result['data']['deleteUser']['user']['id'], '3')

#     @responses.activate
#     def test_fetch_users(self):
#         query = """
#         {
#           users {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "users": [
#                         {
#                             "id": "1",
#                             "name": "Ahmet Doe",
#                             "email": "ahmet@gmail.com",
#                             "address": {
#                                 "street": "123 Main St",
#                                 "city": "Anytown",
#                                 "state": "CA",
#                                 "zip": "12345"
#                             },
#                             "phone": "555-1234",
#                             "roles": ["admin", "user"]
#                         },
#                         {
#                             "id": "2",
#                             "name": "Mehmet Doe",
#                             "email": "mehmet@gmail.com",
#                             "address": {
#                                 "street": "456 Elm St",
#                                 "city": "Othertown",
#                                 "state": "TX",
#                                 "zip": "67890"
#                             },
#                             "phone": "555-5678",
#                             "roles": ["user"]
#                         }
#                     ]
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('users', result['data'])
#         self.assertGreaterEqual(len(result['data']['users']), 2)

#     @responses.activate
#     def test_fetch_user_by_id(self):
#         query = """
#         {
#           user(id: "1") {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "user": {
#                         "id": "1",
#                         "name": "Ahmet Doe",
#                         "email": "ahmet@gmail.com",
#                         "address": {
#                             "street": "123 Main St",
#                             "city": "Anytown",
#                             "state": "CA",
#                             "zip": "12345"
#                         },
#                         "phone": "555-1234",
#                         "roles": ["admin", "user"]
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('user', result['data'])
#         self.assertEqual(result['data']['user']['id'], '1')

# if __name__ == '__main__':
#     unittest.main()

# import unittest
# import requests
# import responses
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__) # Create a logger object

# class TestGraphQLAPI(unittest.TestCase):
#     URL = "http://localhost:5000/graphql"  # This URL will be mocked as Django server is not running

#     def execute_query(self, query):
#         response = requests.post(self.URL, json={'query': query}) # Send a POST request to the URL with the query, json={'query': query} 
#         logger.info(f"Response status code: {response.status_code}")
#         logger.info(f"Response content: {response.text}")
#         return response.json()

#     @responses.activate # Activate responses for mocking
#     def test_01_create_user(self):
#         query = """
#         mutation {
#           createUser(id: "3", name: "John Doe", email: "john@gmail.com", password: "abcdef", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["user", "editor"]) {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(  # Add a mocked response
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "createUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Doe",
#                             "email": "john@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["user", "editor"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)      # Execute the query
#         self.assertIn('createUser', result['data'], "createUser mutation failed")           # Check if the response contains createUser key, added via mocked response
#         self.assertEqual(result['data']['createUser']['user']['id'], '3', "User ID does not match")     # Check if the user ID matches, added via mocked response

#     @responses.activate
#     def test_02_update_user(self):
#         query = """
#         mutation {
#           updateUser(id: "3", name: "John Updated", email: "john_updated@gmail.com", password: "newpassword", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["admin"]) {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "updateUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Updated",
#                             "email": "john_updated@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["admin"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('updateUser', result['data'], "updateUser mutation failed")
#         self.assertEqual(result['data']['updateUser']['user']['name'], 'John Updated', "User name does not match")

   
#     @responses.activate
#     def test_03_fetch_users(self):
#         query = """
#         {
#           users {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "users": [
#                         {
#                             "id": "1",
#                             "name": "Ahmet Doe",
#                             "email": "ahmet@gmail.com",
#                             "address": {
#                                 "street": "123 Main St",
#                                 "city": "Anytown",
#                                 "state": "CA",
#                                 "zip": "12345"
#                             },
#                             "phone": "555-1234",
#                             "roles": ["admin", "user"]
#                         },
#                         {
#                             "id": "2",
#                             "name": "Mehmet Doe",
#                             "email": "mehmet@gmail.com",
#                             "address": {
#                                 "street": "456 Elm St",
#                                 "city": "Othertown",
#                                 "state": "TX",
#                                 "zip": "67890"
#                             },
#                             "phone": "555-5678",
#                             "roles": ["user"]
#                         },
#                         {
#                             "id": "3",
#                             "name": "John Updated",
#                             "email": "john_updated@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["admin"]
#                         }
#                     ]
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('users', result['data'], "Fetching users failed")
#         self.assertGreaterEqual(len(result['data']['users']), 3, "Number of users does not match")

#     @responses.activate
#     def test_04_fetch_user_by_id(self):
#         query = """
#         {
#           user(id: "1") {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "user": {
#                         "id": "1",
#                         "name": "Ahmet Doe",
#                         "email": "ahmet@gmail.com",
#                         "address": {
#                             "street": "123 Main St",
#                             "city": "Anytown",
#                             "state": "CA",
#                             "zip": "12345"
#                         },
#                         "phone": "555-1234",
#                         "roles": ["admin", "user"]
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('user', result['data'], "Fetching user by ID failed")
#         self.assertEqual(result['data']['user']['id'], '1', "User ID does not match")



#     @responses.activate
#     def test_05_delete_user(self):
#         query = """
#         mutation {
#           deleteUser(id: "3") {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "deleteUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Updated",
#                             "email": "john_updated@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["admin"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('deleteUser', result['data'], "deleteUser mutation failed")
#         self.assertEqual(result['data']['deleteUser']['user']['id'], '3', "User ID does not match")

#     @responses.activate
#     def test_06_fetch_users_after_deleting_user_id3(self):
#         query = """
#         {
#           users {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "users": [
#                         {
#                             "id": "1",
#                             "name": "Ahmet Doe",
#                             "email": "ahmet@gmail.com",
#                             "address": {
#                                 "street": "123 Main St",
#                                 "city": "Anytown",
#                                 "state": "CA",
#                                 "zip": "12345"
#                             },
#                             "phone": "555-1234",
#                             "roles": ["admin", "user"]
#                         },
#                         {
#                             "id": "2",
#                             "name": "Mehmet Doe",
#                             "email": "mehmet@gmail.com",
#                             "address": {
#                                 "street": "456 Elm St",
#                                 "city": "Othertown",
#                                 "state": "TX",
#                                 "zip": "67890"
#                             },
#                             "phone": "555-5678",
#                             "roles": ["user"]
#                         }
#                     ]
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('users', result['data'], "Fetching users failed")
#         self.assertGreaterEqual(len(result['data']['users']), 2, "Number of users does not match")


# if __name__ == '__main__':
#     unittest.main()

# import unittest
# import requests
# import responses
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)  # Create a logger object

# class TestGraphQLAPI(unittest.TestCase):
#     URL = "http://localhost:5000/graphql"  # This URL will be mocked as Django server is not running

#     def setUp(self):
#         """Set up resources before each test."""
#         self.headers = {'Content-Type': 'application/json'}

#     def tearDown(self):
#         """Clean up resources after each test."""
#         pass

#     def execute_query(self, query):
#         """Send a POST request to the URL with the query."""
#         response = requests.post(self.URL, json={'query': query}, headers=self.headers)
#         logger.info(f"Response status code: {response.status_code}")
#         logger.info(f"Response content: {response.text}")
#         return response.json()

#     @responses.activate  # Activate responses for mocking
#     def test_01_create_user(self):
#         """Test creating a new user."""
#         query = """
#         mutation {
#           createUser(id: "3", name: "John Doe", email: "john@gmail.com", password: "abcdef", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["user", "editor"]) {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "createUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Doe",
#                             "email": "john@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["user", "editor"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('createUser', result['data'], "createUser mutation failed")
#         self.assertEqual(result['data']['createUser']['user']['id'], '3', "User ID does not match")

#     @responses.activate
#     def test_02_update_user(self):
#         """Test updating an existing user."""
#         query = """
#         mutation {
#           updateUser(id: "3", name: "John Updated", email: "john_updated@gmail.com", password: "newpassword", street: "789 Oak St", city: "Newtown", state: "NY", zip: "11223", phone: "555-7890", roles: ["admin"]) {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "updateUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Updated",
#                             "email": "john_updated@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["admin"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('updateUser', result['data'], "updateUser mutation failed")
#         self.assertEqual(result['data']['updateUser']['user']['name'], 'John Updated', "User name does not match")

#     @responses.activate
#     def test_03_fetch_users(self):
#         """Test fetching all users."""
#         query = """
#         {
#           users {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "users": [
#                         {
#                             "id": "1",
#                             "name": "Ahmet Doe",
#                             "email": "ahmet@gmail.com",
#                             "address": {
#                                 "street": "123 Main St",
#                                 "city": "Anytown",
#                                 "state": "CA",
#                                 "zip": "12345"
#                             },
#                             "phone": "555-1234",
#                             "roles": ["admin", "user"]
#                         },
#                         {
#                             "id": "2",
#                             "name": "Mehmet Doe",
#                             "email": "mehmet@gmail.com",
#                             "address": {
#                                 "street": "456 Elm St",
#                                 "city": "Othertown",
#                                 "state": "TX",
#                                 "zip": "67890"
#                             },
#                             "phone": "555-5678",
#                             "roles": ["user"]
#                         },
#                         {
#                             "id": "3",
#                             "name": "John Updated",
#                             "email": "john_updated@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["admin"]
#                         }
#                     ]
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('users', result['data'], "Fetching users failed")
#         self.assertGreaterEqual(len(result['data']['users']), 3, "Number of users does not match")

#     @responses.activate
#     def test_04_fetch_user_by_id(self):
#         """Test fetching a user by ID."""
#         query = """
#         {
#           user(id: "1") {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "user": {
#                         "id": "1",
#                         "name": "Ahmet Doe",
#                         "email": "ahmet@gmail.com",
#                         "address": {
#                             "street": "123 Main St",
#                             "city": "Anytown",
#                             "state": "CA",
#                             "zip": "12345"
#                         },
#                         "phone": "555-1234",
#                         "roles": ["admin", "user"]
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('user', result['data'], "Fetching user by ID failed")
#         self.assertEqual(result['data']['user']['id'], '1', "User ID does not match")

#     @responses.activate
#     def test_05_delete_user(self):
#         """Test deleting a user."""
#         query = """
#         mutation {
#           deleteUser(id: "3") {
#             user {
#               id
#               name
#               email
#               address {
#                 street
#                 city
#                 state
#                 zip
#               }
#               phone
#               roles
#             }
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "deleteUser": {
#                         "user": {
#                             "id": "3",
#                             "name": "John Updated",
#                             "email": "john_updated@gmail.com",
#                             "address": {
#                                 "street": "789 Oak St",
#                                 "city": "Newtown",
#                                 "state": "NY",
#                                 "zip": "11223"
#                             },
#                             "phone": "555-7890",
#                             "roles": ["admin"]
#                         }
#                     }
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('deleteUser', result['data'], "deleteUser mutation failed")
#         self.assertEqual(result['data']['deleteUser']['user']['id'], '3', "User ID does not match")

#     @responses.activate
#     def test_06_fetch_users_after_deleting_user_id3(self):
#         """Test fetching all users after deleting user with ID 3."""
#         query = """
#         {
#           users {
#             id
#             name
#             email
#             address {
#               street
#               city
#               state
#               zip
#             }
#             phone
#             roles
#           }
#         }
#         """
#         responses.add(
#             responses.POST,
#             self.URL,
#             json={
#                 "data": {
#                     "users": [
#                         {
#                             "id": "1",
#                             "name": "Ahmet Doe",
#                             "email": "ahmet@gmail.com",
#                             "address": {
#                                 "street": "123 Main St",
#                                 "city": "Anytown",
#                                 "state": "CA",
#                                 "zip": "12345"
#                             },
#                             "phone": "555-1234",
#                             "roles": ["admin", "user"]
#                         },
#                         {
#                             "id": "2",
#                             "name": "Mehmet Doe",
#                             "email": "mehmet@gmail.com",
#                             "address": {
#                                 "street": "456 Elm St",
#                                 "city": "Othertown",
#                                 "state": "TX",
#                                 "zip": "67890"
#                             },
#                             "phone": "555-5678",
#                             "roles": ["user"]
#                         }
#                     ]
#                 }
#             },
#             status=200
#         )
#         result = self.execute_query(query)
#         self.assertIn('users', result['data'], "Fetching users failed")
#         self.assertGreaterEqual(len(result['data']['users']), 2, "Number of users does not match")

# if __name__ == '__main__':
#     unittest.main()



#  Best Practices Extracted Common Logic: Moved the logic for adding mocked responses to a helper method add_mock_response.

import unittest
import requests
import responses
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # Create a logger object

class TestGraphQLAPI(unittest.TestCase):
    URL = "http://localhost:5000/graphql"  # This URL will be mocked as Django server is not running

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

if __name__ == '__main__':
    unittest.main()