<?php
setcookie ("PHPSESSID", "", time() - 3600, '/');
// Connexion à la base de données
$conn = mysqli_connect("localhost", "quentin", "quentin", "db_web");
session_start();

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Vérification des identifiants de connexion
if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $pass = md5($_POST['password']);

    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$pass'";
    $result = mysqli_query($conn, $query);

    if (mysqli_num_rows($result) == true) {
        $row = mysqli_fetch_assoc($result);
        $username = $row['username'];
        $encoded_username = base64_encode($username . "v4er9ll1!ss");
        setcookie('user_id', $encoded_username, time() + (86400 * 30), '/', '', false, false);
        header("Location: userpage.php");
        exit;
    } else {
        // Affichage d'un message d'erreur en cas d'identifiants incorrects
        $error_message = "Nom d'utilisateur ou mot de passe incorrect";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>register form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="form-container">

    <form action="" method="post">
        <h3>Login</h3>
        <?php
        // Affichage du message d'erreur si nécessaire
        if (isset($error_message)) {
            echo "<p style='color:red;'>$error_message</p>";
        }
        ?>
        <input type="username" name="username" required placeholder="enter your username">
        <input type="password" name="password" required placeholder="enter your password">
        <input type="submit" value="Connexion">
        <p> don't have an account? <a href="register.php">register now</a></p>
    </form>
</body>
</html>

<?php
mysqli_close($conn);
?>