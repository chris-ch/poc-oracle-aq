--
EXECUTE DBMS_AQADM.create_queue_table(queue_table => 'POC_MEASUREMENT_QUEUE_TABLE', queue_payload_type => 'RAW', multiple_consumers => true);

-- High numbers
EXECUTE DBMS_AQADM.create_queue(queue_name => 'POC_HIGH_NUMBER_QUEUE', queue_table => 'POC_MEASUREMENT_QUEUE_TABLE');

EXECUTE DBMS_AQADM.start_queue(queue_name => 'POC_HIGH_NUMBER_QUEUE');

-- Low  numbers
EXECUTE DBMS_AQADM.create_queue(queue_name => 'POC_LOW_NUMBER_QUEUE', queue_table => 'POC_MEASUREMENT_QUEUE_TABLE');

EXECUTE DBMS_AQADM.start_queue(queue_name => 'POC_LOW_NUMBER_QUEUE');

QUIT

