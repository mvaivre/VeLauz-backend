from pyramid.view import view_config



@view_config(route_name='test', renderer='jsonp')
def my_view(request):
    testParam = request.params.get('testParam')
    return { 'testme': testParam + 'yes' }
