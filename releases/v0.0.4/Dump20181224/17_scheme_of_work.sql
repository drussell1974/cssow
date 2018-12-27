-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cssow
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sow_scheme_of_work`
--

DROP TABLE IF EXISTS `sow_scheme_of_work`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sow_scheme_of_work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `description` text,
  `key_stage_id` int(11) NOT NULL,
  `exam_board_id` int(11) DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) unsigned NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `sow_scheme_of_work__has__key_stage` (`key_stage_id`),
  KEY `sow_scheme_of_work__has__year` (`exam_board_id`),
  CONSTRAINT `sow_scheme_of_work__has__key_stage` FOREIGN KEY (`key_stage_id`) REFERENCES `sow_key_stage` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sow_scheme_of_work__has__year` FOREIGN KEY (`exam_board_id`) REFERENCES `sow_exam_board` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sow_scheme_of_work`
--

LOCK TABLES `sow_scheme_of_work` WRITE;
/*!40000 ALTER TABLE `sow_scheme_of_work` DISABLE KEYS */;
INSERT INTO `sow_scheme_of_work` VALUES (11,'A-Level Computer Science','Computing curriculum for A-Level\r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n\r\n',5,3,'0000-00-00 00:00:00',1,1),(58,'test','\r\n                \r\n\r\n',4,NULL,'2018-12-22 13:26:04',1,1),(61,'GCSE Computer Science','                    \r\n                ',4,NULL,'2018-12-23 04:05:29',1,1),(69,'Test with exam','                                                                                                                                                                                                                                                                                                            \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                \r\n                ',1,2,'2018-12-23 04:37:51',1,1),(71,'Test create exam','                                                                                                    \r\n                \r\n                \r\n                \r\n                \r\n                ',1,2,'2018-12-23 05:44:44',1,1),(72,'Test create exam','                    \r\n                ',1,2,'2018-12-23 05:45:05',1,1),(75,'GCSE Computer Science','\r\n',4,NULL,'2018-12-24 05:15:33',1,1);
/*!40000 ALTER TABLE `sow_scheme_of_work` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-24  5:33:04
