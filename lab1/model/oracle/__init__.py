from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .person import Person
from .group import Group
from .rating import Rating
from .lesson_record import LessonRecord


def create_schema(engine):
    Base.metadata.create_all(engine)