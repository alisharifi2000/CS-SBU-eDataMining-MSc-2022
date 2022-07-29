-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 01, 2022 at 07:24 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dm`
--

-- --------------------------------------------------------

--
-- Table structure for table `timeseries`
--

CREATE TABLE `timeseries` (
  `date` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
  `vol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_unicode_ci;

--
-- Dumping data for table `timeseries`
--

INSERT INTO `timeseries` (`date`, `vol`) VALUES
('1399-9-9', 4),
('1399-9-10', 5),
('1399-9-11', 95),
('1399-9-12', 90),
('1399-9-13', 70),
('1399-9-14', 99),
('1399-9-15', 70),
('1399-9-16', 99),
('1399-9-20', 99),
('1399-9-18', 70),
('1399-9-19', 99),
('1399-9-21', 99),
('1399-9-22', 70),
('1399-9-23', 99),
('1399-9-24', 99),
('1399-9-25', 70),
('1399-9-26', 99);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
