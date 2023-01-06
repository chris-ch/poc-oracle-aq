import random
from datetime import datetime, date
from json import JSONEncoder
from time import sleep

import oracledb
import os
import sys
import json
import logging


class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()


def loop(connection, queue_high, queue_low, name):
    recipients = ['Subscriber01', 'Subscriber02', 'Subscriber03']
    while True:
        pause = random.randint(10, 30)
        sleep(float(pause) / 10.)
        value = random.randint(1, 100)
        message = {'timestamp': datetime.now(), 'source': name, 'value': value}
        if value < 10:
            logging.info('sending {}'.format(message))
            queue_low.enqone(connection.msgproperties(payload=json.dumps(message, cls=DateTimeEncoder), recipients=recipients))
        elif value > 90:
            logging.info('sending {}'.format(message))
            queue_high.enqone(connection.msgproperties(payload=json.dumps(message, cls=DateTimeEncoder), recipients=recipients))

        connection.commit()


def main(name):
    oracledb.init_oracle_client(lib_dir='../lib/instantclient_19_8')
    username = os.environ.get('ORACLE_USERNAME')
    password = os.environ.get('ORACLE_PASSWORD')
    connect_string = os.environ.get('ORACLE_CONNECT_STRING')
    with oracledb.connect(user=username, password=password, dsn=connect_string) as connection:
        queue_high = connection.queue('POC_HIGH_NUMBER_QUEUE')
        queue_low = connection.queue('POC_LOW_NUMBER_QUEUE')
        loop(connection, queue_high, queue_low, name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    if len(sys.argv) != 2:
        logging.error('missing argument: source name')
        sys.exit(-1)

    try:
        main(sys.argv[1])

    except KeyboardInterrupt:
        print('Goodbye!')
