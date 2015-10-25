# Tasks

1. Gnucash: Export/Import Dev Database
	http://denhac.org/wiki/index.php?title=Infrastructure [10.0.101.247 MariaDB]
	Python into Gnucash C API only via MariaDB (not XML)

2. API Endpoint for Authentication
	Linked to Active Directory
	Static Website to send JSON
	Send back true/false

3. Webform for creating new member to talk to API
	Transmit and store data in the database 

# Requirements/Features

## Must Have

- Staff roles can collect payments
	Roles in the database for members (Active Directory)
	Denhac’s LDAP server only used for authentication
- Staff can create a new member
- User can authenticate on website
	Session management in python web framework
	Login screen
- Member can make a payment
- Member can view balance

## Nice to Have
- Payments not automated or mapped back to members
	PayPal, BitPay, Wallet
	Issue: email for payment may not match email in database

## Later
- Create queue of pending transactions
	Gnucash is single-user; locks up database

