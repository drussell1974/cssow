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
-- Table structure for table `sow_schemeofwork`
--

CREATE TABLE `sow_schemeofwork` (
  `id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `asset_id` int(10) NOT NULL DEFAULT '0',
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1',
  `catid` int(11) NOT NULL DEFAULT '0',
  `params` varchar(1024) NOT NULL DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sow_schemeofwork`
--
ALTER TABLE `sow_schemeofwork`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sow_schemeofwork`
--
ALTER TABLE `sow_schemeofwork`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
