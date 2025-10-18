import graphene
from models.user import User
from data import users

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()
        street = graphene.String()
        city = graphene.String()
        state = graphene.String()
        zip = graphene.String()
        phone = graphene.String()
        roles = graphene.List(graphene.String)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, name=None, email=None, password=None, street=None, city=None, state=None, zip=None, phone=None, roles=None):
        import re
        user_data = next((user for user in users if user["id"] == id), None)
        update_user = UpdateUser()
        if user_data:
            if name:
                user_data["name"] = name
            if email:
                # Basic email format validation
                email_regex = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
                if not re.match(email_regex, email):
                    update_user.user = None
                    return update_user
                user_data["email"] = email
            if password:
                user_data["password"] = password
            if street or city or state or zip:
                user_data["address"] = {"street": street, "city": city, "state": state, "zip": zip}
            if phone:
                user_data["phone"] = phone
            if roles:
                user_data["roles"] = roles
            update_user.user = User(**user_data)
            return update_user
        update_user.user = None
        return update_user