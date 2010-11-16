"""The model for pages"""
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base

class Page(Base):
    __tablename__ = "page"
    
    id = Column(Integer, primary_key=True)
    posted = Column(DateTime, default=u'now()')
    title = Column(Unicode(255), default=u'Untitled')
    content = Column(Unicode, nullable=False)
    
    def __init__(self):
        pass
    
