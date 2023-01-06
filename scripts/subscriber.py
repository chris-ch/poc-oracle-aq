from time import sleep

import oracledb
import os
import sys
import json
import logging


def process_messages(message):
    logging.warning('received message {}'.format(message))


def main(queue_name, subscriber_name):
    oracledb.init_oracle_client(lib_dir='../lib/instantclient_19_8')
    username = os.environ.get('ORACLE_USERNAME')
    password = os.environ.get('ORACLE_PASSWORD')
    connect_string = os.environ.get('ORACLE_CONNECT_STRING')
    with oracledb.connect(user=username, password=password, dsn=connect_string, events=True) as connection:
        queue = connection.queue(queue_name)
        queue.deqoptions.wait = oracledb.DEQ_WAIT_FOREVER
        queue.deqoptions.navigation = oracledb.DEQ_FIRST_MSG
        queue.deqoptions.visibility = oracledb.DEQ_IMMEDIATE
        with connection.cursor() as _:
            queue.deqoptions.consumername = subscriber_name
            while True:
                message = queue.deqone()
                logging.info('received message: {}'.format(message.payload.decode()))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    if len(sys.argv) != 3:
        logging.error('expected arguments: <queue name> <subscriber id>')
        sys.exit(-1)

    try:
        main(sys.argv[1], sys.argv[2])

    except KeyboardInterrupt:
        print('Goodbye!')
