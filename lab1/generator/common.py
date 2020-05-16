import random

__names_male = [
    "Александр",
    "Алексей",
    "Андрей",
    "Артем",
    "Виктор",
    "Даниил",
    "Дмитрий",
    "Егор",
    "Илья",
    "Кирилл",
    "Максим",
    "Марк",
    "Михаил",
    "Роман",
    "Степан",
    "Тимофей",
    "Ярослав"
]

__names_female = [
    "Александра",
    "Алиса",
    "Анастасия",
    "Анна",
    "Арина",
    "Валерия",
    "Варвара",
    "Вероника",
    "Виктория",
    "Дарья",
    "Ева",
    "Екатерина",
    "Елизавета",
    "Кира",
    "Маргарита",
    "Мария",
    "Полина",
    "София",
    "Таисия",
    "Ульяна"
]

__surnames = [
    "Смирнов",
    "Иванов",
    "Кузнецов",
    "Соколов",
    "Попов",
    "Лебедев",
    "Козлов",
    "Новиков",
    "Морозов",
    "Петров",
    "Волков",
    "Соловьёв",
    "Васильев",
    "Зайцев",
    "Павлов",
    "Семёнов",
    "Голубев",
    "Виноградов",
    "Богданов",
    "Воробьёв",
    "Фёдоров",
    "Михайлов",
    "Беляев",
    "Тарасов",
    "Белов"
]

def generate_name():
    sex = random.randrange(2)
    if sex == 1:
        return random.choice(__surnames) + " " + random.choice(__names_male)
    else:
        return random.choice(__surnames) + "а " + random.choice(__names_female)


def generate_term():
    return random.randrange(8)


__universities = [
    'Университет ИТМО'
]


def generate_university():
    return random.choice(__universities)


def generate_hours():
    return random.randrange(100, 200)


__disciplines = [
    "Компьютерная графика (2018449043-И)",
    "Технологии веб-сервисов",
    "Системное и прикладное ПО",
    "Языки системного программирования",
    "Программирование",
    "Системы управления базами данных"
]


def generate_discipline():
    return random.choice(__disciplines)


__standards = [
    "новый",
    "старый"
]


def generate_standard():
    return random.choice(__standards)


__facultes = [
    "ФПИиКТ",
    "ФИТИП"
]


def generate_faculty():
    return random.choice(__facultes)


__specialty = [
    "09.01.02 – Магия вне Хогвартса",
    "01.02.03 – Тёмные искусства Дурмстранга"
]


def generate_specialty():
    return random.choice(__specialty)


def generate_position():
    return random.choice([
        "студент бакалавриата", "студент магистратуры", "доцент"
    ])


def generate_conference():
    return random.choice([
        "КМУ", "Майоровские чтения"
    ])


def generate_publication_type():
    return random.choice([
        "статья", "тезисы"
    ])


def generate_language():
    return random.choice([
        "русский", "Английский"
    ])


def generate_source():
    return random.choice([
        "Москва", "Тверь", "Санкт-Петербург", "Челябинск"
    ])


def generate_source_type():
    return random.choice([
        "ВАК", "РИНЦ"
    ])


def generate_group():
    return random.choice([
        "P3110",
        "P3210",
        "P3310",
        "P3410",
        "P4114",
        "P3111",
        "P3211",
        "P3311",
        "P3411",
        "P4116",
        "P41142",
    ])


def generate_qualification():
    return random.choice([
        "бакалавр", "магистр"
    ])


def generate_dormatory():
    return random.choice([
        "Вяземский пер., 3А",
        "Белорусская ул., 6"
    ])


def generate_is_exam():
    return random.randrange(2)


def generate_rating():
    letter = random.choice([
        'A', 'B', 'C', 'D', 'E', 'FX', 'F'
    ])
    if letter == 'A':
        number = 5
    elif letter == 'B' or letter == 'C':
        number = 4
    elif letter == 'D' or letter == 'E':
        number = 3
    else:
        number = 2
    return number, letter


def generate_person_id():
    return random.randrange(100000, 400000)


def generate_place():
    return random.choice([
        "Москва", "Санкт-Петербург", "Новосибирск", "Хабаровск", "Южно-Сахалинск", "Сочи"
    ])