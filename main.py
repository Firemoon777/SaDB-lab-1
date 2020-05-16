from sqlalchemy import create_engine
from configparser import ConfigParser

databases = {}


def init_engines():
    config = ConfigParser()
    config.read('db.cfg')

    for s in config.sections():
        try:
            proto = config[s]['proto']
            url = config[s]['url']
            username = config[s]['username']
            password = config[s]['password']
        except KeyError:
            continue

        databases[s] = {
            'engine': create_engine(
                f'{proto}://{username}:{password}@{url}'
            )
        }

        print(f'Подключение к {s} инициализировано')


if __name__ == '__main__':
    init_engines()

    print(databases['oracle']['engine'].execute("select 'Hello, World!' from DUAL").scalar())
    print(databases['postgres']['engine'].execute("select 'Hello, World!'").scalar())
    print(databases['mysql']['engine'].execute("select 'Hello, World!'").scalar())