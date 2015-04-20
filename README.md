<h3>Pre-Reqs</h3>

- GnuCash
- Python
- A MariaDB or MySql (local or somewhere you have db create perms on )

<h3>Setup</h3>

Note, on a Centos server with mysql added during the install process all I had to do was:

    yum install epel-release
    yum install gnucash
    yum install libdbi-dbd-mysql
        
I'm pretty sure that gnucash ships with the python bindings these days, but your mileage may vary.
    
On a Ubuntu distribution, try:
    
    sudo apt-get install mysql-server
    sudo apt-get install gnucash
    sudo apt-get install python-gnucash
    sudo apt-get install libdbd-mysql
    
<h3>Local Testing</h3>

1. Create a user and test database.
(Modify the username, database, and password if you like.)
        mysql -u root
        create database gnucash;
        create user 'gnucash'@'localhost' IDENTIFIED BY 'yourPasswordHere';
        grant ALL privileges on gnucash.* to 'gnucash'@'localhost';
You'll have to update the connection string in scripts to reflect your password if you are connecting to the Denhac server.
2. Restore the test data into the database.
This can be done any time you want to reset.  It will automatically drop existing tables and recreate the test setup.
        mysql gnucash -u gnucash -p < path_to_devdata.sql;
3. Run the test script to verify connection.
        edit test-connection.py
    
<h3>Sources</h3>
    
The best way to learn about the python bindings are to look at the example scripts at http://svn.gnucash.org/trac/browser/gnucash/trunk/src/optional/python-bindings/example_scripts
  
