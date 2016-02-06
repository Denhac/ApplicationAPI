USE memberdb;

CREATE TABLE IF NOT EXISTS member (
	id				int(11) auto_increment not null primary key,
	lastName		varchar(50),
	firstName		varchar(50),
	middleInitial	varchar(1),
	birthdate		date,
	streetAddress1	varchar(50),
	streetAddress2	varchar(50),
	city			varchar(20),
	zipCode			varchar(9),
	email			varchar(50),
	phoneNumber		varchar(50),
	businessNumber	varchar(50),
	emerContact1	varchar(50),
	emerPhone1		varchar(50),
	emerAddress1	varchar(50),
	emerRelation1	varchar(50),
	emerContact2	varchar(50),
	emerPhone2		varchar(50),
	emerAddress2	varchar(50),
	emerRelation2	varchar(50),
	medicalConditionList	varchar(1024),
	gnuCashId		varchar(6),
	paymentAmount	float,
	active			tinyint(1) not null default 1,
	onAutoPay		tinyint(1) not null default 0,
	isManager		tinyint(1) not null default 0,
	isAdmin			tinyint(1) not null default 0,
	ad_username		varchar(20),
	contact_email	varchar(100),
	paypal_email	varchar(100)
);

CREATE INDEX member_ad_username_idx  ON member(ad_username);
CREATE INDEX member_paypal_email_idx ON member(paypal_email);

CREATE TABLE IF NOT EXISTS invoice (
	id				int(11) auto_increment not null primary key,
	member_id		int(11) not null,
	invoice_date	datetime not null,
	amount			float not null,
	notes			varchar(255),
	FOREIGN KEY (member_id) REFERENCES member(id)
);

ALTER TABLE invoice auto_increment = 100;

CREATE TABLE IF NOT EXISTS payment_type (
	id				int(11) auto_increment not null primary key,
	description		varchar(20) not null
);

CREATE TABLE IF NOT EXISTS payment (
	id				int(11) auto_increment not null primary key,
	member_id		int(11) not null,
	payment_date	datetime not null,
	amount			float not null,
	payment_type_id	int(11) not null,
	notes			varchar(255),
	FOREIGN KEY (member_id) REFERENCES member(id),
	FOREIGN KEY (payment_type_id) REFERENCES payment_type(id)
);

ALTER TABLE payment auto_increment = 100;

INSERT INTO payment_type
	SELECT 1,'Cash' UNION ALL
	SELECT 2,'Check' UNION ALL
	SELECT 3,'PayPal' UNION ALL
	SELECT 4,'Credit Card' UNION ALL
	SELECT 5,'Bitcoin' UNION ALL
	SELECT 6,'Money Order';
