#

"""Main application module."""

import typing

import pyramid
import pyramid.config


def _root_view(
        unused_context: typing.Any,
        unused_request: pyramid.request.Request,
) -> pyramid.response.Response:
    return pyramid.httpexceptions.HTTPOk()


def entry_point(
        unused_global_config: typing.Dict[str, str],
        **settings: typing.Any,
) -> typing.Any:
    """Application entry point."""
    config = pyramid.config.Configurator(settings=settings)
    config.add_route('root', '/')
    config.add_view(_root_view, route_name='root', request_method='GET')
    wsgi_app = config.make_wsgi_app()
    return wsgi_app


# EOF
