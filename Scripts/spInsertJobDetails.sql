DROP PROCEDURE IF EXISTS spInsertJobDetails;

CREATE PROCEDURE spInsertJobDetails
	(
	 companyName varchar(50),
     title varchar(50),
     manager varchar(50),
     location varchar(50),
     jobDetails varchar(50)
	 )
  INSERT into tbl_Jobs(companyName,title,manager,location,jobDetails)
  VALUES (companyName,title,manager,location,jobDetails)
