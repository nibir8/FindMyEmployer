DROP PROCEDURE IF EXISTS spInsertJobDetails;

CREATE PROCEDURE spInsertJobDetails
	(
	 jobId integer,
	 companyName varchar(50),
     title varchar(50),
     manager varchar(50),
     location varchar(50),
     jobDetails varchar(50),
		 myemail varchar(50)
	 )
  INSERT into tbl_Jobs(jobId,companyName,title,manager,location,jobDetails,emailid)
  VALUES (jobId,companyName,title,manager,location,jobDetails,myemail)
