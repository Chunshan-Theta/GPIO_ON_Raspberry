-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'GPIORecord'
-- 
-- ---

DROP TABLE IF EXISTS `GPIORecord`;
		
CREATE TABLE `GPIORecord` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `Pin_Id` INTEGER NULL DEFAULT NULL,
  `User_Id` VARBINARY(10) NOT NULL,
  `cmd` VARCHAR(200) NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'User'
-- 
-- ---

DROP TABLE IF EXISTS `User`;
		
CREATE TABLE `User` (
  `User_Id` VARBINARY(10) NULL DEFAULT NULL,
  `Name` VARCHAR(10) NULL DEFAULT NULL,
  `mail` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`User_Id`)
);

-- ---
-- Table 'DeviceData'
-- 
-- ---

DROP TABLE IF EXISTS `DeviceData`;
		
CREATE TABLE `DeviceData` (
  `Pin_id` INTEGER NULL DEFAULT NULL,
  `cost` INTEGER NULL DEFAULT NULL,
  `Name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`Pin_id`)
);

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `GPIORecord` ADD FOREIGN KEY (Pin_Id) REFERENCES `DeviceData` (`Pin_id`);
ALTER TABLE `GPIORecord` ADD FOREIGN KEY (User_Id) REFERENCES `User` (`User_Id`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `GPIORecord` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `User` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `DeviceData` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `GPIORecord` (`id`,`Pin_Id`,`User_Id`,`cmd`) VALUES
-- ('','','','');
-- INSERT INTO `User` (`User_Id`,`Name`,`mail`) VALUES
-- ('','','');
-- INSERT INTO `DeviceData` (`Pin_id`,`cost`,`Name`) VALUES
-- ('','','');
