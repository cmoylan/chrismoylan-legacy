"""The model for tags"""

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base


class Tag(Base):
    __tablename__ = "tag"
    
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100), nullable=False, unique=True)
    
    def __init__(self):
        pass
    
    def __init__(self, name):
        self.name = name
        
