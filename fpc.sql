/*
SQLyog Job Agent Version 10.0 Beta1 Copyright(c) Webyog Inc. All Rights Reserved.


MySQL - 5.5.5-10.4.14-MariaDB : Database - finalproject
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`finalproject` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `finalproject`;

/*Table structure for table `doctordata` */

DROP TABLE IF EXISTS `doctordata`;

CREATE TABLE `doctordata` (
  `docname` varchar(100) DEFAULT NULL,
  `specialist` varchar(100) DEFAULT NULL,
  `sittinghours` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `days` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `fees` varchar(100) DEFAULT NULL,
  `Experience` varchar(100) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `doctordata` */

insert  into `doctordata` values ('Dr. Aklish Jain','Dermatologist','10AM-7PM','DADABARI, KOTA','M,T,W,F,S,S','aklishjain@gmail.com','400','12yrs',NULL),('Dr. Amit Dev','Neurologist','10AM-8PM','V-MART','All days','amitdev@gmail.com','500','15yrs',NULL),('Dr. Anshul mohan mathur','Dentist','10AM-7PM','Talwandi','All days','anshulmathur@gmail.com','400','25yrs',NULL),('Dr. B.C TELUNG','GENERAL PHYSICIAN','10AM-8PM','DADABARI, KOTA','M,W,F,S,S','bctelung@gmail.com','200','25yrs',NULL),('Dr. Bhanwar Ranwa','cardiaologist','10AM-7PM','Kota Medical college','M,W,F,S,S','bhanwarranwa@gmial.com','500','23',NULL),('Dr. S.N Soni','Orthopedic','10AM-7PM','Talwandi,','All days','chanddni@gmail.com','400','18yrs',NULL),('Dr. Dinesh bindal','cardiaologist','10AM-8PM','DADABARI, KOTA','M,W,F,S,S','dineshbindal@gmail.com','400','32yrs',NULL),('Dr. gaurav rohagtgi','Orthopedic','10AM-7PM','Maheveer Nagar','All days','gauravrohatgi75@gmail.com','500','17yrs',NULL),('Dr Imran khan','ENT specialist','10AM-8PM','Vighyan nagar','all days','imrankhan@gmail.com','500','16yrs',NULL),('Dr. Jasvinder Singh','GENERAL PHYSICIAN','10AM-7PM','DADABARI, KOTA','All days','jasvindersingh@gmail.com','500','15yrs',NULL),('Dr. Kunal Mittal','GENERAL PHYSICIAN','10AM-8PM','GUMANPURA,KOTA HEALTH CARE','M,T,W,T,F,S','kunalmittal34@gmail.com','150','8yrs',NULL),('Dr.Mahesh Punjabi','ENT specialist','10AM-8PM','CAD Circle,Kota','M,W,F,S,S','maheshpunjabi@gmail.com','500','37yrs',NULL),('Dr. Pankaj khandelwal','Dermatologist','10AM-7PM','Maheveer Nagar','All days','pankajsharma75@gmail.com','200','19yrs',NULL),('Dr. Prasant Singhvi','Neurologist','10AM-7PM','Talwandi,sector-c','All days','prashantsinghvi@gmail.com','400','17yrs',NULL),('Dr. Puja sharma','Dermatologist','10AM-8PM','Talwandi,TT hospital','All days','pujasharma@gmail.com','400','12yrs',NULL),('Dr. Purshottam mittal','cardiaologist','10AM-7PM','Talwandi,jhalawar road','All days','purshottammittal@gmail.com','400','16yrs',NULL),('Dr. R.P Sharma','GENERAL PHYSICIAN','10AM-7PM','Talwandi,TT hospital','M,W,F,S,S','rpsharma@gmail.com','400','43yrs',NULL),('Dr. Saket goyal','cardiaologist','10AM-7PM','Talwandi,TT hospital','All days','saketgoyal76@gmail.com','500','12yrs',NULL),('Dr. Salil Mittal','Dermatologist','10AM-8PM','DADABARI, KOTA','M,W,F,S,S','salilmittal@gmail.com','200','27yrs',NULL),('Dr. Sandeep Singh','Dentist','10AM-9PM','Talwandi','All days','sandeepsingh@gmail.com','200','12yrs',NULL),('ladli mohan kansal','Dermatologist','10AM-8PM','jothwara','M,W,F,S,S','sharma75@gmail.com','400','12yrs','BKK.jpg'),('Dr. Shewta Singhwi','Dentist','10AM-8PM','DADABARI, KOTA','M,T,W,F,S,','shewtasinghwi@gmail.com','300','16yrs',NULL),('Dr. Suresh pandey','ENT specialist','10AM-7PM','suvi netra eye','All days','sureshkpandey@gmail.com','400','12yrs','BKK.jpg'),('Dr .TANMAY SHARMA','Orthopedic','10AM-7PM','Talwandi,TT hospital','All days','tanmaysharma@gmail.com','500','21yrs',NULL),('Dr. vijay sardana','Neurologist','10AM-8PM','Kota Medical college','All days','vijaysardana@gmial.com','400','12yrs',NULL),('Dr. Vikrant sharma','ENT specialist','10AM-7PM','Talwandi,anandam ENT hospital','All days','vikrantmathur@gmail.com','400','25yrs',NULL),('Dr. Zia Rehman khan','GENERAL PHYSICIAN','10AM-7PM','Kotari,gordhanpura','M,T,W,F,S,S','ziarehman22@gmail.com','100','5yrs',NULL);

/*Table structure for table `finalproject` */

DROP TABLE IF EXISTS `finalproject`;

CREATE TABLE `finalproject` (
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `confirm password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `finalproject` */

insert  into `finalproject` values ('ayushkhandelwal75@gmail.com','ayush@123','ayush@123','admin'),('bhanukhandelwal75@gmail.com','bhanu@123','bhanu@123','doctor'),('jayeshsharma75@gmail.com','jayesh@123','jayesh@123','patient'),('prakash@gmail.com','prakash@123','prakash@123','reception');

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `name` varchar(100) DEFAULT NULL,
  `mobno` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `symptoms` varchar(100) DEFAULT NULL,
  `appointmentdate` varchar(100) DEFAULT NULL,
  `slot` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `patient` */

insert  into `patient` values ('adi','AA','A','ajayevgan123@gmail.com','diabetes','2021-01-28','6:PM'),('mahesh','9413734941','DADABARI, KOTA','jasvinder@gmail.com','obesity','2021-01-27','6:PM'),('adi','9413734941','DADABARI, KOTA','jasvinderkor@gmail.com','headache','2021-01-29','5:PM'),('adi','9413734941','DADABARI, KOTA','jasvinr@gmail.com','headache','2021-01-29','5:PM'),('ambika','99898090878','DADABARI, KOTA','kasliwal@gmail.com','cough','2021-01-28','6:PM'),('bhanu','9413734941','Maheveer Nagar','pankajsharma75@gmail.com','cough','2021-01-28','7:PM'),('bhanu','9413734941','Maheveer Nagar','pankjsharma75@gmail.com','cough','2021-01-28','7:PM'),('D','X','Maheveer Nagar','pjsharma75@gmail.com','cough','','Time'),('bhanu','9413734941','Maheveer Nagar','X@gmail.com','cough','2021-01-28','7:PM');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
