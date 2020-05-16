import sqlalchemy as sql
from sqlalchemy.orm import relationship

from . import Base

lesson_group = sql.Table('lesson_group', Base.metadata,
    sql.Column('group_id', sql.Integer, sql.ForeignKey('group.id')),
    sql.Column('lesson_record_id', sql.Integer, sql.ForeignKey('lesson_record.id'))
)


class LessonRecord(Base):
    __tablename__ = 'lesson_record'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True)

    name = sql.Column(sql.String(200), nullable=False)
    teacher_id = sql.Column(sql.Integer, sql.ForeignKey('person.id'), nullable=False)
    teacher = relationship('teacher')
    weekday = sql.Column(sql.Integer)
    hour = sql.Column(sql.Integer)
    minute = sql.Column(sql.Integer)
    room = sql.Column(sql.String(10))
    groups = relationship('Group', secondary=lesson_group)

    
    def serialize(self):
        return {
            'name': self.name,
            'teacher': self.teacher.serialize(),
            'weekday': self.weekday,
            'hour': self.hour,
            'minute': self.minute,
            'room': self.room,
            'groups': [g.serialize() for g in self.groups],
        }