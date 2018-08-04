
DROP PROCEDURE IF EXISTS spGetUserDetails;

 CREATE PROCEDURE spGetUserDetails
 (
  email varchar(50)
  )
  Select userid,firstname,typeOfUser from tbl_users where  email = email
