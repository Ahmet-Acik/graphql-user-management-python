import graphene
from models.user import User
from data import users

class GetUsers(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return users