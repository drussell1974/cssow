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
-- Table structure for table `sow_solo_taxonomy`
--

CREATE TABLE `sow_solo_taxonomy` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `level` char(1) NOT NULL DEFAULT 'A',
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sow_solo_taxonomy`
--

INSERT INTO `sow_solo_taxonomy` (`id`, `name`, `level`, `created`, `created_by`, `published`) VALUES
(1, 'A Unistructural: Identify, Name, Define', 'A', '0000-00-00 00:00:00', 0, 1),
(2, 'Multistructural: Describe, List', 'B', '0000-00-00 00:00:00', 0, 1),
(3, 'Relational: Explain, Compare, Justify and Give Reasons', 'C', '0000-00-00 00:00:00', 0, 1),
(4, 'Extended Abstract: Create, Formulate', 'D', '0000-00-00 00:00:00', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sow_solo_taxonomy`
--
ALTER TABLE `sow_solo_taxonomy`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name_UNIQUE` (`name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sow_solo_taxonomy`
--
ALTER TABLE `sow_solo_taxonomy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
