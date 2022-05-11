CREATE DATABASE `nodemcu_database_v2`;
CREATE TABLE `sensor_data` (
  `id` int(6) AUTO_INCREMENT PRIMARY KEY,
  `sensor` varchar(30) NOT NULL,
  `location` varchar(30) NOT NULL,
  `value1` varchar(10),
  `value2` varchar(10),
  `reading_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
