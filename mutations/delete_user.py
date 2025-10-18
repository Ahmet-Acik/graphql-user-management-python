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
        delete_user = DeleteUser()
        if user_data:
            users[:] = [user for user in users if user["id"] != id]
            print(f"Deleted user: {user_data}")
            print(f"Users after deletion: {users}")
            delete_user.user = User(**user_data)
            return delete_user
        print("User not found")
        delete_user.user = None
        return delete_user