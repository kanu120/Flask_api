from .controller import api as userapi
BASE_ROUTE = 'UserOperations'

def register_routes(api, app, root='api'):
     api.add_namespace(userapi, path=f'/{root}/{BASE_ROUTE}')