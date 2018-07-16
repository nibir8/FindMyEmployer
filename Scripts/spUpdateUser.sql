
drop procedure spUpdateUser

CREATE PROCEDURE spUpdateUser
(
 myemail varchar(50),
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
 update tbl_users
 set firstname = firstname,
 lastname = lastname,
 address1 = address1,
 address2 = address2,
 zipcode = zipcode,
 city = city,
 state = state,
 country = country,
 phone = phone
 where  email = myemail
