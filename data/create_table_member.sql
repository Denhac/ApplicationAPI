
drop table if exists members;
create table members 
(
	id int not null auto_increment,
	name_first varchar(255) not null,
	name_last varchar(255) not null,
	handle varchar(255),
	birthdate date,
	address varchar(255) not null,
	city varchar(255) not null,
	state varchar(255) not null,
	zip varchar(255) not null,
	email varchar(255) not null,
	phone varchar(255) not null,
	medical_conditions text,
	--businessNumber
	emergency_contact_1 varchar(255) not null,
	emergency_phone_1 varchar(255) not null,
	emergency_email_1 varchar(255) not null,
	emergency_address_1 varchar(255),
	emergency_city_1 varchar(255),
	emergency_state_1 varchar(255),
	emergency_zip_1 varchar(255),
	emergency_contact_2 varchar(255) not null,
	emergency_phone_2 varchar(255) not null,
	emergency_email_2 varchar(255) not null,
	emergency_address_2 varchar(255),
	emergency_city_2 varchar(255),
	emergency_state_2 varchar(255),
	emergency_zip_2 varchar(255),

	primary key (id)	
)
