import logging

from formalchemy import FieldSet, Grid

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chrismoylan.lib.base import BaseController, Session, render
from chrismoylan.model.page import Page

log = logging.getLogger(__name__)

page_form = FieldSet(Page)
page_form.configure(
    include = [
        page_form.title.required(),
        page_form.content.textarea()
    ]
)

class PagesController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('page', 'pages')
    requires_auth = ['new', 'create', 'edit', 'save', 'list', 'delete']


    def create(self):
        """POST /pages: Create a new item"""
        # url('pages')

    def new(self, format='html'):
        """GET /pages/new: Form to create a new item"""
        # url('new_page')
        # Render edit.html with a blank page object
        return render('/pages/edit.html')

    def update(self, id):
        """PUT /pages/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('page', id=ID),
        #           method='put')
        # url('page', id=ID)
        if id is not None:
            page = Session.query(Page).filter_by(id = id).first()
            if page is None:
                abort(404)
            edit_form = page_form.bind(page, data=request.POST)
            if request.POST and edit_form.validate():
                edit_form.sync()
                Session.commit()
                redirect('/pages/show/%s' % id)
            context = {
                'edit_form': edit_form.render(),
                'page': page
            }
            return render('pages/edit.html', context)

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
        if id is None:
            abort(404)
        page = Session.query(Page).filter_by(id = id).first()
        if page is None:
            abort(404)
        context = {'page': page}
        return render('/pages/show.html', context)

    def edit(self, id, format='html'):
        """GET /pages/id/edit: Form to edit an existing item"""
        # url('edit_page', id=ID)
        if id is not None:
            page = Session.query(Page).filter_by(id = id).first()
            if page is None:
                abort(404)
        else:
            redirect('/pages/new')
        edit_form = page_form.bind(page)
        context = {
            'edit_form': edit_form.render(),
            'page': page
        }
        return render('pages/edit.html', context)

        #identity = request.environ.get('repoze.who.identity')
        #if identity is None:
        #    request.environ['pylons.status_code_redirect'] = True
        #    abort(401, 'Not authenticated')
        #else:
        #    return 'welcome aboard'
