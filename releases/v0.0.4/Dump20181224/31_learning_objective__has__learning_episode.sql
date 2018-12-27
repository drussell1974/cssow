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
-- Table structure for table `sow_learning_objective__has__learning_episode`
--

DROP TABLE IF EXISTS `sow_learning_objective__has__learning_episode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sow_learning_objective__has__learning_episode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `learning_objective_id` int(11) DEFAULT NULL,
  `learning_episode_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sow_learning_episode__unique__idx` (`learning_objective_id`,`learning_episode_id`),
  KEY `learning_objective_id__idx` (`learning_objective_id`),
  KEY `learning_episode_id__idx` (`learning_episode_id`),
  CONSTRAINT `sow_learning_objective__has__learning_episode_ibfk_1` FOREIGN KEY (`learning_objective_id`) REFERENCES `sow_learning_objective` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sow_learning_objective__has__learning_episode_ibfk_2` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sow_learning_objective__has__learning_episode`
--

LOCK TABLES `sow_learning_objective__has__learning_episode` WRITE;
/*!40000 ALTER TABLE `sow_learning_objective__has__learning_episode` DISABLE KEYS */;
INSERT INTO `sow_learning_objective__has__learning_episode` VALUES (59,395,35),(60,405,35),(58,410,35);
/*!40000 ALTER TABLE `sow_learning_objective__has__learning_episode` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-24  5:33:03
