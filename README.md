# Proof-of-Concept for Oracle Advanced Queuing

## Installation

**MacOs specifics**
```shell
podman machine stop || true
podman machine rm || true
podman machine init --cpus=2 --memory=4096 -v $HOME:$HOME -v /private/tmp:/private/tmp -v /var/folders/:/var/folders/
sed -i '' 's/security_model=mapped-xattr/security_model=none/' $(podman machine inspect | jq --raw-output '.[0].ConfigPath.Path')
podman machine start
```

Pulling an Oracle Database image first:

`> podman pull container-registry.oracle.com/database/enterprise:19.3.0.0`

Starting a container:

`> podman run -d -it --name oracle -p 1521:1521 -v config/sqlnet.ora:/opt/oracle/oradata/dbconfig/ORCLCDB/sqlnet.ora container-registry.oracle.com/database/enterprise:19.3.0.0`

Starting a shell within the container:

`> podman exec -it 49c5cab40014 /bin/bash`

Database setup (thanks to https://github.com/monodot/oracle-aq-demo):

```SQL
sqlplus / as sysdba

alter session set "_ORACLE_SCRIPT"=true;
create user scott identified by tiger;
grant dba to scott;
```

Setting up the Oracle AQ queues (thanks to https://laurentschneider.com/wordpress/2013/09/advanced-queuing-hello-world.html):

```SQL
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

select owner, table_name from dba_all_tables where table_name = 'QT';
select owner, table_name from dba_all_tables where table_name = 'POCQUEUETABLE';
```
