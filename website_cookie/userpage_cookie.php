<?php
setcookie ("PHPSESSID", "", time() - 3600, '/');
session_start();
$conn = mysqli_connect("localhost", "quentin", "quentin", "db_web");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

if(isset($_COOKIE['user_id'])) {
    $encoded_username = $_COOKIE['user_id'];
    $decoded_username = base64_decode($encoded_username);
    $username = str_replace("v4er9ll1!ss", "", $decoded_username);
    $query = "SELECT * FROM users WHERE username = '$username'";
    $result = mysqli_query($conn, $query);

    if (mysqli_num_rows($result) == true) {
        $row = mysqli_fetch_assoc($result);
        $user_id = $row['id'];
        $password = $row['password'];

    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Information</title>
</head>
<body>
    <h1>User Information</h1>
    <p>id: <?php echo $user_id; ?></p>
    <p>username: <?php echo $username; ?></p>
    <p>password: <?php echo $password; ?></p>
    <button onclick="showCookies()">Show cookies</button>
    <a href="login_cookie.php">Logout</a>
</body>
</html>