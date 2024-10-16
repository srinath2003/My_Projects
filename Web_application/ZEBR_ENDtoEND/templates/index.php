<?php
 include("connection.php")
 //index.php
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Surveillance App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50;
            padding: 20;
            background-image: url('image1.jpeg');
            background-size: cover;
            background-position: center;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Makes the body take up the full height of the viewport */
            flex-direction: column;
        }
        h1  {
            font-size: 50px;
            text-shadow: 3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000; /* Creates a black border effect */
            margin: 5px 0;
        }
        h2 {
            font-size: 40px;
            text-shadow: 1px 1px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000; /* Creates a black border effect */
            margin: 5px 0;
            color: #007bff;
        }
        #imageContainer {
            margin: 20px auto;
            width: 300px; /* Set the width of the image container */
            height: 200px;
        }
        #imageContainer img {
            width: 100%;
            height: auto; /* Ensure the image scales within the container */
            border-radius: 10px; /* Optional: Adds rounded corners to the image */
        }
        .login-signup {
    margin-top: 20px;
    font-size: 20px;
    margin: 0 auto;
}

        button {
            padding: 10px 20px;
            margin: 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #007bff;
            border: none;
            color: #fff;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #c75818;
        }

        .username{
            padding: 8px 0px;
        }
    </style>
</head>
<body>

   <h1>Surveillance App</h1>

  

   <div id="forms">
    <form id="form" action="login.php" method="POST">
        <h2>Welcome Back !</h2>
        <label for="username">Username:</label>
        <input type="text" id="user" name="user" placeholder="Enter your username" required>
        
        <label for="password">Password:</label>
        <input type="password" id="pass" name="pass" placeholder="Enter your password" required>
        
        <button type="submit" name="submit">Login</button>

        
        <button type="button" onclick="location.href='welcom.php'">Sign Up</button>
    </form>
    
</div>

</body>
</html>
