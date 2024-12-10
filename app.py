import graphene
from mutations.create_user import CreateUser
from mutations.update_user import UpdateUser
from mutations.delete_user import DeleteUser
from queries.get_user import GetUser
from queries.get_users import GetUsers

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class MyQuery(GetUser, GetUsers, graphene.ObjectType):
    pass

schema = graphene.Schema(query=MyQuery, mutation=MyMutations)

def execute_and_print(label, query):
    print(f"\n{label}")
    result = schema.execute(query)
    if result.errors:
        print("Errors:", result.errors)
    else:
        print(result.data)

# Create a new user with a different id
execute_and_print(
    "Creating a new user with id 3:",
    """
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
)

# Update the newly created user
execute_and_print(
    "Updating the user with id 3:",
    """
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
)

# Fetch all users before deleting the updated user
execute_and_print(
    "Fetching all users before deleting the user with id 3:",
    """
{
  getUsers {
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
)

# Delete the newly created user
execute_and_print(
    "Deleting the user with id 3:",
    """
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
)

# Fetch all users after deleting the updated user
execute_and_print(
    "Fetching all users after deleting the user with id 3:",
    """
{
  getUsers {
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
)

# Fetch a specific user by id
execute_and_print(
    "Fetching the user with id 1:",
    """
{
  getUser(id: "1") {
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
)

# Fetch a specific user by id
execute_and_print(
    "Fetching the user with id 1 using user query:",
    """
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
)