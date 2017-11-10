from model import User

def is_admin(token):
    print token
    if get_user_role_id_by_token(token) == 1:
        return True

def is_bot(token):
    if get_user_role_id_by_token(token) == 2:
        return True

def is_user(token):
    if get_user_role_id_by_token(token) > 2:
        return True

def get_user_role_id_by_token(auth_token):
    print auth_token
    u = User.query.filter_by(token=auth_token).first()
    print u
    if u is not None:
        return u.role.id
