"""The model for the blog/journal"""

from sqlalchemy import Table, Column, ForeignKey, desc
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base, Session
from datetime import datetime


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now())
    title = Column(Unicode(255), nullable=False)
    entry = Column(UnicodeText, nullable=False)

    comments = relation('Comment', backref='blog', primaryjoin='Blog.id == Comment.referid', cascade='all')
    tags = relation('Tag', secondary='blogtag', backref='blogs')

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.title = kwargs['title']
            self.date = kwargs['date'] or datetime.now()
            self.entry = kwargs['entry']

    def next(self):
        return Session.query(Blog).filter(Blog.id > self.id).order_by(Blog.id).first()

    def prev(self):
        return Session.query(Blog).filter(Blog.id < self.id).order_by(desc(Blog.id)).first()

class BlogTag(Base):
    __tablename__ = 'blogtag'

    blogid = Column(Integer, ForeignKey('blog.id'), primary_key=True)
    tagid = Column(Integer, ForeignKey('tag.id'), primary_key=True)

    def __init__(self):
        pass
