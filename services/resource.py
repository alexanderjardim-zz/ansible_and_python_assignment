from flask_restful import reqparse, abort, Resource, fields, marshal
from model import User, Role, Service, Tag

parser = reqparse.RequestParser()
parser.add_argument('user')
parser.add_argument('id')

role_fields = {
    'id': fields.String,
    'name': fields.String
}

user_fields = {
    'login': fields.String,
    'id': fields.String,
    'role': fields.Nested(role_fields)
}

service_fields = {
    'id': fields.String,
    'name': fields.String,
    'region': fields.String,
    'size': fields.String,
    'image': fields.String,
    'ssh_keys': fields.String,
    'backups': fields.Boolean,
    'ipv6': fields.Boolean,
    'user_data': fields.String,
    'private_networking': fields.String,
    'volumes': fields.String,
    'owner': fields.Nested(user_fields)
}


class RoleResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str )
        super(RoleResource, self).__init__()

    def get(self, role_id=None):
        if role_id is None :
            roles = Role.query.all()
            return { 'roles': [marshal(r, role_fields) for r in roles] }
        else:
            return { 'role': marshal(Role.query.get_or_404(role_id), role_fields) }

    def post(self):
        args = self.parser.parse_args()
        r = Role.query.filter_by(name=args['name']).first()
        if r is not None:
            abort(400, message="Role already exists")
        else:
            r = Role(name=args['name'])
            r.insert()
        return {'role': marshal(r, role_fields)}, 201



class ServiceResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('owner_login', type=str)
        self.parser.add_argument('owner_id', type=str)
        self.parser.add_argument('search', type=str)
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('region', type=str)
        self.parser.add_argument('size', type=str)
        self.parser.add_argument('image', type=str)
        self.parser.add_argument('ssh_keys', type=str)
        self.parser.add_argument('backups', type=bool)
        self.parser.add_argument('ipv6', type=bool)
        self.parser.add_argument('user_data', type=str)
        self.parser.add_argument('private_networking', type=str)
        self.parser.add_argument('volumes', type=str)
        #self.parser.add_argument('tags', type=arr)
        super(ServiceResource, self).__init__()

    def get(self, service_id=None):
        args = self.parser.parse_args()
        if args['search'] is not None:
            services = Service.query.filter_by(name=args['search']).all()
            return { 'services': [marshal(s, service_fields) for s in services] }
        if service_id is None :
            services = Service.query.all()
            return { 'services': [marshal(s, service_fields) for s in services] }
        else:
            return { 'service': marshal(Service.query.get_or_404(service_id), service_fields) }

    def post(self):
        args = self.parser.parse_args()
        s = Service().query.filter_by(name=args['name']).first()
        if s is not None:
            abort(400, message="Service already exists")
        else:
            u = User.query.filter_by(login=args['owner_login']).first()
            s = Service(name=args['name'],
                        region=args['region'],
                        size=args['size'],
                        image=args['image'],
                        ssh_keys=args['ssh_keys'],
                        backups=args['backups'],
                        ipv6=args['ipv6'],
                        user_data=args['user_data'],
                        private_networking=args['private_networking'],
                        volumes=args['volumes'],
                        owner=u)
            s.insert()
            return {'service': marshal(s, service_fields)}, 201

    def delete(self, service_id):
        s = Service().query.get_or_404(service_id)
        if s is not None:
            s.remove()
            return '', 204

    def put(self, service_id):
        args = self.parser.parse_args()
        s = Service().query.get_or_404(service_id)
        if args['owner_id'] is not None:
            u = User.query.get(args['owner_id'])
            s.owner=u
        elif args['owner_login'] is not None:
            u = User.query.filter_by(login=args['owner_login']).first()
            s.owner=u
        else:
            return 'You are not updating anything', 400
        return {'service': marshal(s, service_fields)}, 201

class UserResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('login', type=str )
        super(UserResource, self).__init__()

    def delete(self, user_id):
        u = User.query.get_or_404(user_id)
        u.remove()
        return '', 204

    def get(self, user_id=None):
        if user_id is None :
            users = User.query.all()
            return { 'users': [marshal(u, user_fields) for u in users] }
        else:
            return { 'user': marshal(User.query.get_or_404(user_id), user_fields) }

    def post(self):
        args = self.parser.parse_args()
        u = User.query.filter_by(login=args['login']).first()
        if u is not None:
            abort(400, message="User already exists")
        else:
            u = User(login=args['login'])
            u.insert()
        return {'user': marshal(u, user_fields)}, 201
