from lab1.db import Base
from .discipline import Discipline
from .rating import Rating


def create_schema(engine):
    Base.metadata.create_all(engine)