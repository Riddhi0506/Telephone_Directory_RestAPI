-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: telephonedirectory
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `telephonedirectory`
--

DROP TABLE IF EXISTS `telephonedirectory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `telephonedirectory` (
  `ID` int NOT NULL,
  `NAME` text NOT NULL,
  `PHONENUMBER` text NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telephonedirectory`
--

LOCK TABLES `telephonedirectory` WRITE;
/*!40000 ALTER TABLE `telephonedirectory` DISABLE KEYS */;
INSERT INTO `telephonedirectory` VALUES (1,'Bruce Schneier','(703)111-2121'),(2,'Schneier, Bruce Wayne','+32 (21) 212-2324'),(3,'John O\'Malley-Smith','011 1 703 111 1234'),(7,'Schneier, Bruce Wayne','123-1234'),(9,'Schneier, John','1(703)123-1234'),(11,'Joe Belle','12345.12345'),(13,'Ron Yarpeys','(221) 212-2324'),(14,'Samuel Samuel','+01 (703) 123-1234'),(17,'Ron Barnes','326718.12837'),(18,'Everett Samuel','+45 (211) 212-2324'),(24,'Samuel Samuel','011 1 703 111 1234'),(28,'Cherey','1(703)123-1234'),(29,'Chereyl','011 701 111 1234'),(30,'Chereylph','1234.1234'),(31,'Chey','011 701 111 1234'),(32,'Chewyku','011 1 703 111 1234'),(33,'Yen Kul','1(703)123-1234'),(34,'Yen lie','+32 (21) 212-2324'),(35,'Fungiie ','+1(703)111-2121'),(36,'Kapil dev','123-1234'),(37,'David','21215'),(38,'David','111-2121'),(39,'Kung Fu','1234.12345'),(40,'Hundar','01 122 233 1294');
/*!40000 ALTER TABLE `telephonedirectory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-22 15:45:45
