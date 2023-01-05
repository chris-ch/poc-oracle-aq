import oracledb
import os


def main(name):
    oracledb.init_oracle_client(lib_dir='lib/instantclient_19_8')
    username = os.environ.get('PYTHON_USERNAME')
    password = os.environ.get('PYTHON_PASSWORD')
    connect_string = os.environ.get('PYTHON_CONNECT_STRING')
    with oracledb.connect(user=username, password=password, dsn=connect_string) as connection:
        with connection.cursor() as cursor:
            sql = """select sysdate from dual"""
            for r in cursor.execute(sql):
                print(r)

        queue = connection.queue('POC_QUEUE')
        PAYLOAD_DATA = [
            'The first message',
            'The second message',
            'The third message'
        ]
        for data in PAYLOAD_DATA:
            queue.enqone(connection.msgproperties(payload=data))
        connection.commit()


if __name__ == '__main__':
    main('PyCharm')
