import datetime

from lab1.model.postgres import Rating
from .common import *
from ..model import databases
from ..model.postgres.discipline import Discipline
from sqlalchemy.orm import sessionmaker

def fill_postgres():
    Session = sessionmaker(bind=databases['postgres']['engine'])
    session = Session()

    discipline_count = 50
    rating_count = 5*discipline_count

    disciplines = []
    print('Генерируем дисциплины', end='')
    for i in range(discipline_count):
        d = Discipline()
        d.university_name = generate_university()
        d.standard = generate_standard()
        d.name = generate_discipline()
        d.faculty = generate_faculty()
        d.specialty = generate_specialty()
        d.term = generate_term()
        d.lecture_hours = generate_hours()
        d.laboratory_hours = generate_hours()
        d.practice_hours = generate_hours()
        d.is_exam = generate_is_exam()
        session.add(d)
        disciplines.append(d)
        print('.', end='')
    print()

    print('Генерируем оценки', end='')
    for i in range(rating_count):
        r = Rating()
        r.discipline = random.choice(disciplines)
        r.rating, a = generate_rating()
        r.date = datetime.datetime.now()
        r.teacher_name = generate_name()
        r.student_name = generate_name()
        r.student_id = generate_person_id()
        r.teacher_id = generate_person_id()

        session.add(r)
        print('.', end='')
    print()

    session.commit()