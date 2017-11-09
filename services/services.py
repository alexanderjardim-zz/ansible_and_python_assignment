from flask import Flask
app = Flask(__name__)

@app.route('/users/', methods = ['GET'])
def users():
    return 'TODO: List all available/active users'

@app.route('/users/add', methods = ['POST'])
def users_add():
    return 'TODO: Create a new user'

@app.route('/users/<user_id>', methods = ['GET'] )
def users_get_by_user_id(user_id):
    return 'TODO: Show details from user with user_id'

@app.route('/roles/', methods=['GET'])
def roles():
    return 'TODO: List all available roles'

@app.route('/roles/add', methods=['POST'])
def roles_add():
    return 'TODO: Create new role'

@app.route('/roles/<role_id>', methods=['GET'])
def roles_get_role_by_id(role_id):
    return 'TODO: Show details from role with role_id'

@app.route('/services/', methods=['GET'])
def services():
    return 'TODO: List all available services'

@app.route('/services/add', methods=['POST'])
def services_add():
    return 'TODO: Create new service'

@app.route('/services/<service_id>', methods=['GET'])
def services_get_service_by_id(service_id):
    return 'TODO: Show details from service with service_id'
