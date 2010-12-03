import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chrismoylan.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UsersController(BaseController):

    def login(self):
        return render('users/login.html')

    def authenticate(self):
        try:
            username = request.params['username']
            password = request.params['password']
        except KeyError:
            return None
        # do some crap to log in...
        session['user'] = {
            'id': 'user.id',
            'username': 'user.username'
        }
        session.save()
        return redirect(session['path_before_login'])

    def logout(self):
        if 'user' not in session:
            return redirect('/')
        else:
            session.pop('user')
            session.save()
            #return redirect('/')
            return 'logged out'
