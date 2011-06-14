"""The model for projects"""

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base, Session

class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    thumbImage = Column(Unicode(255))
    fullImage = Column(Unicode(255))
    indexImage = Column(Unicode(255))
    link = Column(Unicode(255)),
    description = Column(Unicode, nullable=False)

    tags = relation('Tag', secondary='projecttag', backref='projects')

    def __init__(self):
        pass

    @classmethod
    def find_all_tags(self):
        projects = Session.query(Project).all()
        # Use a set to only get unique results
        return set([project.tags[0] for project in projects])


class ProjectTag(Base):
    __tablename__ = "projecttag"

    id = Column(Integer, primary_key=True)
    projectid = Column(Integer, ForeignKey('project.id'))
    tagid = Column(Integer, ForeignKey('tag.id'))

    def __init__(self):
        pass


#TODO: You need to change the database around to make portfolio into projects!!!!
