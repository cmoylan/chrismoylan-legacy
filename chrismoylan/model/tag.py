"""The model for tags"""

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base, Session
#from chrismoylan.model.blog import BlogTag


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.name = kwargs['name']

    def __repr__(self):
        return self.name

    @classmethod
    def find_all(self):
        tags = Session.query(Tag).all()
        return [str(tag.name) for tag in tags]
