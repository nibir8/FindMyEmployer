
DROP PROCEDURE IF EXISTS spGetAllUsers;

CREATE PROCEDURE spGetAllUsers
 (
 )
 Select email,password from tbl_users
