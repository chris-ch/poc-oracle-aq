grant execute on dbms_aq to scott;
grant execute on dbms_aqadm to scott;
grant execute on dbms_aqin to scott;

EXEC dbms_aqadm.create_queue_table('POCQUEUETABLE', 'SYS.AQ$_JMS_TEXT_MESSAGE')
EXEC dbms_aqadm.create_queue('POCQUEUE','POCQUEUETABLE')
EXEC dbms_aqadm.start_queue('POCQUEUE')
set serverout on

DECLARE
enqueue_options DBMS_AQ.ENQUEUE_OPTIONS_T;
message_properties DBMS_AQ.MESSAGE_PROPERTIES_T;
message_handle RAW (16);
msg SYS.AQ$_JMS_TEXT_MESSAGE;
BEGIN
msg := SYS.AQ$_JMS_TEXT_MESSAGE.construct;
msg.set_text('Hello, PLSQL World!');
DBMS_AQ.ENQUEUE (
queue_name => 'POCQUEUE',
enqueue_options => enqueue_options,
message_properties => message_properties,
payload => msg,
msgid => message_handle);
COMMIT;
END;
/
