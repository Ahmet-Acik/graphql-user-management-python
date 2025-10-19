import graphene
from models.user import User
from models.user_model import UserModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///users.db')
SessionLocal = sessionmaker(bind=engine)

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
        db = SessionLocal()
        user_model = db.query(UserModel).filter_by(id=id).first()
        update_user = UpdateUser()
        if user_model:
            if name:
                user_model.name = name
            if email:
                # Basic email format validation
                email_regex = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
                if not re.match(email_regex, email):
                    update_user.user = None
                    db.close()
                    return update_user
                user_model.email = email
            if password:
                user_model.password = password
            if phone:
                user_model.phone = phone
            if roles:
                user_model.roles = ','.join(roles)
            db.commit()
            address = {"street": street, "city": city, "state": state, "zip": zip}
            user_data = {"id": str(user_model.id), "name": user_model.name, "email": user_model.email, "password": user_model.password, "address": address, "phone": user_model.phone, "roles": roles}
            update_user.user = User(**user_data)
            db.close()
            return update_user
        update_user.user = None
        db.close()
        return update_user