import sqlalchemy as sql
from . import Base


class Discipline(Base):
    __tablename__ = 'discipline'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True)

    university_name = sql.Column(sql.String, nullable=False)
    standard = sql.Column(sql.String, nullable=False)
    name = sql.Column(sql.String, nullable=False)
    faculty = sql.Column(sql.String, nullable=False)
    specialty = sql.Column(sql.String, nullable=False)
    term = sql.Column(sql.Integer, nullable=False)
    lecture_hours = sql.Column(sql.Integer, nullable=False)
    practice_hours = sql.Column(sql.Integer, nullable=False)
    laboratory_hours = sql.Column(sql.Integer, nullable=False)
    is_exam = sql.Column(sql.Boolean, nullable=False)