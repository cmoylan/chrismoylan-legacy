"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons import session
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render

from chrismoylan.model.meta import Session

class BaseController(WSGIController):
    requires_auth = []

    def __before__(self, action, **params):
        if action in self.requires_auth:
            if 'user' not in session:
                #session['path_before_login'] = request.path_info
                #session.save()
                #return redirect_to(h.url_for(controller='login', action='signin'))
                print 'AUTH REQUIRED!!!'


    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            self.identity = environ.get('repoze.who.identity')
            return WSGIController.__call__(self, environ, start_response)
        finally:
            Session.remove()
