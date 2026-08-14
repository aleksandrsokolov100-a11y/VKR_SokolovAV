SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

USE `mydb`;

SET GLOBAL local_infile = 1;

-- Дополнительно:
-- Что бы использовать код импорта данных, требуется сделать следующее:
-- Database -> Connect to Database -> Advenced -> ввести в поле other "OPT_LOCAL_INFILE=1" и сохранить
-- Откроется новое окно, в него скопировать код и выполнить его
-- OPT_LOCAL_INFILE=1
-- 
-- 
-- 

TRUNCATE TABLE Users;
LOAD DATA LOCAL INFILE 'C:/Users/aleks/Desktop/SQL/Data_for_SQL/Data_Users_SQL.csv'
INTO TABLE Users
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;


TRUNCATE TABLE Lung_Cancer_Risk_and_Prediction_Dataset;
LOAD DATA LOCAL INFILE 'C:/Users/aleks/Desktop/SQL/Data_for_SQL/lung_cancer_prediction_SQL.csv'
INTO TABLE Lung_Cancer_Risk_and_Prediction_Dataset
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;




select * from Lung_Cancer_Risk_and_Prediction_Dataset;
select * from Users;




SELECT user_id FROM Users WHERE fio = "F22"



