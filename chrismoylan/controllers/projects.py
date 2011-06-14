import logging

from formalchemy import FieldSet, Field

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict
import webhelpers.paginate as paginate

from chrismoylan.lib.base import BaseController, render
from chrismoylan.model.meta import Session
from chrismoylan.model.project import Project, ProjectTag
from chrismoylan.model.tag import Tag

log = logging.getLogger(__name__)

project_form = FieldSet(Project)

class ProjectsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('project', 'projects')
    requires_auth = ['index', 'list','new', 'create', 'edit', 'update', 'delete']

    def index(self, format='html'):
        """GET /projects: All items in the collection"""
        # url('projects')
        projects = Session.query(Project).order_by(Project.id.desc())
        project_paginator = paginate.Page(
            projects,
            page = int(request.params.get('page', 1)),
            items_per_page = 15,
            controller = 'projects',
            action = 'index',
        )

        tags = Project.find_all_tags()

        return render('projects/index.html', {
            'projects': project_paginator,
            'tags': tags
        })

    def categories(self, id=None, format='html'):
        pass


    def show(self, id=None, format='html'):
        """GET /projects/id: Show a specific item"""
        # url('project', id=ID)
        if id is None:
            return redirect(url(controller='projects', action='index'))

        project_q = Session.query(Project).filter_by(id=int(id)).first()

        if project_q is None:
            # TODO FLash an alert, redirect to index
            abort(404)

        return render('/projects/show.html', {'project': project_q})


    @restrict('POST')
    def create(self):
        """POST /projects: Create a new item"""
        # url('projects')
        project = project()
        create_form = project_form.bind(project, data=request.POST or None)
        if create_form.validate():
            create_form.sync()
            Session.add(project)
            Session.commit()
            redirect('/projects/index')
        return render('projects/edit.html', {'project_form': create_form.render()})


    def new(self, format='html'):
        """GET /projects/new: Form to create a new item"""
        # url('new_project')
        return render('projects/edit.html', {'project_form': project_form.render()})


    @restrict('POST')
    def update(self, id):
        """PUT /projects/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('project', id=ID),
        #           method='put')
        # url('project', id=ID)
        project = Session.query(project).filter_by(id = id).first()
        if project is None:
            redirect('/projects/new')

        edit_form = project_form.bind(project, data=request.POST)

        if edit_form.validate():
            edit_form.sync()
            Session.commit()
            redirect('/projects/index')

        return render('projects/edit.html', {
            'project_form': edit_form.render(),
            'project': project
        })


    def delete(self, id):
        """DELETE /projects/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('project', id=ID),
        #           method='delete')
        # url('project', id=ID)
        project = Session.query(project).filter_by(id = id).first()
        if project is not None:
            Session.delete(project)
            Session.commit()
            redirect('/projects/index')
        else:
            return 'project does not exist'


    def edit(self, id, format='html'):
        """GET /projects/id/edit: Form to edit an existing item"""
        # url('edit_project', id=ID)
        if id is not None:
            project = Session.query(project).filter_by(id = id).first()
            print project
            if project is None:
                abort(404)
        else:
            redirect('/projects/new')

        edit_form = project_form.bind(project)

        return render('/projects/edit.html', {
            'project_form': edit_form.render(),
            'project': project
        })


    def list(self):
        projects = Session.query(Project).all()

        project_paginator = paginate.Page(
            projects,
            page = int(request.params.get('page', 1)),
            items_per_page = 25,
            controller = 'projects',
            action = 'list',
        )

        return render('projects/list.html', {'projects': project_paginator})
