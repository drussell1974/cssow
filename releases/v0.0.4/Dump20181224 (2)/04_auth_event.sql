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
-- Table structure for table `auth_event`
--

DROP TABLE IF EXISTS `auth_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_stamp` datetime DEFAULT NULL,
  `client_ip` varchar(512) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `origin` varchar(512) DEFAULT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  KEY `user_id__idx` (`user_id`),
  CONSTRAINT `auth_event_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_event`
--

LOCK TABLES `auth_event` WRITE;
/*!40000 ALTER TABLE `auth_event` DISABLE KEYS */;
INSERT INTO `auth_event` VALUES (1,'2018-12-16 15:06:46','127.0.0.1',NULL,'auth','Group 1 created'),(2,'2018-12-16 15:06:46','127.0.0.1',1,'auth','User 1 Registered'),(3,'2018-12-16 15:06:59','127.0.0.1',1,'auth','User 1 Profile updated'),(4,'2018-12-16 15:11:57','127.0.0.1',1,'auth','User 1 Logged-out'),(5,'2018-12-16 15:12:13','127.0.0.1',1,'auth','User 1 Logged-in'),(6,'2018-12-16 15:12:27','127.0.0.1',1,'auth','User 1 Logged-out'),(7,'2018-12-16 15:13:27','127.0.0.1',NULL,'auth','User 1 Password reset'),(8,'2018-12-16 17:03:16','127.0.0.1',1,'auth','User 1 Logged-in'),(9,'2018-12-17 02:59:49','127.0.0.1',1,'auth','User 1 Logged-out'),(10,'2018-12-17 03:00:18','127.0.0.1',1,'auth','User 1 Logged-in'),(11,'2018-12-17 06:18:50','127.0.0.1',1,'auth','User 1 Logged-in'),(12,'2018-12-17 06:29:49','127.0.0.1',1,'auth','User 1 Logged-out'),(13,'2018-12-17 06:31:45','127.0.0.1',1,'auth','User 1 Logged-in'),(14,'2018-12-18 04:19:06','127.0.0.1',1,'auth','User 1 Logged-in'),(15,'2018-12-18 07:24:12','127.0.0.1',1,'auth','User 1 Logged-out'),(16,'2018-12-18 07:24:43','127.0.0.1',1,'auth','User 1 Logged-in'),(17,'2018-12-19 08:50:19','127.0.0.1',1,'auth','User 1 Logged-in'),(18,'2018-12-19 09:04:41','127.0.0.1',1,'auth','User 1 Logged-in'),(19,'2018-12-19 09:23:04','127.0.0.1',1,'auth','User 1 Logged-in'),(20,'2018-12-20 04:34:04','127.0.0.1',1,'auth','User 1 Logged-in'),(21,'2018-12-20 18:13:41','127.0.0.1',1,'auth','User 1 Logged-in'),(22,'2018-12-21 02:55:16','127.0.0.1',1,'auth','User 1 Logged-in'),(23,'2018-12-21 12:46:28','127.0.0.1',1,'auth','User 1 Logged-in'),(24,'2018-12-21 18:41:52','127.0.0.1',1,'auth','User 1 Logged-in'),(25,'2018-12-22 02:49:52','127.0.0.1',1,'auth','User 1 Logged-in'),(26,'2018-12-22 05:58:00','127.0.0.1',1,'auth','User 1 Logged-in'),(27,'2018-12-22 07:10:16','127.0.0.1',1,'auth','User 1 Logged-in'),(28,'2018-12-22 07:36:57','127.0.0.1',1,'auth','User 1 Logged-in'),(29,'2018-12-22 12:18:49','127.0.0.1',1,'auth','User 1 Logged-in'),(30,'2018-12-22 13:06:22','127.0.0.1',1,'auth','User 1 Logged-in'),(31,'2018-12-23 03:09:16','127.0.0.1',1,'auth','User 1 Logged-in'),(32,'2018-12-23 08:54:53','127.0.0.1',1,'auth','User 1 Logged-in'),(33,'2018-12-23 16:21:08','127.0.0.1',1,'auth','User 1 Logged-in'),(34,'2018-12-23 17:58:19','127.0.0.1',1,'auth','User 1 Logged-in'),(35,'2018-12-24 03:35:04','127.0.0.1',1,'auth','User 1 Logged-in'),(36,'2018-12-24 05:13:50','127.0.0.1',1,'auth','User 1 Logged-in');
/*!40000 ALTER TABLE `auth_event` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-24  6:01:19
