import sys

from sqlalchemy.orm import sessionmaker

from lab1.model import databases

from lab1.model.oracle.oracleperson import OraclePerson
from lab1.model.final.person import Person as FinalPerson
from lab1.model.mongo.person import Person as MongoPerson
from lab1.model.mysql.person import Person as MySQLPerson

from lab1.model.mysql.conference import Conference as MySQLConference
from lab1.model.final.conference import Conference as FinalConference

from lab1.model.postgres.discipline import Discipline as PostgreDiscipline
from lab1.model.final.discipline import Discipline as FinalDiscipline

from lab1.model.mongo.dormitory import Dormitory as MongoDormitory
from lab1.model.final.dormitory import Dormitory as FinalDormitory

from lab1.model.mongo.room import Room as MongoRoom
from lab1.model.final.room import Room as FinalRoom

from lab1.model.mongo.dormitory_person import DormitoryPerson as MongoDormitoryPerson
from lab1.model.final.dormitory_person import DormitoryPerson as FinalDormitoryPerson

from lab1.model.oracle.group import Group as OracleGroup
from lab1.model.final.group import Group as FinalGroup

from lab1.model.oracle.lesson_record import LessonRecord as OracleLessonRecord
from lab1.model.final.lesson_record import LessonRecord as FinalLessonRecord

from lab1.model.mysql.library_record import LibraryRecord as MySQLLibRecord
from lab1.model.final.library_record import LibraryRecord as FinalLibRecord

from lab1.model.mysql.project import Project as MySQLProject
from lab1.model.final.project import Project as FinalProject

from lab1.model.mysql.publication import Publication as MySQLPublication
from lab1.model.final.publication import Publication as FinalPublication

from lab1.model.postgres.rating import Rating as PostgresRating
from lab1.model.oracle.rating import Rating as OracleRating
from lab1.model.final.rating import Rating as FinalRating


