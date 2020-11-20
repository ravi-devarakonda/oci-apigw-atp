#!/bin/sh
l_output=`sqlplus -s ADBUSER/Adb__Ex4d4t4@blkatp_low<<EOF
set serveroutput on;
set feedback off;
DECLARE
 sql_stmt VARCHAR2(250);
 sql_output employees%ROWTYPE;
BEGIN
 sql_stmt := 'select * from employees where empname=''sid''';
 execute immediate sql_stmt into sql_output;
 dbms_output.put_line('Employee Name :' || sql_output.empname);
dbms_output.put_line('Employee ID: '||sql_output.empid);
end;
/
exit
EOF
`
echo $l_output