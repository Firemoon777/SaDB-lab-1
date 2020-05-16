from .db import init_sql_engines, init_mongo_engine, check_connection, databases

if __name__ == '__main__':
    init_sql_engines()
    init_mongo_engine()

    check_connection()

    from lab1.model.postgres import create_schema
    create_schema(databases['postgres']['engine'])