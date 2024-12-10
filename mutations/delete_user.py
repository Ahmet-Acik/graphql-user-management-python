import graphene
from models.user import User
from data import users

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id):
        global users
        user_data = next((user for user in users if user["id"] == id), None)
        if user_data:
            users = [user for user in users if user["id"] != id]
            return DeleteUser(user=User(**user_data))
        return DeleteUser(user=None)