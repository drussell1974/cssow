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
-- Table structure for table `sow_content`
--

DROP TABLE IF EXISTS `sow_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sow_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) NOT NULL,
  `letter` char(1) NOT NULL,
  `key_stage_id` int(11) NOT NULL DEFAULT '4',
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) unsigned NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_sow_content_key_stage` (`key_stage_id`),
  CONSTRAINT `fk_sow_content_key_stage` FOREIGN KEY (`key_stage_id`) REFERENCES `sow_key_stage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sow_content`
--

LOCK TABLES `sow_content` WRITE;
/*!40000 ALTER TABLE `sow_content` DISABLE KEYS */;
INSERT INTO `sow_content` VALUES (1,'standard algorithms, including binary search and merge sort','A',4,'0000-00-00 00:00:00',0,1),(2,'following and writing algorithms to solve problems, including sequence, selection and iteration, and input, processing and output','B',4,'0000-00-00 00:00:00',0,1),(3,'how particular programs and algorithms work','C',4,'0000-00-00 00:00:00',0,1),(4,'the concept of data type, including integer, Boolean, real, character and string and data structures, including records and one- and two-dimensional arrays','D',4,'0000-00-00 00:00:00',0,1),(5,'representation of numbers in binary and hexadecimal; conversion between these and decimal; binary addition and shifts','E',4,'0000-00-00 00:00:00',0,1),(6,'representation of text, sound, and graphics inside computers','F',4,'0000-00-00 00:00:00',0,1),(7,'boolean logic using AND, OR and NOT, combination of these, and the application of logical operators','G',4,'0000-00-00 00:00:00',0,1),(8,'the purpose and functionality of systems software, including the operating system and utility software','H',4,'0000-00-00 00:00:00',0,1),(9,'characteristics of systems architectures: CPU architecture, including Von Neumann and the role of components','I',4,'0000-00-00 00:00:00',0,1),(10,'characteristics of systems architectures: main and contemporary secondary storage and ways of storing data on devices including magnetic, optical and solid state','J',4,'0000-00-00 00:00:00',0,1),(11,'characteristics of systems architectures: data capacity and calculation of data capacity requirements','K',4,'0000-00-00 00:00:00',0,1),(12,'networks and the importance of: connectivity, both wired and wireless; types of networks; common network topologies; network security; protocols; layers','L',4,'0000-00-00 00:00:00',0,1),(13,'cyber security: forms of attack; methods of identifying vulnerabilities; way to protect software systems','M',4,'0000-00-00 00:00:00',0,1),(14,'the ethical, legal and environmental impacts of digital technology on wider society, including issues of privacy and cyber security','N',4,'0000-00-00 00:00:00',0,1),(15,'characteristics and purpose of different levels of programming language, including lowlevel language','O',4,'0000-00-00 00:00:00',0,1),(17,'use a keyboard and mouse effectively','A',2,'0000-00-00 00:00:00',0,1),(19,'fundamentals of programming','A',5,'0000-00-00 00:00:00',0,1),(20,'the concept of data type, including primitive data types and complex data structures','B',5,'0000-00-00 00:00:00',0,1),(21,'data representation','C',5,'0000-00-00 00:00:00',0,1),(22,'following and writing algorithms','D',5,'0000-00-00 00:00:00',0,1),(23,'methods of capturing, selecting, exchanging and managing data to produce information for a particular purpose ','E',5,'0000-00-00 00:00:00',0,1),(24,'the need for and functions of systems software ','F',5,'0000-00-00 00:00:00',0,1),(25,'characteristics of contemporary systems architectures, including processors, storage, input, output and their connectivity','G',5,'0000-00-00 00:00:00',0,1),(26,'characteristics of networks and the importance of networking protocols and standards','H',5,'0000-00-00 00:00:00',0,1),(27,'the individual moral, social ethical, legal and cultural opportunities and risks of digital technology','I',5,'0000-00-00 00:00:00',0,1);
/*!40000 ALTER TABLE `sow_content` ENABLE KEYS */;
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
