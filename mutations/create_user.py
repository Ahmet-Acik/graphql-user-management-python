import graphene
from models.user import User
from models.user_model import UserModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///users.db')
SessionLocal = sessionmaker(bind=engine)

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
        db = SessionLocal()
        # Convert roles list to comma-separated string
        roles_str = ','.join(roles) if roles else ''
        user_model = UserModel(id=id, name=name, email=email, password=password, phone=phone, roles=roles_str)
        db.add(user_model)
        db.commit()
        db.refresh(user_model)
        address = {"street": street, "city": city, "state": state, "zip": zip}
        user_data = {"id": str(user_model.id), "name": user_model.name, "email": user_model.email, "password": user_model.password, "address": address, "phone": user_model.phone, "roles": roles}
        create_user = CreateUser()
        create_user.user = User(**user_data)
        db.close()
        return create_user