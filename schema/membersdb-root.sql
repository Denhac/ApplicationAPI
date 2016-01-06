CREATE DATABASE memberdb;
CREATE USER 'denhac'@'%' identified by 'password';
GRANT ALL on memberdb.* to 'denhac'@'%' identified by 'password';
