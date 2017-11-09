from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from resource import UserResource

app = Flask(__name__)
api = Api(app)

USERS = {
    '1': { 'id': '1', 'user': 'nedstark@doe.john'},
    '2': { 'id': '2', 'user': 'kaimelannister@doe.john'},
    '3': { 'id': '3', 'user': 'cerseilannister@doe.john'},
    '4': { 'id': '4', 'user': 'daenerystargaryen@doe.john'},
    '5': { 'id': '5', 'user': 'littlefinger@doe.john'},
    '6': { 'id': '6', 'user': 'jonsnow@doe.john'}
}

def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="No such user {}".format(user_id))


api.add_resource(UserResource, '/user/<user_id>', '/user', '/user/')

if __name__ == '__main__':
    app.run(debug=True)
