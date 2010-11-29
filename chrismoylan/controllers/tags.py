import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chrismoylan.lib.base import BaseController, render

log = logging.getLogger(__name__)

class TagsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('tag', 'tags')
    requires_auth = ['new', 'create', 'edit', 'update', 'delete'] #list

    def index(self, format='html'):
        """GET /tags: All items in the collection"""
        # url('tags')

    def create(self):
        """POST /tags: Create a new item"""
        # url('tags')

    def new(self, format='html'):
        """GET /tags/new: Form to create a new item"""
        # url('new_tag')

    def update(self, id):
        """PUT /tags/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('tag', id=ID),
        #           method='put')
        # url('tag', id=ID)

    def delete(self, id):
        """DELETE /tags/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('tag', id=ID),
        #           method='delete')
        # url('tag', id=ID)

    def show(self, id, format='html'):
        """GET /tags/id: Show a specific item"""
        # url('tag', id=ID)

    def edit(self, id, format='html'):
        """GET /tags/id/edit: Form to edit an existing item"""
        # url('edit_tag', id=ID)
