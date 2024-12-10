import graphene
from address import Address

class User(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    address = graphene.Field(Address)
    phone = graphene.String()
    roles = graphene.List(graphene.String)