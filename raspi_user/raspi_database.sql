CREATE DATABASE `raspi_database`;
CREATE TABLE `as7341_sensor_data` (
  `id` int(6) AUTO_INCREMENT PRIMARY KEY,
  `sensor` varchar(30) NOT NULL,
  `location` varchar(30) NOT NULL,
  `value1` varchar(10),
  `value2` varchar(10),
  `value3` varchar(10),
  `value4` varchar(10),
  `value5` varchar(10),
  `value6` varchar(10),
  `value7` varchar(10),
  `value8` varchar(10),
  `value9` varchar(10),
  `value10` varchar(10),
  `reading_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
