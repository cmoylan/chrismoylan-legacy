import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chrismoylan.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UsersController(BaseController):

    def login(self):
        return 'serving the login form...'
