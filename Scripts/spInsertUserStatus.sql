
DROP PROCEDURE IF EXISTS spInsertUserStatus;

DELIMITER $$
CREATE PROCEDURE spInsertUserStatus ( myemail varchar(50), user_status varchar(500))
BEGIN

DECLARE myuserid INTEGER;
DECLARE myfirstname varchar(50);
DECLARE mylastname varchar(50);

Select @myuserid := userid , @myfirstname := firstname , @mylastname := lastname   From tbl_users where email = myemail;


INSERT INTO
  tbl_user_status (email, userstatus, userId,firstname,lastname)
values
  (
    myemail,
    user_status,
    @myuserid,
    @myfirstname,
    @mylastname
  ) ;
  END$$
DELIMITER ;
