import sqlalchemy as sql
from sqlalchemy.orm import relationship

from . import Base

class LibraryRecord(Base):
    __tablename__ = 'f_library_record'

    id = sql.Column(sql.Integer, sql.Sequence('f_library_record_seq_id'), primary_key=True)

    book_name = sql.Column(sql.String(100))
    taken_by_id = sql.Column(sql.Integer, sql.ForeignKey('f_person.id'))
    taken_by = relationship('Person')

    taken_at = sql.Column(sql.Date, nullable=False)
    returned_at = sql.Column(sql.Date)

    def serialize(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'taken_by': self.taken_by.serialize(),
            'taken_at': self.taken_at,
            'returned_at': self.returned_at,
        }