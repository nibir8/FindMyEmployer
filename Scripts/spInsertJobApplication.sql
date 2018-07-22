DROP PROCEDURE IF EXISTS spInsertJobApplication;

CREATE PROCEDURE spInsertJobApplication
	(
     email varchar(50)
	 )
  INSERT into tbl_JobsApplication(email)
  VALUES (email)
