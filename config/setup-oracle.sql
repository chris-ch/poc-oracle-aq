ALTER SESSION SET "_ORACLE_SCRIPT"=true;
CREATE USER SCOTT IDENTIFIED BY tiger;
GRANT dba TO scott;
GRANT EXECUTE ON dbms_aq TO scott;
GRANT EXECUTE ON dbms_aqadm TO scott;
GRANT EXECUTE ON dbms_aqin TO scott;
GRANT CREATE SESSION TO scott;
ALTER USER scott QUOTA UNLIMITED ON USERS;
ALTER USER scott IDENTIFIED BY tiger ACCOUNT UNLOCK;
ALTER SYSTEM DISABLE RESTRICTED SESSION;
QUIT
