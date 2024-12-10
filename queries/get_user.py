import graphene
from models.user import User
from data import users

class GetUser(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.String(required=True))

    def resolve_user(self, info, id):
        user_data = next((user for user in users if user["id"] == id), None)
        if user_data:
            return User(**user_data)
        return None