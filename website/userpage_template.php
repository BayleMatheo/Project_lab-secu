<?php
session_start();
?>

</head>
<body>
        <h1>User Information</h1>
        <p>id: <?php echo $_SESSION['id']; ?></p>
        <p>username: <?php echo $_SESSION['username']; ?></p>
        <p>password: <?php echo $_SESSION['password']; ?></p>
        <a href="login.php">Logout</a>
</body>
</html>