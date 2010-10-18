"""The model for the blog/journal"""

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base
from datetime import datetime


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now())
    title = Column(Unicode(255), nullable=False)
    entry = Column(UnicodeText, nullable=False)

    comments = relation("Comment", backref="blog", primaryjoin="Blog.id == Comment.referid", cascade="all")
    tags = relation("Tag", secondary='blogtag', backref="blogs")

    def __init__(self, title, date, entry):
        self.title = title
        self.date = date or datetime.now()
        self.entry = entry


class BlogTag(Base):
    __tablename__ = 'blogtag'

    blog_id = Column(Integer, ForeignKey('blog.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)

    def __init__(self):
        pass
