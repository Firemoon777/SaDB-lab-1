# Хранилища и базы данных

## Подготовка сервера

### Docker

https://docs.docker.com/engine/install/ubuntu/

### Oracle DB 

1. Скачать докер-образ https://yadi.sk/d/9nOqNSKgoRV5bA
1. Распаковать `unzip oracle_with_olaptrain.zip`
1. `docker load -i oracle_with_olaptrain.tar`
1. `docker run --name oracle -d -p 0.0.0.0:1521:1521 oracle_with_olaptrain`
1. `docker exec -ti -u oracle oracle bash`
1. В шелле делаем `sqlplus sys as sysdba@PDB1;`, пароль пустой. Затем выполняем последовательность команд:
```
shutdown;
startup;
ALTER PLUGGABLE DATABASE ALL OPEN;

alter session set container=pdb1;
create user lab_oracle_user identified by lab_oracle_user_password;
GRANT CONNECT,RESOURCE,DBA TO lab_oracle_user;
GRANT CREATE SESSION, GRANT ANY PRIVILEGE TO lab_oracle_user;
GRANT UNLIMITED TABLESPACE TO lab_oracle_user;

exit;
```
1. Выходим из шелла, Oracle DB готов и доступен на порту 1521.

### MySQL

1. `docker pull mysql`
1. `docker run --name mysql -e MYSQL_ROOT_PASSWORD=superstr0ngpassword -e MYSQL_USER=lab_mysql_user -e MYSQL_PASSWORD=lab_mysql_user_password -e MYSQL_DATABASE=lab -d -p 0.0.0.0:3306:3306 mysql`

Если контейнер тут же завершается, нужно подкрутить настройки у хоста: `sysctl -w fs.aio-max-nr=2097152`

### PostgreSQL

1. `docker pull postgres`
1. `docker run --name postgres -e POSTGRES_USER=lab_postgre_user -e POSTGRES_PASSWORD=lab_postgre_user_password -d -p 0.0.0.0:5432:5432 postgres:11`


### MongoDB

1. `docker pull mongo`
1. `docker run --name mongodb -e MONGO_INITDB_DATABASE=lab -e MONGO_INITDB_ROOT_USERNAME=lab_mongo_user -e MONGO_INITDB_ROOT_PASSWORD=lab_mongo_user_password -d -p 0.0.0.0:27017:27017 mongo`

## Подготовка клиента

1. Устанавливаем Python 3.6.x
2. Устанавливаем все пакеты из requirements.txt
3. Для Оракла накатываем библиотеки [по ссылке](https://oracle.github.io/odpi/doc/installation.html#oracle-instant-client-zip)
4. Для MySQL и PostgreSQL могут потребоваться дополнительные пакеты из пакетного менеджера вашей ОС

## Запуск

### Задание 1

Задание заключается в создании схемы в 4 БД и заполнении каждой БД своими данными. В `model/<database>` можно посмотреть объекты для конкретной базы данных.

Запуск из корня проекта: 
```
/usr/bin/python3 -m lab1 create
```

Повторный запуск удвоит количество записей во всех БД. Количество генерируемых записей можно изменять в функциях `fill_<database>` в `generator/<database>.py`

### Задание 2

Необходимо провести миграцию из четырёх БД в единую схему в Oracle DB. Объекты схемы можно найти в `model/final`.

Запуск из корня проекта: 
```
/usr/bin/python3 -m lab1 migrate
```

### Задание 3

Необходимо получить из БД пару отчётов с помощью Oracle Analytic Workspace Manager.
Скачиваем [отсюда](https://www.oracle.com/database/technologies/olap-downloads.html) версию `for Oracle 12.1.0.2`.
Распаковываем, запускаем:
```
java -mx1024m -Duser.country=us -Duser.language=en -jar awm12.1.0.1.0B.jar
```

Подключаемся к нашей БД, создаём рабочее место аналитика. В качестве более подробного туториала можно опираться на [туториал от Оракла](https://www.oracle.com/ocom/groups/public/@otn/documents/webcontent/453094.htm).

#### Величины (Dimensions)

Элементы или объекты в логической схеме. В данном задании они заданы преподавателем и обозначены в [файле](./res/er-rus for awm.pdf). В нашем случае их четыре:

- место рождения (`birth_place`)
- место публикации (`publication_place`)
- время (`time`)
- общежитие (`dormitory`)

#### Уровни (Levels) и иерархии (Hierarchy)

Все данные можно группировать по различным критериям. Если грубо, то уровни и есть эти самые критерии. 
Проще всего это понять по времени. Данные со временем можно группировать по дням, неделям, месяцам, кварталам, года, etc. 
"День", "Неделя", "Месяц" -- это уровни
Последовательность "День -> Неделя -> Месяц" -- это иерархия, где "день" -- это наиболее низкий уровень, а "месяц" -- наиболее высокий.

Уровни и их иерархии так же заданы в [файле](./res/er-rus for awm.pdf). 

Вот они, для каждой величины от высокого к низкому уровню:
- место рождения (`birth_place`) 
    - все страны (`all_countries`)
    - страна (`country`)
    - город (`city`)
    - район (`district`)
- место публикации (`publication_place`)
    - все страны (`all_countries`)
    - страна (`country`)
    - город (`city`)
    - издание (`office`)
- время (`study_time`)
    - год (`year`)
    - семестр (`term`)
- общежитие (`dormitory`)
    - адрес (`address`)

#### Кубы

Кубы -- это представления данных на базе величин. Создаём куб `LAB_CUBE` и добавляем в него все величины.
