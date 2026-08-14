-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Users`
-- Создат таблицу пользователей в базе данных
-- Содержит поля: id, ФИО, пароль
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Users` (
  `user_id` INT NOT NULL,
  `fio` VARCHAR(60) NOT NULL,
  `pass` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Lung_Cancer_Risk_and_Prediction_Dataset`
-- Создат таблицу показаний пациента в базе данных
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Lung_Cancer_Risk_and_Prediction_Dataset` (
  `id_patient` INT NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `age` VARCHAR(45) NOT NULL,
  `gender` VARCHAR(45) NOT NULL,
  `smoking_status` VARCHAR(45) NOT NULL,
  `second_hand_smoke` VARCHAR(45) NOT NULL,
  `air_pollution_exposure` VARCHAR(45) NOT NULL,
  `occupation_exposure` VARCHAR(45) NOT NULL,
  `rural_or_urban` VARCHAR(45) NOT NULL,
  `socioeconomic_status` VARCHAR(45) NOT NULL,
  `healthcare_access` VARCHAR(45) NOT NULL,
  `insurance_coverage` VARCHAR(45) NOT NULL,
  `screening_availability` VARCHAR(45) NOT NULL,
  `stage_at_diagnosis` VARCHAR(45) NOT NULL,
  `cancer_type` VARCHAR(45) NOT NULL,
  `mutation_type` VARCHAR(45) NOT NULL,
  `treatment_access` VARCHAR(45) NOT NULL,
  `clinical_trial_access` VARCHAR(45) NOT NULL,
  `language_barrier` VARCHAR(45) NOT NULL,
  `mortality_risk` DOUBLE NOT NULL,
  `5_year_survival_probability` DOUBLE NOT NULL,
  `delay_in_diagnosis` VARCHAR(45) NOT NULL,
  `family_history` VARCHAR(45) NOT NULL,
  `indoor_smoke_exposure` VARCHAR(45) NOT NULL,
  `tobacco_marketing_exposure` VARCHAR(45) NOT NULL,
  `final_prediction` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_patient`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;




select * from Users;
select * from Lung_Cancer_Risk_and_Prediction_Dataset;




# drop table Users;



#----------------------------------------

# Процедура создания новой записи пользователя
DROP PROCEDURE IF EXISTS AddUser;
DELIMITER //
CREATE PROCEDURE AddUser(
  IN p_fio VARCHAR(60),
  IN p_password VARCHAR(45)
)
BEGIN
  DECLARE v_next_id INT;
  SELECT IFNULL(MAX(user_id), 0) + 1 INTO v_next_id FROM mydb.Users;
  INSERT INTO mydb.Users (user_id, pass, fio)
  VALUES (user_id, p_password, p_fio);
END
// DELIMITER ;

select * from Users;













