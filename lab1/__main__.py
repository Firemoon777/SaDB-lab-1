from .model import init_sql_engines, init_mongo_engine, check_connection, databases
from .model.mongo import *

if __name__ == '__main__':
    init_sql_engines()
    init_mongo_engine()

    check_connection()

    from lab1.model.postgres import create_schema as postgres_create_schema
    postgres_create_schema(databases['postgres']['engine'])

    from .generator.postgres import fill_postgres
    fill_postgres()

    from lab1.model.mysql import create_schema as mysql_create_schema
    mysql_create_schema(databases['mysql']['engine'])

    from lab1.model.oracle import create_schema as oracle_create_schema
    oracle_create_schema(databases['oracle']['engine'])
