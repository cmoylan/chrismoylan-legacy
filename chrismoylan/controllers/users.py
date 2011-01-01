import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict

from chrismoylan.lib.base import BaseController, Session, render
from chrismoylan.model.user import User

log = logging.getLogger(__name__)

class UsersController(BaseController):

    #def new(self):
    #    return render('users/new.html')

    #@restrict('POST')
    #def create(self):
    #    try:
    #        username = request.params['username']
    #        pass1 = request.params['password']
    #        pass2 = request.params['password2']
    #    except KeyError:
    #        return "Fail"

    #    if pass1 == pass2:
    #        user = User(username, pass1)
    #        Session.add(user)
    #        Session.commit()
    #        return '%s created' % username
    #    else:
    #        return "Passwords did not match"

    def login(self):
        return render('users/login.html')

    @restrict('POST')
    def authenticate(self):
        try:
            username = request.params['username']
            password = request.params['password']

            password = User.hash(password)
            user = Session.query(User).filter(User.username == username).\
                      filter(User.password == password).\
                      one()
        except:
            session['flash'] = 'Authentication Failed'
            session.save()
            return redirect('/login')

        session['user'] = {
            'id': 'user.id',
            'username': 'user.username'
        }
        session['flash'] = 'Successfully logged in'
        session.save()

        if session.get('path_before_login'):
            return redirect(session['path_before_login'])
        else:
            return redirect('/')

    def logout(self):
        if 'user' not in session:
            session['flash'] = 'Not logged in'
            session.save()
            return redirect('/')
        else:
            session.pop('user')
            session.save()
            session['flash'] = 'Successfully logged out'
            session.save()
            return redirect('/')
