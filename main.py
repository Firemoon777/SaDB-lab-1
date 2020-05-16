from db import init_sql_engines, init_mongo_engine, check_connection

if __name__ == '__main__':
    init_sql_engines()
    init_mongo_engine()

    check_connection()
