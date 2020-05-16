import sqlalchemy as sql
from sqlalchemy.orm import relationship

from lab1.model.mysql.project import project_person
from . import Base

group_person = sql.Table('group_person', Base.metadata,
    sql.Column('group_id', sql.Integer, sql.ForeignKey('group.id')),
    sql.Column('person_id', sql.Integer, sql.ForeignKey('person.id'))
)

class Group(Base):
    __tablename__ = 'group'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True)

    name = sql.Column(sql.String(100), nullable=False)
    study_type = sql.Column(sql.String(200), nullable=False)
    school = sql.Column(sql.String(200), nullable=False)
    direction = sql.Column(sql.String(200), nullable=False)
    speciality = sql.Column(sql.String(200), nullable=False)
    qualification = sql.Column(sql.String(200), nullable=False)
    study_year = sql.Column(sql.String(10),nullable=False)
    students = relationship('Person', secondary=group_person)


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'study_type': self.study_type,
            'school': self.school,
            'direction': self.direction,
            'speciality': self.speciality,
            'qualification': self.qualification,
            'study_year': self.study_year,
            'students': [s.serialize() for s in self.students]
        }