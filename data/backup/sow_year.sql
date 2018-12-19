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
-- Table structure for table `sow_year`
--

CREATE TABLE `sow_year` (
  `id` int(11) NOT NULL,
  `name` varchar(4) NOT NULL,
  `key_stage_id` int(11) NOT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sow_year`
--

INSERT INTO `sow_year` (`id`, `name`, `key_stage_id`, `created`, `created_by`, `published`) VALUES
(1, 'Yr1', 1, '0000-00-00 00:00:00', 0, 1),
(2, 'Yr2', 1, '0000-00-00 00:00:00', 0, 1),
(3, 'Yr3', 1, '0000-00-00 00:00:00', 0, 1),
(4, 'Yr4', 2, '0000-00-00 00:00:00', 0, 1),
(5, 'Yr5', 2, '0000-00-00 00:00:00', 0, 1),
(6, 'Yr6', 2, '0000-00-00 00:00:00', 0, 1),
(7, 'Yr7', 3, '0000-00-00 00:00:00', 0, 1),
(8, 'Yr8', 3, '0000-00-00 00:00:00', 0, 1),
(9, 'Yr9', 3, '0000-00-00 00:00:00', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sow_year`
--
ALTER TABLE `sow_year`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_sow_year_keystage_idx` (`key_stage_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sow_year`
--
ALTER TABLE `sow_year`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `sow_year`
--
ALTER TABLE `sow_year`
  ADD CONSTRAINT `fk_sow_year_keystage` FOREIGN KEY (`key_stage_id`) REFERENCES `sow_key_stage` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
