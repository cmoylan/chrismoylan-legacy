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
    email = Column(Unicode(255))
    created = Column(DateTime, nullable=False, default=datetime.now())
        
    def __init__(self, referid, name, content, created, email):
        self.referid = referid
        self.name = name
        self.content = content
        self.created = created or datetime.now()
        self.email = email or ''
