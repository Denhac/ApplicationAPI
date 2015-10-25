drop database if exists gnucash;
create database gnucash;
grant usage on *.* to 'gnucash'@'localhost';
drop user 'gnucash'@'localhost';
create user 'gnucash'@'localhost' identified by 'password';
grant all privileges on gnucash.* to 'gnucash'@'localhost';

drop database if exists denhac;
create database denhac;
grant usage on *.* to 'denhac'@'localhost';
drop user 'denhac'@'localhost';
create user 'denhac'@'localhost' identified by 'password';
grant all privileges on denhac.* to 'denhac'@'localhost';
