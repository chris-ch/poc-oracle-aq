EXECUTE DBMS_AQADM.create_queue_table(queue_table => 'POC_QUEUE_TABLE', queue_payload_type => 'RAW')
EXECUTE DBMS_AQADM.create_queue(queue_name => 'POC_QUEUE', queue_table => 'POC_QUEUE_TABLE')
EXECUTE DBMS_AQADM.start_queue(queue_name => 'POC_QUEUE')
QUIT
