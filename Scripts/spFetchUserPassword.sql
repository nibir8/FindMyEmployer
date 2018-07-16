
DROP PROCEDURE IF EXISTS spFetchUserPassword;



CREATE PROCEDURE spFetchUserPassword
(
 email varchar(50)
 )
 Select userid,password from tbl_users where  email = email
