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

    def __init__(self, user=None):
        super().__init__()
        self.user = user

    def mutate(self, info, id, name, email, password, street=None, city=None, state=None, zip=None, phone=None, roles=None):
        # Basic validation: reject empty name/email/password
        if not name or not email or not password:
            create_user = CreateUser()
            create_user.user = None
            return create_user
        address = {"street": street, "city": city, "state": state, "zip": zip}
        user_data = {"id": id, "name": name, "email": email, "password": password, "address": address, "phone": phone, "roles": roles}
        users.append(user_data)
        create_user = CreateUser()
        create_user.user = User(**user_data)
        return create_user