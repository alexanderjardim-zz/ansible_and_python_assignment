from flask_restful import reqparse, abort, Resource

parser = reqparse.RequestParser()
parser.add_argument('user')
parser.add_argument('id')

class UserResource(Resource):

    USERS = {
        '1': { 'id': '1', 'user': 'nedstark@doe.john'},
        '2': { 'id': '2', 'user': 'kaimelannister@doe.john'},
        '3': { 'id': '3', 'user': 'cerseilannister@doe.john'},
        '4': { 'id': '4', 'user': 'daenerystargaryen@doe.john'},
        '5': { 'id': '5', 'user': 'littlefinger@doe.john'},
        '6': { 'id': '6', 'user': 'jonsnow@doe.john'}
    }

    def abort_if_user_doesnt_exist(user_id):
        if user_id not in self.USERS:
            abort(404, message="No such user {}".format(user_id))

    def get(self, user_id=None):
        if user_id is None :
            return self.USERS
        self.abort_if_user_doesnt_exist(user_id)
        return self.USERS[user_id]

    def delete(self, user_id):
        self.abort_if_user_doesnt_exist(user_id)
        del self.USERS[user_id]
        return '', 204

    def post(self):
        args = parser.parse_args()
        if args['id'] in self.USERS:
            abort(400, message="User already exists")
        user = { 'id': args['id'], 'user': args['user']}
        self.USERS[args['id']] = user
        return user, 201

    def put(self, user_id):
        if user_id not in USERS:
            abort(400, message="There is no user to update")
        args = parser.parse_args()
        user = { 'id': user_id, 'user': args['user']}
        self.USERS[user_id] = user
        return user, 201
