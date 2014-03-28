from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.ext.declarative import declarative_base

from velauz.models import DBSession

Base = declarative_base()

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    # Static config
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_view(route_name='home', renderer='velauz:templates/index.mako') #velauz: est le package
    
    config.scan()
    return config.make_wsgi_app()
