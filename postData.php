<?php

$data = json_decode(file_get_contents('php://input'), true);
print_r($data);

$variant = $data["variant"];
$clickedYes = $data["clickedYes"];

print($variant);
print($clickedYes);


$servername = "localhost";
$username = "root";
$password = "Bk&=kw/gH3rY";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

$sql = "INSERT INTO ab_test (variant, clickedYes)
VALUES ($variant, $clickedYes)";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
