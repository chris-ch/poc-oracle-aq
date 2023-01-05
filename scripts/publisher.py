import random
from datetime import datetime
from time import sleep

import oracledb
import os
import sys
import json
import logging


def loop(connection, queue, name):
    while True:
        pause = random.randint(10, 30)
        sleep(float(pause) / 10.)
        message = {'timestamp': datetime.now(), 'source': name, 'value': random.randint(1, 100)}
        logging.info('sending {}'.format(message))
        if queue and connection:
            queue.enqone(connection.msgproperties(payload=json.dumps(message)))
            connection.commit()


def main(name):
    oracledb.init_oracle_client(lib_dir='../lib/instantclient_19_8')
    username = os.environ.get('ORACLE_USERNAME')
    password = os.environ.get('ORACLE_PASSWORD')
    connect_string = os.environ.get('ORACLE_CONNECT_STRING')
    with oracledb.connect(user=username, password=password, dsn=connect_string) as connection:
        queue = connection.queue('POC_QUEUE')
        loop(connection, queue, name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    if len(sys.argv) != 2:
        logging.error('missing argument: source name')
        sys.exit(-1)

    main(sys.argv[1])
