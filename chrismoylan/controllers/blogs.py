import logging

from formalchemy import FieldSet, Grid

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import webhelpers.paginate as paginate

#import chrismoylan.lib.helpers as h

from chrismoylan.lib.base import BaseController, render
from chrismoylan.model.meta import Session
from chrismoylan.model.blog import Blog

log = logging.getLogger(__name__)

blog_form = FieldSet(Blog)
blog_form.configure(
    include = [
        blog_form.title.required(),
        blog_form.date,
        blog_form.entry.textarea()
    ]
)

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
        create_form = blog_form.bind(Blog, data=request.POST)
        if request.POST and create_form.validate():
            blog_args = {
                'title': create_form.title.value,
                'content': create_form.content.value
            }
            blog = Blog(**blog_args)
            Session.add(blog)
            Session.commit()
            redirect('/blogs/show/%s' % blog.id)
        context = {
            'blog_form': create_form.render()
        }
        return render('/blogs/edit.html', context)

    def new(self, format='html'):
        """GET /blogs/new: Form to create a new item"""
        # url('new_blog')
        context = {
            'blog_form': blog_form.render()
        }
        return render('/blogs/edit.html', context)

    def update(self, id):
        """PUT /blogs/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('blog', id=ID),
        #           method='put')
        # url('blog', id=ID)
        if id is not None:
            blog = Session.query(Blog).filter_by(id = id).first()
            if blog is None:
                abort(404)
            blog_form = page_form.bind(blog, data=request.POST)
            if request.POST and edit_form.validate():
                blog.sync()
                Session.commit()
                redirect('/blogs/show/%s' % id)
            context = {
                'blog': blog.render(),
                'blog': blog
            }
            return render('blogs/edit.html', context)

    def delete(self, id):
        """DELETE /blogs/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('blog', id=ID),
        #           method='delete')
        # url('blog', id=ID)
        if id is None:
            abort(404)
        blog = Session.query(Blog).filter_by(id = id).first()
        if blog is None:
            abort(404)
        if request.params.get('_method') == 'DELETE':
            Session.delete(blog)
            Session.commit()
            context = {'confirm': True}
        else:
            context = {'id': id}
        return render('blogs/delete.html', context)



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
        if id is not None:
            blog = Session.query(Blog).filter_by(id = id).first()
            if blog is None:
                abort(404)
        else:
            redirect('/blogs/new')
        edit_form = blog_form.bind(blog)
        context = {
            'blog_form': blog_form.render(),
            'blog': blog
        }
        return render('/blogs/edit.html', context)
