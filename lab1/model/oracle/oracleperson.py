import sqlalchemy as sql
from sqlalchemy.orm import relationship

from lab1.model.mysql.project import project_person
from . import Base


class OraclePerson(Base):
    __tablename__ = 'oracle_person'

    id = sql.Column(sql.Integer, sql.Sequence('oracle_person_seq_id'), primary_key=True)

    name = sql.Column(sql.String(100), nullable=False)
    birth_date = sql.Column(sql.Date, nullable=False)
    birth_place = sql.Column(sql.String(100), nullable=False)
    faculty = sql.Column(sql.String(100), nullable=False)
    position = sql.Column(sql.String(100), nullable=False)

    contractFrom = sql.Column(sql.Date, nullable=False)
    contractTo = sql.Column(sql.Date, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_date': self.birth_date,
            'birth_place': self.birth_place,
            'faculty': self.faculty,
            'position': self.position,
            'contractFrom': self.contractFrom,
            'contractTo': self.contractTo,
        }