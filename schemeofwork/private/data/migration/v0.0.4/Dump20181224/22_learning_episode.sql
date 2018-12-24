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
-- Table structure for table `sow_learning_episode`
--

DROP TABLE IF EXISTS `sow_learning_episode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sow_learning_episode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_of_delivery_id` int(11) DEFAULT NULL,
  `scheme_of_work_id` int(11) DEFAULT NULL,
  `topic_id` int(11) DEFAULT '76',
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) unsigned NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `scheme_of_work_id__idx` (`scheme_of_work_id`),
  KEY `sow_learning_episode_has_topic_id` (`topic_id`),
  CONSTRAINT `sow_learning_episode_has_topic_id` FOREIGN KEY (`topic_id`) REFERENCES `sow_topic` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sow_learning_episode_ibfk_1` FOREIGN KEY (`scheme_of_work_id`) REFERENCES `sow_scheme_of_work` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sow_learning_episode`
--

LOCK TABLES `sow_learning_episode` WRITE;
/*!40000 ALTER TABLE `sow_learning_episode` DISABLE KEYS */;
INSERT INTO `sow_learning_episode` VALUES (30,2,11,73,'2018-12-18 10:08:27',1,1),(35,1,11,13,'2018-12-21 15:44:24',1,1),(46,1,75,36,'2018-12-24 05:15:56',1,1);
/*!40000 ALTER TABLE `sow_learning_episode` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-24  5:33:05
