"""The model for comments"""

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base
from datetime import datetime

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    referid = Column(Integer, ForeignKey("blog.id"), nullable=False)
    content = Column(UnicodeText, nullable=False)
    name = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False)
    created = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.referid = kwargs['referid']
            self.name = kwargs['name']
            self.content = kwargs['content']
            self.created = datetime.now()
            self.email = kwargs['email'] or ''
