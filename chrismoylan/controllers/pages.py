import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chrismoylan.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PagesController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('page', 'pages')

    def index(self, format='html'):
        """GET /pages: All items in the collection"""
        # url('pages')
        # This will show the 4 sections - reading, writing, listening

    def create(self):
        """POST /pages: Create a new item"""
        # url('pages')

    def new(self, format='html'):
        """GET /pages/new: Form to create a new item"""
        # url('new_page')

    def update(self, id):
        """PUT /pages/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('page', id=ID),
        #           method='put')
        # url('page', id=ID)

    def delete(self, id):
        """DELETE /pages/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('page', id=ID),
        #           method='delete')
        # url('page', id=ID)

    def show(self, id, format='html'):
        """GET /pages/id: Show a specific item"""
        # url('page', id=ID)

    def edit(self, id, format='html'):
        """GET /pages/id/edit: Form to edit an existing item"""
        # url('edit_page', id=ID)
        identity = request.environ.get('repoze.who.identity')
        if identity is None:
            request.environ['pylons.status_code_redirect'] = True
            abort(401, 'Not authenticated')
        else:
            return 'welcome aboard'
