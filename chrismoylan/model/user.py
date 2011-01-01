"""The model for the users"""

import hashlib

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime, Boolean
from sqlalchemy.orm import relation
from chrismoylan.model.meta import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), nullable=False)
    password = Column(UnicodeText, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = self.hash(password)

    @staticmethod
    def hash(password):
        return hashlib.md5(password).hexdigest()
