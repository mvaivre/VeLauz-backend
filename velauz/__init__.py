from pyramid.config import Configurator
from pyramid.renderers import JSONP
from pyramid.mako_templating import renderer_factory as mako_renderer_factory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    config.add_renderer('.html', mako_renderer_factory)
    config.add_renderer('.js', mako_renderer_factory)
    config.add_renderer('jsonp', JSONP(param_name='callback', indent=4))

    config.add_static_view('app', 'velauz:static/VeLauz-app')

    config.add_route('home', '/')
    config.add_route('toto', '/service')

    config.add_view(route_name='home', renderer='velauz:templates/index.mako') #velauz: est le package
    # Static files
    config.scan()
    return config.make_wsgi_app()
