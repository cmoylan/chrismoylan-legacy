import logging

from formalchemy import FieldSet, Field

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict
import webhelpers.paginate as paginate

from chrismoylan.lib.base import BaseController, render
from chrismoylan.model.meta import Session
from chrismoylan.model.tag import Tag

log = logging.getLogger(__name__)

tag_form = FieldSet(Tag)
tag_form.configure(
    include = [tag_form.name]
)

class TagsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('tag', 'tags')
    requires_auth = ['index', 'new', 'create', 'edit', 'update', 'delete']

    def index(self, format='html'):
        """GET /tags: All items in the collection"""
        # url('tags')
        tags = Session.query(Tag).all()
        tag_paginator = paginate.Page(
            tags,
            page = int(request.params.get('page', 1)),
            items_per_page = 20,
            controller = 'tags',
            action = 'index',
        )
        return render('tags/list.html', {'tags': tag_paginator})


    @restrict('POST')
    def create(self):
        """POST /tags: Create a new item"""
        # url('tags')
        tag = Tag()
        create_form = tag_form.bind(tag, data=request.POST or None)
        if create_form.validate():
            create_form.sync()
            Session.add(tag)
            Session.commit()
            redirect('/tags/index')
        return render('tags/edit.html', {'tag_form': create_form.render()})


    def new(self, format='html'):
        """GET /tags/new: Form to create a new item"""
        # url('new_tag')
        return render('tags/edit.html', {'tag_form': tag_form.render()})


    @restrict('POST')
    def update(self, id):
        """PUT /tags/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('tag', id=ID),
        #           method='put')
        # url('tag', id=ID)
        tag = Session.query(Tag).filter_by(id = id).first()
        if tag is None:
            redirect('/tags/new')

        edit_form = tag_form.bind(tag, data=request.POST)

        if edit_form.validate():
            edit_form.sync()
            Session.commit()
            redirect('/tags/index')

        return render('tags/edit.html', {
            'tag_form': edit_form.render(),
            'tag': tag
        })


    def delete(self, id):
        """DELETE /tags/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('tag', id=ID),
        #           method='delete')
        # url('tag', id=ID)
        tag = Session.query(Tag).filter_by(id = id).first()
        if tag is not None:
            Session.delete(tag)
            Session.commit()
            redirect('/tags/index')
        else:
            return 'Tag does not exist'


    def edit(self, id, format='html'):
        """GET /tags/id/edit: Form to edit an existing item"""
        # url('edit_tag', id=ID)
        if id is not None:
            tag = Session.query(Tag).filter_by(id = id).first()
            print tag
            if tag is None:
                abort(404)
        else:
            redirect('/tags/new')

        edit_form = tag_form.bind(tag)

        return render('/tags/edit.html', {
            'tag_form': edit_form.render(),
            'tag': tag
        })
