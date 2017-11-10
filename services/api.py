from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from resource import UserResource, RoleResource, ServiceResource
from database import db
from model import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
init_db()

api = Api(app)

api.add_resource(UserResource, '/user/<user_id>', '/user', '/user/')
api.add_resource(RoleResource, '/role/<role_id>', '/role', '/role/')
api.add_resource(ServiceResource, '/service/<service_id>', '/service', '/service/')

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def teardown_db(exception):
    if db is not None:
        db.session.close()
