import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import webhelpers.paginate as paginate

#import chrismoylan.lib.helpers as h

from chrismoylan.lib.base import BaseController, render
from chrismoylan.model.meta import Session
from chrismoylan.model.blog import Blog

log = logging.getLogger(__name__)

class BlogsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('blog', 'blogs')

    def index(self, format='html'):
        """GET /blogs: All items in the collection"""
        # url('blogs')
        blog_q = Session.query(Blog).order_by(Blog.id.desc())
        blog_paginator = paginate.Page(
            blog_q,
            page = int(request.params.get('page', 1)),
            items_per_page = 10,
            controller = 'blogs',
            action = 'index',
            )
        return render('/blogs/index.html', {'blogs': blog_paginator})

    def create(self):
        """POST /blogs: Create a new item"""
        # url('blogs')

    def new(self, format='html'):
        """GET /blogs/new: Form to create a new item"""
        # url('new_blog')

    def update(self, id):
        """PUT /blogs/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('blog', id=ID),
        #           method='put')
        # url('blog', id=ID)

    def delete(self, id):
        """DELETE /blogs/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('blog', id=ID),
        #           method='delete')
        # url('blog', id=ID)

    def show(self, id=None, format='html'):
        """GET /blogs/id: Show a specific item"""
        # url('blog', id=ID)
        if id is None:
            return redirect(url(controller='blogs', action='index'))
        blog_q = Session.query(Blog).filter_by(id=int(id)).first()
        if blog_q is None:
            abort(404)
        return render('/blogs/show.html', {'blog': blog_q})

    def edit(self, id, format='html'):
        """GET /blogs/id/edit: Form to edit an existing item"""
        # url('edit_blog', id=ID)
        blog_q = Session.query(Blog).filter_by(id=int(id)).first()
        if blog_q is None:
            abort(404)
        return render('/blogs/edit.html', {'blog': blog_q})
