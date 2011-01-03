import logging

from formalchemy import FieldSet, Field

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict
import webhelpers.paginate as paginate

from chrismoylan.lib.base import BaseController, render
from chrismoylan.model.meta import Session
from chrismoylan.model.blog import Blog
from chrismoylan.controllers.comments import comment_form

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
    requires_auth = ['new', 'create', 'edit', 'update', 'delete'] #list

    def index(self, format='html'):
        """GET /blogs: All items in the collection"""
        # url('blogs')
        blogs = Session.query(Blog).order_by(Blog.date.desc())
        blog_paginator = paginate.Page(
            blogs,
            page = int(request.params.get('page', 1)),
            items_per_page = 10,
            controller = 'blogs',
            action = 'index',
        )
        return render('/blogs/index.html', {'blogs': blog_paginator})


    @restrict('POST')
    def create(self):
        """POST /blogs: Create a new item"""
        # url('blogs')
        create_form = blog_form.bind(Blog, data=request.POST)
        if request.POST and create_form.validate():
            blog_args = {
                'title': create_form.title.value.strip(),
                'entry': create_form.entry.value.strip(),
                'date': create_form.date.value
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


    @restrict('POST')
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
            edit_form = blog_form.bind(blog, data=request.POST)

            if request.POST and edit_form.validate():
                edit_form.sync()
                Session.commit()
                redirect('/blogs/show/%s' % id)

            return render('blogs/edit.html', {
                'blog': edit_form.render(),
                'blog': blog
            })


    @restrict('POST')
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
            # TODO FLash an alert, redirect to index
            abort(404)

        comment_form.append(
            Field(name='captcha').required().with_metadata(
                instructions='What color is the grass? (hint: green)'
        ))
        #c.blog = blog_q
        return render('/blogs/show.html', {
            'blog': blog_q,
            'comment_form': comment_form.render()
        })


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
            'blog_form': edit_form.render(),
            'blog': blog
        }
        return render('/blogs/edit.html', context)
