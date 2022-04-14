
def connectionroutes(api,app,root='api'):
    from appfolder.userdata import register_routes as reg_route
    reg_route(api, app)
    