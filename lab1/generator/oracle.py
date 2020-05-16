import datetime
import sys

from lab1.model.oracle import OraclePerson, Rating
from .common import *
from ..model import databases
from sqlalchemy.orm import sessionmaker


def fill_oracle():
    print('Генерация данных в oracle...', end='')
    sys.stdout.flush()
    Session = sessionmaker(bind=databases['oracle']['engine'])
    session = Session()

    person_count = 50
    rating_count = person_count*5

    person = []
    for i in range(person_count):
        p = OraclePerson()
        p.name = generate_name()
        p.birth_date = datetime.datetime.now()
        p.birth_place = generate_place()
        p.faculty = generate_faculty()
        p.position = generate_position()
        p.contractFrom = datetime.datetime.now()
        p.contractTo = datetime.datetime.now()
        session.add(p)
        person.append(p)

    session.commit()

    for i in range(rating_count):
        r = Rating()
        r.discipline = generate_discipline()
        r.rating, r.rating_letter = generate_rating()
        r.date = datetime.datetime.now()
        r.student = random.choice(person)
        session.add(r)

    session.commit()
    print('ОК')