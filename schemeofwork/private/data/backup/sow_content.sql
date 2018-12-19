-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: db764008810.hosting-data.io
-- Generation Time: Dec 15, 2018 at 07:29 AM
-- Server version: 5.5.60-0+deb7u1-log
-- PHP Version: 7.0.33-0+deb9u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db764008810`
--

-- --------------------------------------------------------

--
-- Table structure for table `sow_content`
--

CREATE TABLE `sow_content` (
  `id` int(11) NOT NULL,
  `description` varchar(500) NOT NULL,
  `letter` char(1) NOT NULL,
  `key_stage_id` int(11) NOT NULL DEFAULT '4',
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sow_content`
--

INSERT INTO `sow_content` (`id`, `description`, `letter`, `key_stage_id`, `created`, `created_by`, `published`) VALUES
(1, 'standard algorithms, including binary search and merge sort', 'A', 4, '0000-00-00 00:00:00', 0, 1),
(2, 'following and writing algorithms to solve problems, including sequence, selection and iteration, and input, processing and output', 'B', 4, '0000-00-00 00:00:00', 0, 1),
(3, 'how particular programs and algorithms work', 'C', 4, '0000-00-00 00:00:00', 0, 1),
(4, 'the concept of data type, including integer, Boolean, real, character and string and data structures, including records and one- and two-dimensional arrays', 'D', 4, '0000-00-00 00:00:00', 0, 1),
(5, 'representation of numbers in binary and hexadecimal; conversion between these and decimal; binary addition and shifts', 'E', 4, '0000-00-00 00:00:00', 0, 1),
(6, 'representation of text, sound, and graphics inside computers', 'F', 4, '0000-00-00 00:00:00', 0, 1),
(7, 'Boolean logic using AND, OR and NOT, combination of these, and the application of logical operators', 'G', 4, '0000-00-00 00:00:00', 0, 1),
(8, 'the purpose and functionality of systems software, including the operating system and utility software', 'H', 4, '0000-00-00 00:00:00', 0, 1),
(9, 'characteristics of systems architectures: CPU architecture, including Von Neumann and the role of components', 'I', 4, '0000-00-00 00:00:00', 0, 1),
(10, 'characteristics of systems architectures: main and contemporary secondary storage and ways of storing data on devices including magnetic, optical and solid state', 'J', 4, '0000-00-00 00:00:00', 0, 1),
(11, 'characteristics of systems architectures: data capacity and calculation of data capacity requirements', 'K', 4, '0000-00-00 00:00:00', 0, 1),
(12, 'networks and the importance of: connectivity, both wired and wireless; types of networks; common network topologies; network security; protocols; layers', 'L', 4, '0000-00-00 00:00:00', 0, 1),
(13, 'cyber security: forms of attack; methods of identifying vulnerabilities; way to protect software systems', 'M', 4, '0000-00-00 00:00:00', 0, 1),
(14, 'the ethical, legal and environmental impacts of digital technology on wider society, including issues of privacy and cyber security', 'N', 4, '0000-00-00 00:00:00', 0, 1),
(15, 'characteristics and purpose of different levels of programming language, including lowlevel language', 'O', 4, '0000-00-00 00:00:00', 0, 1),
(17, 'use a keyboard and mouse effectively', 'A', 2, '0000-00-00 00:00:00', 0, 1),
(19, 'fundamentals of programming', 'A', 5, '0000-00-00 00:00:00', 0, 1),
(20, 'the concept of data type, including primitive data types and complex data structures', 'B', 5, '0000-00-00 00:00:00', 0, 1),
(21, 'data representation', 'C', 5, '0000-00-00 00:00:00', 0, 1),
(22, 'following and writing algorithms', 'D', 5, '0000-00-00 00:00:00', 0, 1),
(23, 'methods of capturing, selecting, exchanging and managing data to produce information for a particular purpose ', 'E', 5, '0000-00-00 00:00:00', 0, 1),
(24, 'the need for and functions of systems software ', 'F', 5, '0000-00-00 00:00:00', 0, 1),
(25, 'characteristics of contemporary systems architectures, including processors, storage, input, output and their connectivity', 'G', 5, '0000-00-00 00:00:00', 0, 1),
(26, 'characteristics of networks and the importance of networking protocols and standards', 'H', 5, '0000-00-00 00:00:00', 0, 1),
(27, 'the individual moral, social ethical, legal and cultural opportunities and risks of digital technology', 'I', 5, '0000-00-00 00:00:00', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sow_content`
--
ALTER TABLE `sow_content`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_sow_content_key_stage` (`key_stage_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sow_content`
--
ALTER TABLE `sow_content`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `sow_content`
--
ALTER TABLE `sow_content`
  ADD CONSTRAINT `fk_sow_content_key_stage` FOREIGN KEY (`key_stage_id`) REFERENCES `sow_key_stage` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
