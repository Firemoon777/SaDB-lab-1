import os

from .model import init_sql_engines, init_mongo_engine, check_connection, databases
from .model.mongo import *

if __name__ == '__main__':
    os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'

    init_sql_engines()
    init_mongo_engine()

    check_connection()

    from lab1.model.postgres import create_schema as postgres_create_schema
    from .generator.postgres import fill_postgres
    postgres_create_schema(databases['postgres']['engine'])
    fill_postgres()

    # from lab1.model.mysql import create_schema as mysql_create_schema
    # mysql_create_schema(databases['mysql']['engine'])

    from lab1.model.oracle import create_schema as oracle_create_schema
    from .generator.oracle import fill_oracle
    oracle_create_schema(databases['oracle']['engine'])
    fill_oracle()
