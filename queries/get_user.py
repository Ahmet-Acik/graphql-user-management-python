import graphene
from models.user import User
from data import users

class GetUser(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.ID(required=True))

    def resolve_user(self, info, id):
        return next((user for user in users if user["id"] == id), None)