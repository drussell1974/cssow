-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: db764008810.hosting-data.io
-- Generation Time: Dec 15, 2018 at 07:30 AM
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
-- Table structure for table `sow_topic`
--

CREATE TABLE `sow_topic` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sow_topic`
--

INSERT INTO `sow_topic` (`id`, `name`, `parent_id`, `created`, `created_by`, `published`) VALUES
(1, 'Algorithms', 0, '0000-00-00 00:00:00', 0, 1),
(2, 'Programming and development', 0, '0000-00-00 00:00:00', 0, 1),
(3, 'Data representation', 0, '0000-00-00 00:00:00', 0, 1),
(4, 'Hardware and architecture', 0, '0000-00-00 00:00:00', 0, 1),
(5, 'Communication and networks', 0, '0000-00-00 00:00:00', 0, 1),
(6, 'Information technology', 0, '0000-00-00 00:00:00', 0, 1),
(7, 'CPU', 4, '0000-00-00 00:00:00', 0, 1),
(8, 'Memory', 4, '0000-00-00 00:00:00', 0, 1),
(9, 'Types of computers', 4, '0000-00-00 00:00:00', 0, 1),
(10, 'Primary storage', 4, '0000-00-00 00:00:00', 0, 1),
(11, 'Secondary storage', 4, '0000-00-00 00:00:00', 0, 1),
(12, 'Flash memory', 4, '0000-00-00 00:00:00', 0, 1),
(13, 'Magnetic storage', 4, '0000-00-00 00:00:00', 0, 1),
(14, 'Optical storage', 4, '0000-00-00 00:00:00', 0, 1),
(15, 'Networks', 5, '0000-00-00 00:00:00', 0, 1),
(16, 'VPN', 5, '0000-00-00 00:00:00', 0, 1),
(17, 'Network connection', 5, '0000-00-00 00:00:00', 0, 1),
(18, 'Types of network', 5, '0000-00-00 00:00:00', 0, 1),
(19, 'Network hardware', 5, '0000-00-00 00:00:00', 0, 1),
(20, 'Network topology', 5, '0000-00-00 00:00:00', 0, 1),
(21, 'Network protocol', 5, '0000-00-00 00:00:00', 0, 1),
(22, 'Network encryption', 5, '0000-00-00 00:00:00', 0, 1),
(23, 'Network addressing', 5, '0000-00-00 00:00:00', 0, 1),
(24, 'Network protocol', 5, '0000-00-00 00:00:00', 0, 1),
(25, 'Network layers', 5, '0000-00-00 00:00:00', 0, 1),
(26, 'Network hardware', 5, '0000-00-00 00:00:00', 0, 1),
(27, 'Malicious attacks', 5, '0000-00-00 00:00:00', 0, 1),
(28, 'Network policy', 5, '0000-00-00 00:00:00', 0, 1),
(29, 'Hacking', 5, '0000-00-00 00:00:00', 0, 1),
(30, 'Internet services', 6, '0000-00-00 00:00:00', 0, 1),
(31, 'Programs and applications', 6, '0000-00-00 00:00:00', 0, 1),
(32, 'Operating system', 6, '0000-00-00 00:00:00', 0, 1),
(33, 'Libraries', 6, '0000-00-00 00:00:00', 0, 1),
(34, 'Utilities', 6, '0000-00-00 00:00:00', 0, 1),
(35, 'Problem solving', 1, '0000-00-00 00:00:00', 0, 1),
(36, 'Algorithms', 1, '0000-00-00 00:00:00', 0, 1),
(37, 'Programming and constructs', 1, '0000-00-00 00:00:00', 0, 1),
(38, 'Data Types', 1, '0000-00-00 00:00:00', 0, 1),
(39, 'Program structures', 1, '0000-00-00 00:00:00', 0, 1),
(40, 'Logic gates', 1, '0000-00-00 00:00:00', 0, 1),
(41, 'Boolean algebra', 1, '0000-00-00 00:00:00', 0, 1),
(42, 'Operators', 2, '0000-00-00 00:00:00', 0, 1),
(43, 'Variables and constants', 2, '0000-00-00 00:00:00', 0, 1),
(44, 'Iteration and loops', 2, '0000-00-00 00:00:00', 0, 1),
(45, 'Arrays', 2, '0000-00-00 00:00:00', 0, 1),
(46, 'Storing and accessing data: Files and SQL', 2, '0000-00-00 00:00:00', 0, 1),
(47, 'String manipulation', 2, '0000-00-00 00:00:00', 0, 1),
(48, 'Functions and procedures', 2, '0000-00-00 00:00:00', 0, 1),
(49, 'Documentation, testing and Debugging', 2, '0000-00-00 00:00:00', 0, 1),
(50, 'Translators', 2, '0000-00-00 00:00:00', 0, 1),
(51, 'Assembly language', 2, '0000-00-00 00:00:00', 0, 1),
(52, 'Assemblers', 2, '0000-00-00 00:00:00', 0, 1),
(53, 'High-level languages', 2, '0000-00-00 00:00:00', 0, 1),
(54, 'Compilers', 2, '0000-00-00 00:00:00', 0, 1),
(55, 'Interpreters', 2, '0000-00-00 00:00:00', 0, 1),
(56, 'Development environment', 2, '0000-00-00 00:00:00', 0, 1),
(57, 'Run-time environment', 2, '0000-00-00 00:00:00', 0, 1),
(58, 'Binary', 3, '0000-00-00 00:00:00', 0, 1),
(59, 'Hexidecimal', 3, '0000-00-00 00:00:00', 0, 1),
(60, 'Characters', 3, '0000-00-00 00:00:00', 0, 1),
(61, 'Images', 3, '0000-00-00 00:00:00', 0, 1),
(62, 'Metadata', 3, '0000-00-00 00:00:00', 0, 1),
(63, 'Images', 3, '0000-00-00 00:00:00', 0, 1),
(64, 'Sound', 3, '0000-00-00 00:00:00', 0, 1),
(65, 'Data compression', 3, '0000-00-00 00:00:00', 0, 1),
(66, 'Cultural', 6, '0000-00-00 00:00:00', 0, 1),
(67, 'Legal', 6, '0000-00-00 00:00:00', 0, 1),
(68, 'Open-source and propretary software', 6, '0000-00-00 00:00:00', 0, 1),
(69, 'Ethical', 6, '0000-00-00 00:00:00', 0, 1),
(70, 'Automation', 6, '0000-00-00 00:00:00', 0, 1),
(71, 'Artificial Intelligence', 6, '0000-00-00 00:00:00', 0, 1),
(72, 'Environment', 6, '0000-00-00 00:00:00', 0, 1),
(73, 'Computing', 0, '0000-00-00 00:00:00', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sow_topic`
--
ALTER TABLE `sow_topic`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_sow_topic_topic1_idx` (`parent_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sow_topic`
--
ALTER TABLE `sow_topic`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10001;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
