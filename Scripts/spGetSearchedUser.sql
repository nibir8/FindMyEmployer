DROP PROCEDURE IF EXISTS spGetSearchedUser;

CREATE PROCEDURE spGetSearchedUser
	(
	 myFirstName varchar(50)
	 )
  SELECT userId, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone FROM tbl_users
  where firstName=myFirstName