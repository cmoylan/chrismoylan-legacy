"""The model for the blog/journal"""

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base
from datetime import datetime

blogtag_table = Table('blogtag', Base.metadata,
    Column('blog_id', Integer, ForeignKey(), primary_key=True),
    Column('tag_id', Integer, ForeignKey(), primary_key=True),
)

class Blog(Base):
    __tablename__ = 'blog'
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=now())
    title = Column(Unicode(255), nullable=False)
    entry = Column(UnicodeText, nullable=False)
    
    comments = relation("Comment", backref="blog", primaryjoin="Blog.id == Comment.referid", cascade="all")
    tags = relation("Tag", secondary=blogtag_table, backref="blogs")
    
    def __init__(self):
        pass
    
    def __init__(self, title, date, entry):
        self.title = title
        self.date = date or datetime.now()
        self.entry = entry