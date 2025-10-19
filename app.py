
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

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class MyQuery(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.ID(required=True))
    users = graphene.List(User)

    def resolve_user(self, info, id):
        return next((user for user in users if user["id"] == id), None)

    def resolve_users(self, info):
        return users

schema = graphene.Schema(query=MyQuery, mutation=MyMutations)


app = Flask(__name__)
CORS(app)

# SQLAlchemy setup
engine = create_engine('sqlite:///users.db')
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
    app.run(debug=True, port=5050)