"""The model for projects"""

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base

class Project(Base):
    __tablename__ = "portfolio"

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    thumbImage = Column(Unicode(255))
    fullImage = Column(Unicode(255))
    indexImage = Column(Unicode(255))
    link = Column(Unicode(255)),
    description = Column(Unicode, nullable=False)

    #tags = relation('Tag', secondary='blogtag', backref='blogs')

    def __init__(self):
        pass

