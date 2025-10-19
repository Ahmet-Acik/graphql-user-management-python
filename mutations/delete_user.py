import graphene
from models.user import User
from models.user_model import UserModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///users.db')
SessionLocal = sessionmaker(bind=engine)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id):
        db = SessionLocal()
        user_model = db.query(UserModel).filter_by(id=id).first()
        delete_user = DeleteUser()
        if user_model:
            user_data = {"id": str(user_model.id), "name": user_model.name, "email": user_model.email, "password": user_model.password, "address": None, "phone": user_model.phone, "roles": user_model.roles.split(',') if user_model.roles else []}
            db.delete(user_model)
            db.commit()
            delete_user.user = User(**user_data)
            db.close()
            return delete_user
        delete_user.user = None
        db.close()
        return delete_user