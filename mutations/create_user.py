import graphene
from models.user import User
from data import users

class CreateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        street = graphene.String()
        city = graphene.String()
        state = graphene.String()
        zip = graphene.String()
        phone = graphene.String()
        roles = graphene.List(graphene.String)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, name, email, password, street=None, city=None, state=None, zip=None, phone=None, roles=None):
        address = {"street": street, "city": city, "state": state, "zip": zip}
        user_data = {"id": id, "name": name, "email": email, "password": password, "address": address, "phone": phone, "roles": roles}
        users.append(user_data)
        return CreateUser(user=User(**user_data))