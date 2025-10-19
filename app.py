
import graphene
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import Base, UserModel
from mutations.create_user import CreateUser
from mutations.update_user import UpdateUser
from mutations.delete_user import DeleteUser
from models.user import User
from data import users
import os

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class MyQuery(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.ID(required=True))
    users = graphene.List(User)

    def resolve_user(self, info, id):
        db = SessionLocal()
        user_model = db.query(UserModel).filter_by(id=id).first()
        db.close()
        if user_model:
            user_data = {"id": str(user_model.id), "name": user_model.name, "email": user_model.email, "password": user_model.password, "address": None, "phone": user_model.phone, "roles": user_model.roles.split(',') if user_model.roles else []}
            return User(**user_data)
        return None

    def resolve_users(self, info):
        db = SessionLocal()
        user_models = db.query(UserModel).all()
        db.close()
        users_list = []
        for user_model in user_models:
            user_data = {"id": str(user_model.id), "name": user_model.name, "email": user_model.email, "password": user_model.password, "address": None, "phone": user_model.phone, "roles": user_model.roles.split(',') if user_model.roles else []}
            users_list.append(User(**user_data))
        return users_list

schema = graphene.Schema(query=MyQuery, mutation=MyMutations)


app = Flask(__name__)
CORS(app)

# SQLAlchemy setup
db_url = 'sqlite:///users.db'
if os.environ.get('TESTING') == '1':
    db_url = 'sqlite:///test.db'
engine = create_engine(db_url)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    result = schema.execute(data.get("query"), variables=data.get("variables"))
    response = {}
    if result.errors:
        response["errors"] = [str(e) for e in result.errors]
    if result.data:
        response["data"] = result.data
    return jsonify(response)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    playground_html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>GraphQL Playground</title>
      <link rel="stylesheet" href="https://unpkg.com/graphql-playground-react/build/static/css/index.css" />
      <link rel="shortcut icon" href="https://graphql.org/img/favicon.png" />
      <script src="https://unpkg.com/graphql-playground-react/build/static/js/middleware.js"></script>
    </head>
    <body>
      <div id="root"></div>
      <script>window.addEventListener('load', function (event) { GraphQLPlayground.init(document.getElementById('root'), { endpoint: '/graphql' }) })</script>
    </body>
    </html>
    """
    return playground_html

if __name__ == "__main__":
    app.run(debug=True, port=5051)
    