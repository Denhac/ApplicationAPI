DATE=`date +%Y-%m-%d`

mysqldump --add-drop-database --add-drop-table --host 10.0.101.111 --routines --user denhac --password --databases memberdb > memberdb_$DATE.sql
