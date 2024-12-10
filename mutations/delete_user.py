import graphene
from models.user import User
from data import users

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id):
        global users
        print(f"Users before deletion: {users}")
        user_data = next((user for user in users if user["id"] == id), None)
        if user_data:
            users[:] = [user for user in users if user["id"] != id]
            print(f"Deleted user: {user_data}")
            print(f"Users after deletion: {users}")
            return DeleteUser(user=User(**user_data))
        print("User not found")
        return DeleteUser(user=None)