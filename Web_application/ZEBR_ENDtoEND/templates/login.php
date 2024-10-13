<?php
//login.php
    include('connection.php');
    if (isset($_POST['submit'])) {
        $username = $_POST['user'];
        $password = $_POST['pass'];
    
        // Use prepared statements to prevent SQL injection
        $stmt = $conn->prepare("SELECT * FROM login WHERE username = ? AND password = ?");
        $stmt->bind_param("ss", $username, $password);
        $stmt->execute();
        $result = $stmt->get_result();
        $count = $result->num_rows;
    
        if($count == 1){  
            header("Location: welcom.php");
        } else {  
            echo '<script>
                      window.location.href = "index.php";
                      alert("Login failed. Invalid username or password!!")
                  </script>';
        }  
    }
    
    ?>