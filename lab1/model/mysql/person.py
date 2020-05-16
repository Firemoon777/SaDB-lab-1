import sqlalchemy as sql
from sqlalchemy.orm import relationship

from lab1.model.mysql.project import project_person
from . import Base

from .conference import conference_person
from .publication import publication_person


class Person(Base):
    __tablename__ = 'person'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True)

    name = sql.Column(sql.String(100), nullable=False)
    position = sql.Column(sql.String(100), nullable=False)

    conferences = relationship('Conference', secondary=conference_person, back_populates='participants')
    publications = relationship('Publication', secondary=publication_person, back_populates='authors')
    projects = relationship('Project', secondary=project_person, back_populates='participants')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position
        }