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
-- Table structure for table `sow_learning_objective_has_ks123_pathway`
--

CREATE TABLE `sow_learning_objective_has_ks123_pathway` (
  `id` int(11) NOT NULL,
  `learning_objective_id` int(11) NOT NULL,
  `ks123_pathway_id` int(11) NOT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sow_learning_objective_has_ks123_pathway`
--
ALTER TABLE `sow_learning_objective_has_ks123_pathway`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_sow_learning_objective_has_ks123_pathway_ks123_pathway_idx` (`ks123_pathway_id`),
  ADD KEY `fk_learning_objective_has_ks123_pathway_learning_objective_idx` (`learning_objective_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sow_learning_objective_has_ks123_pathway`
--
ALTER TABLE `sow_learning_objective_has_ks123_pathway`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `sow_learning_objective_has_ks123_pathway`
--
ALTER TABLE `sow_learning_objective_has_ks123_pathway`
  ADD CONSTRAINT `fk_sow_learning_objective_has_ks123_pathway_ks123_pathway1` FOREIGN KEY (`ks123_pathway_id`) REFERENCES `sow_ks123_pathway` (`id`),
  ADD CONSTRAINT `fk_sow_learning_objective_has_ks123_pathway_learning_objective1` FOREIGN KEY (`learning_objective_id`) REFERENCES `sow_learning_objective` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
