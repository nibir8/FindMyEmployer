
DROP PROCEDURE IF EXISTS spUpdatePassword;


CREATE PROCEDURE spUpdatePassword
(
newpassword varchar(50),
userid integer
)
update tbl_users set password = newpassword
where userid = userid
