<?php
$servername = "localhost";
$username = "pma";
$password = "RIVeMKSn4[/Os7(1";
$dbname = "raspi_database";

/*$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);*/

$api_key_value = "tPmAT5Ab3j7F9";

$api_key = $sensor = $location = $value1 = $value2 = $value3 = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $api_key = test_input($_POST["api_key"]);
    if($api_key == $api_key_value) {
        $sensor = test_input($_POST["sensor"]);
        $location = test_input($_POST["location"]);
        $value1 = test_input($_POST["value1"]);
        $value2 = test_input($_POST["value2"]);
        $value3 = test_input($_POST["value3"]);
        $value4 = test_input($_POST["value4"]);
        $value5 = test_input($_POST["value5"]);
        $value6 = test_input($_POST["value6"]);
        $value7 = test_input($_POST["value7"]);
        $value8 = test_input($_POST["value8"]);
        $value9 = test_input($_POST["value9"]);
        $value10 = test_input($_POST["value10"]);
        /*$keygen = test_input($_POST["keygen"]);
        $value11 = html_entity_decode(test_input($_POST["value3"]));*/

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sql = "INSERT INTO as7341_sensor_data (sensor, location, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10)
        VALUES ('" . $sensor . "', '" . $location . "', '" . $value1 . "', '" . $value2 . "', '" . $value3 . "','" . $value4 . "', '" . $value5 . "', '" . $value6 . "','" . $value7 . "', '" . $value8 . "', '" . $value9 . "','" . $value10 . "')";

        if ($conn->query($sql) === TRUE) {
            echo "HTTP Code Response: 200\nNew record created successfully!";
        }
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }

        $conn->close();
    }
    else {
        echo "Wrong API Key provided.";
    }

}
else {
    echo "No data posted with HTTP POST.";
}

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
