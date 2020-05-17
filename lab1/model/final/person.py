import sqlalchemy as sql
from sqlalchemy.orm import relationship

from . import Base


class Person(Base):
    __tablename__ = 'f_person'

    id = sql.Column(sql.Integer, primary_key=True)

    name = sql.Column(sql.String(100))
    position = sql.Column(sql.String(100))

    birth_date = sql.Column(sql.Date)
    birth_place = sql.Column(sql.String(100))
    faculty = sql.Column(sql.String(100))

    contract_from = sql.Column(sql.Date)
    contract_to = sql.Column(sql.Date)

    is_beneficiary = sql.Column(sql.Boolean)
    is_contract_student = sql.Column(sql.Boolean)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'birth_date': self.birth_date,
            'birth_place': self.birth_place,
            'faculty': self.faculty,
            'contract_from': self.contract_from,
            'contract_to': self.contract_to,
            'is_beneficiary': self.is_beneficiary,
            'is_contract_student': self.is_contract_student

        }