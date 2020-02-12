from .users import UsersApi, UserApi
from .pubs import PubsApi, PubApi

def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<id>')
    api.add_resource(PubsApi, '/api/pubs')