from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from velauz.models import DBSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    # Static config
    config.add_route('home', '/')
    config.add_view('home', 'velauz:index.html', cache_max_age=3600) #velauz: est le package
    

    config.scan()
    return config.make_wsgi_app()
