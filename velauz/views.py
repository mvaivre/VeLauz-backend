from pyramid.view import view_config



@view_config(route_name='test', renderer='jsonp')
def my_view(request):
    testParam = request.params.get('testParam')
    return { 'testme': testParam + 'yes' }

@view_config(route_name='login', renderer='jsonp')
def login(request):
    if 'login' in request.params and 'password' in request.params:
        userid = request.params['login']
        password = request.params['password']
        if check_password(login, password):
            headers = remember(request, userid)
            response = Response('')
            response.headers.extend(headers)
            return response
        return HTTPUnauthorized(detail='Bad Login')
    return HTTPUnauthorized(detail='Bad Login')


def logout(request):
    headers = forget(request)
    return HTTPFound('/', headers=headers)