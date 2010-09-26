"""The model for the photos and albums"""

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from ideabox.model.meta import Base
from ideabox.model.user import User
from datetime import datetime

class Album(Base):
    __tablename__ = 'album'
    
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    description = Column(Unicode, nullable=False)
    thumb = Column(Integer, ForeignKey('photo.id'), default=0)
    date = Column(DateTime, default=now())
    folder = Column(Unicode, nullable=False)
    
    def __init__(self):
        pass
    

class Photo(Base):
    __tablename__ = 'photo'
    
    id = Column(Integer, primary_key=True)
    album_id = Column(Integer, ForeignKey('album.id'), nullable=False)
    filename = Column(Unicode(255), nullable=False)
    thumbImage = Column(Unicode(255), nullable=False)
    fullImage = Column(Unicode(255), nullable=False)
    description = Column(Unicode)
    date = Column(DateTime, default=now())

    def __init__(self):
        pass

    
