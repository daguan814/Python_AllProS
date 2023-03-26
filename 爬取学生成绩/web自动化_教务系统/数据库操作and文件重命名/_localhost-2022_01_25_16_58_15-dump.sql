-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (arm64)
--
-- Host: 127.0.0.1    Database: 学生信息
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `class3`
--

DROP TABLE IF EXISTS `class3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class3` (
  `Number` char(10) NOT NULL,
  `Name` char(10) DEFAULT NULL,
  `bool` int DEFAULT NULL,
  `password` char(16) DEFAULT NULL,
  PRIMARY KEY (`Number`),
  UNIQUE KEY `19513003_Number_uindex` (`Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class3`
--

LOCK TABLES `class3` WRITE;
/*!40000 ALTER TABLE `class3` DISABLE KEYS */;
INSERT INTO `class3` VALUES ('1951300401','1951300401',NULL,'1951300401\r'),('1951300402','1951300402',NULL,'1951300402\r'),('1951300403','1951300403',NULL,'1951300403\r'),('1951300404','1951300404',NULL,'1951300404\r'),('1951300405','1951300405',1,'1951300405\r'),('1951300406','1951300406',NULL,'1951300406\r'),('1951300407','1951300407',NULL,'1951300407\r'),('1951300408','1951300408',NULL,'1951300408\r'),('1951300409','1951300409',NULL,'1951300409\r'),('1951300410','1951300410',NULL,'1951300410\r'),('1951300411','1951300411',NULL,'1951300411\r'),('1951300412','1951300412',NULL,'1951300412\r'),('1951300413','1951300413',NULL,'1951300413\r'),('1951300414','1951300414',NULL,'1951300414\r'),('1951300415','1951300415',NULL,'1951300415\r'),('1951300416','1951300416',NULL,'1951300416\r'),('1951300417','1951300417',NULL,'1951300417\r'),('1951300418','1951300418',NULL,'1951300418\r'),('1951300419','1951300419',NULL,'1951300419\r'),('1951300420','1951300420',NULL,'1951300420\r'),('1951300421','1951300421',NULL,'1951300421\r'),('1951300422','1951300422',NULL,'1951300422\r'),('1951300423','1951300423',1,'1951300423\r'),('1951300424','1951300424',1,'1951300424\r'),('1951300425','1951300425',NULL,'1951300425\r'),('1951300426','1951300426',NULL,'1951300426\r'),('1951300427','1951300427',NULL,'1951300427\r'),('1951300428','1951300428',NULL,'1951300428\r'),('1951300429','1951300429',NULL,'1951300429\r'),('1951300430','1951300430',NULL,'1951300430\r'),('1951300431','1951300431',NULL,'1951300431\r'),('1951300432','1951300432',1,'1951300432\r'),('1951300433','1951300433',NULL,'1951300433\r'),('1951300434','1951300434',1,'1951300434\r'),('1951300435','1951300435',NULL,'1951300435\r'),('1951300436','1951300436',1,'1951300436\r'),('1951300437','1951300437',NULL,'1951300437');
/*!40000 ALTER TABLE `class3` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-25 16:58:15
