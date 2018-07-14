DROP PROCEDURE IF EXISTS spGetCompleteUserDetails;

CREATE PROCEDURE spGetCompleteUserDetails
	(
	 email varchar(50)
	 )
  SELECT userId, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone FROM tbl_users
  where email=email