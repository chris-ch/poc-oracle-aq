import oracledb
import os


def main(name):
    username = os.environ.get('PYTHON_USERNAME')
    password = os.environ.get('PYTHON_PASSWORD')
    connect_string = os.environ.get('PYTHON_CONNECTSTRING')
    with oracledb.connect(user=username, password=password, dsn=connect_string) as connection:
        with connection.cursor() as cursor:
            sql = """select sysdate from dual"""
            for r in cursor.execute(sql):
                print(r)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
