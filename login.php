<?php
include 'config.php';
include 'loginvalidate.php';
include 'error.php';
?>

<!DOCTYPE html>
<html>
<head>
<title>Login</title>
<link rel="stylesheet" href="style.css">
<style>

</style>
</head>
<body style="background-color:black">

	<div id="wrap">
		<center>
			<h1>Enter your credentials!!!!</h1>
		</center>

	<form action="login.php" method="post">
		<label> <b>Username:</label>
		<input name="username" type="text" class="uName" placeholder="Enter your username"/><br>
		<label><b> Password:</label>
		<input name="password" type="password" class="uName" placeholder="Enter your password"/><br>
		<input name="submit" type="Submit" id="log_button" value="Login"/><br>
		<a href="index.php"><input type="button" id="back_button" value="Back"/>
	</form>
</div> 
</body>
</html>