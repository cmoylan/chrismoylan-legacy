import logging

from formalchemy import FieldSet

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict

from chrismoylan.lib.base import BaseController, render
from chrismoylan.model.meta import Session
from chrismoylan.model.comment import Comment
from chrismoylan.model.blog import Blog

log = logging.getLogger(__name__)

comment_form = FieldSet(Comment)
comment_form.configure(
    include = [
        comment_form.name,
        comment_form.email.with_metadata(
            instructions='Used to help prevent spam but will not be published'
        ),
        comment_form.content.textarea()
    ],
    focus = False
)

class CommentsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('comment', 'comments')

    @restrict('POST')
    def create(self, blogid):
        """POST /comments: Create a new item"""
        # url('comments')
        create_form = comment_form.bind(Comment, data=request.POST)

        if create_form.validate():
            # Validate captcha
            if create_form.captcha.value.strip().lower() != 'green':
                return render('/comments/error.html')

            comment_args = {
                'referid': blogid,
                'name': create_form.name.value.strip(),
                'email': create_form.email.value.strip(),
                'content': create_form.content.value.strip()
            }
            comment = Comment(**comment_args)
            Session.add(comment)
            Session.commit()

            session['flash'] = 'Great success! Your comment was posted.'
            session['flash_class'] = 'success'
            session.save()

            redirect('/journal/%s' % blogid)

        blog = Session.query(Blog).filter_by(id = int(blogid)).first()

        session['flash'] = 'There was a problem with your comment.'
        session['flash_class'] = 'fail'
        session.save()

        return render('/blogs/show.html', {
            'blog': blog,
            'comment_form': create_form.render()
        })


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
