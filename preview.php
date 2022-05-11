<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Specified Result</title>
    <link rel="stylesheet" href="assets/css/datastyle.css">
    <script type="text/javascript" src="assets/js/jquery.min.js"></script>
    <script type="text/javascript" src="assets/js/qrcode.js"></script>
    <script type="text/javascript" src="assets/js/FileSaver.min.js"></script>
  </head>
  <body align="center">
    <div id="page_header">
      <div id="home" class="tooltip">
        <a href="https://faisalsyamsuri13.github.io/supremeproject"><img class="icon" src="assets/images/home_icon.png" alt="home_icon.png"></a>
        <span class="tooltiptext">Home</span>
      </div>
      <div id="back" class="tooltip">
        <a href="datarecap.php"><img class="icon" src="assets/images/back_icon.png" alt="back_icon.png"></a>
        <span class="tooltiptext">Back</span>
      </div>
      <div id="print" class="tooltip">
        <a href=""><img class="icon" src="assets/images/print_icon.png" alt="print_icon.png"></a>
        <span class="tooltiptext">Print</span>
      </div>
      <div id="generate" class="tooltip">
        <a href="javascript:void(0)" onclick="javascript:makeCode()"><img class="icon" src="assets/images/qr_icon.png" alt="qr_icon.png"></a>
        <span class="tooltiptext">Generate</span>
      </div>
    </div>
    <div id="container">
    <?php
      $servername = "localhost";
      $username = "pma";
      $password = "RIVeMKSn4[/Os7(1";
      $dbname = "nodemcu_database_v2";

      $conn = new mysqli($servername, $username, $password, $dbname);
      if($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
      }

      $index = $_GET["id"];

      $sql = "SELECT id, sensor, location, value1, value2, /*value3,*/ reading_time FROM sensor_data WHERE id = {$index}";

      echo '<table cellspacing="4" cellpadding="4" align=center>
            <tr>
              <th>ID</th>
              <th>Date | Time</th>
              <th>Sensor</th>
              <th>Location</th>
              <th>Temperature &deg;C</th>
              <th>Humidity &#37;</th>
            </tr>';

      if($result = $conn->query($sql)) {
        while($row = $result->fetch_assoc()) {
          $row_id = $row["id"];
          $row_reading_time = $row["reading_time"];
          $row_sensor = $row["sensor"];
          $row_location = $row["location"];
          $row_value1 = $row["value1"];
          $row_value2 = $row["value2"];
          /*$row_value3 = $row["value3"];*/

          echo '<tr>
                  <td>' . $row_id . '</td>
                  <td>' . $row_reading_time . '</td>
                  <td>' . $row_sensor . '</td>
                  <td>' . $row_location . '</td>
                  <td>' . $row_value1 . '</td>
                  <td>' . $row_value2 . '</td>
                </tr>';
        }
        $result->free();
      }
      echo '</table>';

      $conn->close();

     ?>
     <input id="url" type="hidden"></input>
     <div id="qrcode"></div>
     <button>Download</button>
     <script type="text/javascript" src="assets/js/generate.js"></script>
     <script type="text/javascript" src="assets/js/download.js"></script>
   </div>
   <div id="footer">
     <p class="one" align=center>
         &copy; 2022 President University. All rights reserved. <a href="https://faisalsyamsuri13.github.io/supremeproject">Home</a> | <a href="https://faisalsyamsuri13.github.io/supremeproject/about.html">About</a> |
         <a href="https://faisalsyamsuri13.github.io/supremeproject/contactus.html">Contact Us</a>
     </p>
   </div>
  </body>
</html>