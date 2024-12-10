import graphene
from models.address import Address

class User(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    address = graphene.Field(Address)
    phone = graphene.String()
    roles = graphene.List(graphene.String)
    
    @staticmethod
    def get(id):
        # Fetch the user by id from the database
        pass

    def delete(self):
        # Delete the user from the database
        pass