""" Main application module
"""


import pyramid
import pyramid.config


def _root_view(dummy_context, dummy_request):
    return pyramid.httpexceptions.HTTPOk()


def entry_point(dummy_global_config, **settings):
    """ Application entry point
    """
    config = pyramid.config.Configurator(
        settings=settings,
    )
    config.add_route('root', '/')
    config.add_view(_root_view, route_name='root', request_method='GET')
    wsgi_app = config.make_wsgi_app()
    return wsgi_app


# EOF
