import graphene
from models.user import User
from data import users

class GetUsers(graphene.ObjectType):
    get_users = graphene.List(User)

    def resolve_get_users(self, info):
        return [User(**user_data) for user_data in users]