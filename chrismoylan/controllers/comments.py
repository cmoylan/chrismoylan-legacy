import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chrismoylan.lib.base import BaseController, render

log = logging.getLogger(__name__)

class CommentsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('comment', 'comments')

    def index(self, format='html'):
        """GET /comments: All items in the collection"""
        # url('comments')

    def create(self):
        """POST /comments: Create a new item"""
        # url('comments')

    def new(self, format='html'):
        """GET /comments/new: Form to create a new item"""
        # url('new_comment')

    def update(self, id):
        """PUT /comments/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('comment', id=ID),
        #           method='put')
        # url('comment', id=ID)

    def delete(self, id):
        """DELETE /comments/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('comment', id=ID),
        #           method='delete')
        # url('comment', id=ID)

    def show(self, id, format='html'):
        """GET /comments/id: Show a specific item"""
        # url('comment', id=ID)

    def edit(self, id, format='html'):
        """GET /comments/id/edit: Form to edit an existing item"""
        # url('edit_comment', id=ID)
