import logging

from formalchemy import FieldSet

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chrismoylan.lib.base import BaseController, render
from chrismoylan.model.meta import Session
from chrismoylan.model.comment import Comment

log = logging.getLogger(__name__)

comment_form = FieldSet(Comment)
comment_form.configure(
    include = [
    ]
)

class CommentsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('comment', 'comments')

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
