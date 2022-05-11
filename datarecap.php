<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8" content="5">
    <title>Data Recapitulation</title>
    <link rel="stylesheet" href="assets/css/datastyle.css">
  </head>
  <body align="center">
    <div id="page_header">
      <div id="back" class="tooltip">
        <a href="https://faisalsyamsuri13.github.io/supremeproject"><img class="icon" src="assets/images/home_icon.png" alt="home_icon.png" width="20px" height="20px"></a>
        <span class="tooltiptext">Home</span>
      </div>
      <div id="search"></div>
      <div id="searchby" align="left"></div>
    </div>
    <div id="container">
      <?php
        $servername = "localhost";
        $username = "pma";
        $password = "RIVeMKSn4[/Os7(1";
        $dbname = "raspi_database";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sql = "SELECT id, sensor, location, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, reading_time FROM as7341_sensor_data /*new_data*/ ORDER BY id DESC"; /*select items to display from the sensordata table in the data base*/

        echo '<table cellspacing="4" cellpadding="4" align=center>
              <tr>
                <th class="hid">ID</th>
                <th class="hid">Date | Time</th>
                <th class="hid">Sensor</th>
                <th class="hid">Location</th>
                <th class="hid">Data 1</th>
                <th class="hid">Data 2</th>
                <th class="hid">Data 3</th>
                <th class="hid">Data 4</th>
                <th class="hid">Data 5</th>
                <th class="hid">Data 6</th>
                <th class="hid">Data 7</th>
                <th class="hid">Data 8</th>
                <th class="hid">Data 9</th>
                <th class="hid">Data 10</th>
                <th class="hid">Link</th>
              </tr>';

        if ($result = $conn->query($sql)) {
            while ($row = $result->fetch_assoc()) {
                $row_id = $row["id"];
                $row_reading_time = $row["reading_time"];
                $row_sensor = $row["sensor"];
                $row_location = $row["location"];
                $row_value1 = $row["value1"];
                $row_value2 = $row["value2"];
                $row_value3 = $row["value3"];
                $row_value4 = $row["value4"];
                $row_value5 = $row["value5"];
                $row_value6 = $row["value6"];
                $row_value7 = $row["value7"];
                $row_value8 = $row["value8"];
                $row_value9 = $row["value9"];
                $row_value10 = $row["value10"];
                $link = '<a href="preview.php?id=' . $row["id"] . '">Preview</a>';

                // Uncomment to set timezone to - 1 hour (you can change 1 to any number)
               // $row_reading_time = date("Y-m-d H:i:s", strtotime("$row_reading_time - 1 hours"));

                // Uncomment to set timezone to + 4 hours (you can change 4 to any number)
                //$row_reading_time = date("Y-m-d H:i:s", strtotime("$row_reading_time + 4 hours"));

                echo '<tr>
                        <td>' . $row_id . '</td>
                        <td>' . $row_reading_time . '</td>
                        <td>' . $row_sensor . '</td>
                        <td>' . $row_location . '</td>
                        <td>' . $row_value1 . '</td>
                        <td>' . $row_value2 . '</td>
                        <td>' . $row_value3 . '</td>
                        <td>' . $row_value4 . '</td>
                        <td>' . $row_value5 . '</td>
                        <td>' . $row_value6 . '</td>
                        <td>' . $row_value7 . '</td>
                        <td>' . $row_value8 . '</td>
                        <td>' . $row_value9 . '</td>
                        <td>' . $row_value10 . '</td>
                        <td>' . $link . '</td>
                      </tr>';
            }
            $result->free();
        }

        echo'</table>';

        $conn->close();
      ?>
    </div>
    <script type="text/javascript" src="assets/js/search.js"></script>
    <div id="footer">
      <p class="one" align=center>
          &copy; 2022 President University. All rights reserved. <a href="https://faisalsyamsuri13.github.io/supremeproject">Home</a> | <a href="https://faisalsyamsuri13.github.io/supremeproject/about.html">About</a> |
          <a href="https://faisalsyamsuri13.github.io/supremeproject/contactus.html">Contact Us</a>
      </p>
    </div>
  </body>
</html>
