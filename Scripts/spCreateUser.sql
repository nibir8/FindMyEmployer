
DROP PROCEDURE IF EXISTS spCreateUser;

CREATE PROCEDURE spCreateUser
(
 Password_given varchar(50),
 email varchar(50),
 firstname varchar(50),
 lastname varchar(50),
 address1 varchar(50),
 address2 varchar(50),
 zipcode varchar(50),
 city varchar(50),
 state varchar(50),
 country varchar(50),
 phone varchar(50)
 )
INSERT INTO tbl_users (password, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone)
VALUES
(Password_given, email, firstname , lastname, address1,address2 ,zipcode ,city ,state,country,phone)
