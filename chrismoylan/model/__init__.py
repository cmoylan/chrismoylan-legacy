"""The application's model objects"""
from chrismoylan.model.meta import Session, Base
from chrismoylan.model.blog import Blog, BlogTag
from chrismoylan.model.comment import Comment
from chrismoylan.model.tag import Tag


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
