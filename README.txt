Pre-Reqs
    GnuCash
    Python
    A MariaDB or MySql (local or somewhere you have db create perms on )

    Note, on a Centos server with mysql added during the install process all I had to do was
        yum install epel-release
        yum install gnucash
        yum install libdbi-dbd-mysql
    I'm pretty sure that gnucash ships with the python bindings these days but your mileage may vary


1. Create a user and test database
Modify the username, database, and password if you like.
You'll have to update the connection string in scripts to reflect your password at least
    create database gnucash;
    create user 'gnucash'@'localhost' IDENTIFIED BY 'yourPasswordHere';
    grant ALL privileges on gnucash.* to 'gnucash'@'localhost';

2. Restore the test data into the database
This can be done any time you want to reset.  It will automatically drop existing tables and recreate
    mysql gnucash -u gnucash -p < devdata.sql

3. Run the test script to verify connection
    edit test-connection.py

The best way to learn about the python bindings are to look at the example scripts at http://svn.gnucash.org/trac/browser/gnucash/trunk/src/optional/python-bindings/example_scripts
  
