<?php

$servername = "localhost";
$username = "root";
$password = "Bk&=kw/gH3rY";
$database = "team_02";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$query = "SELECT * FROM `ab_test`";

if ($result = $conn->query($query)) {

    $newArr = array();
    while ($db_field = mysqli_fetch_assoc($result)) {
        $newArr[] = $db_field;
    }
    echo json_encode($newArr); // get all rows in json format.
}
?>