def migrate_all():
    print('Миграция данных о людях...', end='')
    sys.stdout.flush()

    Session = sessionmaker(bind=databases['oracle']['engine'])
    session_oracle = Session()

    Session = sessionmaker(bind=databases['mysql']['engine'])
    session_mysql = Session()

    Session = sessionmaker(bind=databases['postgres']['engine'])
    session_postgres = Session()

    # Oracle -> Oracle
    for p in session_oracle.query(OraclePerson).all():
        f = FinalPerson()
        f.id = p.id
        f.name = p.name
        f.position = p.position
        f.birth_place = p.birth_place
        f.birth_date = p.birth_date
        f.faculty = p.faculty
        f.contract_from = p.contract_from
        f.contract_to = p.contract_to
        session_oracle.add(f)

    # Postgres -> Oracle
    for m in session_postgres.query(PostgresRating).all():
        f = session_oracle.query(FinalPerson).filter_by(id=m.student_id).first()
        if f is None:
            f = FinalPerson()
            f.id = m.student_id
            f.name = m.student_name
            session_oracle.add(f)
        f = session_oracle.query(FinalPerson).filter_by(id=m.teacher_id).first()
        if f is None:
            f = FinalPerson()
            f.id = m.teacher_id
            f.name = m.teacher_name
            session_oracle.add(f)

    # Mongo -> Oracle
    for m in MongoPerson.objects():
        f = session_oracle.query(FinalPerson).filter_by(id=m.person_id).first()
        if f is None:
            # Информации нет, создаём
            f = FinalPerson()
            f.id = m.person_id
            f.name = m.name
            f.is_beneficiary = m.is_beneficiary
            f.is_contract_student = m.is_contract_student
            session_oracle.add(f)
        else:
            f.is_beneficiary = m.is_beneficiary
            f.is_contract_student = m.is_contract_student


    # MySQL -> Oracle
    for m in session_mysql.query(MySQLPerson).all():
        f = session_oracle.query(FinalPerson).filter_by(id=m.id).first()
        if f is None:
            # Информации нет, создаём
            f = FinalPerson()
            f.id = m.id
            f.name = m.name
            f.position = m.position
            session_oracle.add(f)
        else:
            # Если не заполнено, заполняем
            if f.position is None:
                f.position = m.position

    session_oracle.commit()
    print('ОК')

    print('Миграция данных о конференциях...', end='')
    sys.stdout.flush()

    for c in session_mysql.query(MySQLConference).all():
        f = FinalConference()
        f.id = c.id
        f.name = c.name
        f.place = c.place
        f.date = c.date
        for p in c.participants:
            f.participants.append(session_oracle.query(FinalPerson).filter_by(id=p.id).first())
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')

    print('Миграция данных о дисциплинах...', end='')
    sys.stdout.flush()

    # Postgres -> Oracle
    for p in session_postgres.query(PostgreDiscipline).all():
        f = FinalDiscipline()
        f.university_name = p.university_name
        f.standard = p.standard
        f.name = p.name
        f.faculty = p.faculty
        f.specialty = p.specialty
        f.term = p.term
        f.lecture_hours = p.lecture_hours
        f.practice_hours = p.practice_hours
        f.laboratory_hours = p.laboratory_hours
        f.is_exam = p.is_exam
        session_oracle.add(f)

    # Oracle -> Oracle
    for r in session_oracle.query(OracleRating).all():
        f = session_oracle.query(FinalDiscipline).filter_by(name=r.discipline).first()
        if f is None:
            f = FinalDiscipline()
            f.name = r.discipline
            session_oracle.add(f)

    session_oracle.commit()
    print('ОК')

    print('Миграция данных об общежитиях...', end='')
    sys.stdout.flush()

    # Mongo -> Oracle
    for d in MongoDormitory.objects():
        f = FinalDormitory()
        f.name = d.name
        f.total_rooms = d.total_rooms
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')

    print('Миграция данных о комнатах в общежитиях...', end='')
    sys.stdout.flush()

    # Mongo -> Oracle
    for r in MongoRoom.objects():
        f = FinalRoom()
        f.room_number = r.room_number
        f.insects = r.insects
        f.max_person = r.max_person
        f.latest_debug = r.latest_debug
        f.dormitory = session_oracle.query(FinalDormitory).filter_by(name=r.dormitory.name, total_rooms=r.dormitory.total_rooms).first()
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')
    
    print('Миграция данных о жителях общежитий...', end='')
    sys.stdout.flush()

    # Mongo -> Oracle
    for p in MongoDormitoryPerson.objects():
        f = FinalDormitoryPerson()
        f.warnings = p.warnings
        f.room = session_oracle.query(FinalRoom).filter_by(room_number=p.room.room_number, max_person=p.room.max_person).first()
        f.price = p.price
        f.lives_from = p.lives_from
        f.lives_to = p.lives_to
        f.person = session_oracle.query(FinalPerson).filter_by(id=p.person.person_id).first()
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')

    print('Миграция данных о группах...', end='')
    sys.stdout.flush()
    
    # Oracle -> Oracle
    for g in session_oracle.query(OracleGroup).all():
        f = FinalGroup()
        f.id = g.id
        f.name = g.name
        f.study_type = g.study_type
        f.school = g.school
        f.direction = g.direction
        f.speciality = g.speciality
        f.qualification = g.qualification
        f.study_year = g.study_year
        for s in g.students:
            f.students.append(session_oracle.query(FinalPerson).filter_by(id=s.id).first())
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')
    
    print('Миграция раписания...', end='')
    sys.stdout.flush()
    
    # Oracle -> Oracle
    for r in session_oracle.query(OracleLessonRecord).all():
        f = FinalLessonRecord()
        f.name = r.name
        f.teacher_id = r.teacher_id
        f.weekday = r.weekday
        f.hour = r.hour
        f.minute = r.minute
        f.room = r.room
        for g in r.groups:
            f.groups.append(session_oracle.query(FinalGroup).filter_by(id=g.id).first())
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')
    
    print('Миграция читательского листа...', end='')
    sys.stdout.flush()

    # MySQL -> Oracle
    for r in session_mysql.query(MySQLLibRecord).all():
        f = FinalLibRecord()
        f.book_name = r.book_name
        f.taken_by_id = r.taken_by_id
        f.taken_at = r.taken_at
        f.returned_at = r.returned_at
        session_oracle.add(f)
    
    session_oracle.commit()
    print('ОК')

    print('Миграция проектов...', end='')
    sys.stdout.flush()

    for r in session_mysql.query(MySQLProject).all():
        f = FinalProject()
        f.name = r.name
        f.date_from = r.date_from
        f.date_to = r.date_to
        for p in r.participants:
            f.participants.append(session_oracle.query(FinalPerson).filter_by(id=p.id).first())
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')

    print('Миграция публикаций...', end='')
    sys.stdout.flush()

    for r in session_mysql.query(MySQLPublication).all():
        f = FinalPublication()
        f.name = r.name
        f.language = r.language
        f.country = r.country
        f.country_id = r.country_id
        f.city = r.city
        f.city_id = r.city_id
        f.office = r.office
        f.office_id = r.office_id
        f.type = r.type
        f.quote_index = r.quote_index
        f.date = r.date
        for p in r.authors:
            f.authors.append(session_oracle.query(FinalPerson).filter_by(id=p.id).first())
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')

    print('Миграция оценок...', end='')
    sys.stdout.flush()

    # Postgres -> Oracle
    for r in session_postgres.query(PostgresRating).all():
        f = FinalRating()
        f.discipline_id = r.discipline_id
        f.rating = r.rating
        if f.rating == '5':
            f.rating_letter = 'A'
        elif f.rating == '4':
            f.rating_letter = 'B'
        elif f.rating == '3':
            f.rating_letter = 'D'
        else:
            f.rating_letter = 'FX'
        f.date = r.date
        f.teacher_id = r.teacher_id
        f.student_id = r.student_id
        session_oracle.add(f)

    # Oracle -> Oracle
    for r in session_oracle.query(OracleRating).all():
        f = FinalRating()
        f.discipline_id = session_oracle.query(FinalDiscipline).filter_by(name=r.discipline).first().id
        f.rating = r.rating
        f.rating_letter = r.rating_letter
        f.date = r.date
        f.student_id = r.student_id
        session_oracle.add(f)

    session_oracle.commit()
    print('ОК')