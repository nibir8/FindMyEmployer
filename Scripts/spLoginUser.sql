DROP PROCEDURE IF EXISTS spLoginUser;

CREATE PROCEDURE spLoginUser
(
email varchar(50)
)
Select userid,firstname from tbl_users where  email = email
