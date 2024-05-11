-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 11, 2024 at 07:34 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `musicdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `album`
--

CREATE TABLE `album` (
  `albumID` varchar(20) NOT NULL,
  `title` varchar(50) NOT NULL,
  `artistID` varchar(20) NOT NULL,
  `genre` varchar(50) NOT NULL,
  `releasedate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `album`
--

INSERT INTO `album` (`albumID`, `title`, `artistID`, `genre`, `releasedate`) VALUES
('AB0001', 'The New', 'AT0003', 'Pop', '2020-01-08');

-- --------------------------------------------------------

--
-- Table structure for table `artist`
--

CREATE TABLE `artist` (
  `artistID` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `genre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `artist`
--

INSERT INTO `artist` (`artistID`, `name`, `genre`) VALUES
('AT0001', 'J977', 'Ballad'),
('AT0002', 'Karik', 'Rap'),
('AT0003', 'Imagine Dragon', 'Pop'),
('AT0004', 'Avicii', 'Pop'),
('AT0005', 'Coldplay', 'Pop'),
('AT0006', 'Boney M', 'Russian Pop'),
('AT0007', 'Ed Sheeran', 'Pop'),
('AT0008', 'One Republic', 'Pop'),
('AT0009', 'Russian', 'Russian Folk'),
('AT0010', 'djkmel', 'Pop'),
('AT0011', 'Jack', 'Pop');

-- --------------------------------------------------------

--
-- Table structure for table `playlist`
--

CREATE TABLE `playlist` (
  `playlistID` varchar(20) NOT NULL,
  `userID` varchar(10) NOT NULL,
  `title` varchar(50) NOT NULL,
  `creationdate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `playlist`
--

INSERT INTO `playlist` (`playlistID`, `userID`, `title`, `creationdate`) VALUES
('PL0001', '0007', 'Pop', '2024-05-10'),
('PL0002', '0007', 'Bug', '2024-05-10');

-- --------------------------------------------------------

--
-- Table structure for table `playlist_detail`
--

CREATE TABLE `playlist_detail` (
  `playlistID` varchar(20) NOT NULL,
  `userID` varchar(20) NOT NULL,
  `trackID` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `playlist_detail`
--

INSERT INTO `playlist_detail` (`playlistID`, `userID`, `trackID`) VALUES
('PL0001', '0007', 'T0004'),
('PL0001', '0007', 'T0009'),
('PL0002', '0007', 'T0010');

-- --------------------------------------------------------

--
-- Table structure for table `track`
--

CREATE TABLE `track` (
  `trackID` varchar(20) NOT NULL,
  `title` varchar(50) NOT NULL,
  `artistID` varchar(20) NOT NULL,
  `albumID` varchar(20) DEFAULT NULL,
  `duration` smallint(100) NOT NULL,
  `realeasedate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `track`
--

INSERT INTO `track` (`trackID`, `title`, `artistID`, `albumID`, `duration`, `realeasedate`) VALUES
('T0001', 'Thiên Lý Ơi', 'AT0011', NULL, 220, '2024-01-02'),
('T0002', 'Hai Thế Giới', 'AT0002', NULL, 278, '2012-07-06'),
('T0003', 'Khu Tao Sống', 'AT0002', NULL, 241, '2012-07-05'),
('T0004', 'Thương', 'AT0002', NULL, 176, '2017-05-09'),
('T0005', 'Anh Không Đòi Quà', 'AT0002', NULL, 198, '2019-07-11'),
('T0006', 'Mặc Cảm', 'AT0002', NULL, 228, '2018-12-23'),
('T0007', 'The Nights', 'AT0004', NULL, 176, '0201-08-04'),
('T0008', 'Rasputin', 'AT0006', NULL, 220, '2011-08-22'),
('T0009', 'Hymn For The Weekend', 'AT0004', NULL, 220, '2016-08-06'),
('T0010', 'Shape Of You', 'AT0007', NULL, 220, '2014-02-05'),
('T0011', 'Radioactive', 'AT0003', 'AB0001', 232, '2013-07-05'),
('T0012', 'Counting Stars', 'AT0008', NULL, 268, '2010-08-09'),
('T0013', 'The Bogatyr', 'AT0009', NULL, 220, '2012-04-06'),
('T0014', 'Katyusha', 'AT0009', NULL, 210, '2008-08-06'),
('T0015', 'Stronger Than You', 'AT0010', NULL, 241, '2018-05-08');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userID` varchar(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userID`, `username`, `email`, `password`) VALUES
('0001', 'admin', '0', 'admin'),
('0002', 'acquy369258147', 'acquy3695741@gmail.com', 'Dotuan952003'),
('0003', 'duyphan', 'duy1425@gmail.com', '111222'),
('0004', 'hieuvan', 'hieu8845@gmail.com', '1247aa'),
('0005', 'danhpham', 'danh2547@gmail.com', '349ax'),
('0006', 'debugger', 'bug@gmail.com', 'bugggg'),
('0007', 'aaa', 'aaaa', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`albumID`),
  ADD KEY `album_artistfk_1` (`artistID`);

--
-- Indexes for table `artist`
--
ALTER TABLE `artist`
  ADD PRIMARY KEY (`artistID`);

--
-- Indexes for table `playlist`
--
ALTER TABLE `playlist`
  ADD PRIMARY KEY (`playlistID`),
  ADD KEY `playlist_useridfk_1` (`userID`);

--
-- Indexes for table `playlist_detail`
--
ALTER TABLE `playlist_detail`
  ADD PRIMARY KEY (`playlistID`,`trackID`) USING BTREE,
  ADD KEY `pldetail_useridfk_1` (`userID`),
  ADD KEY `pldetail_trackidfk_1` (`trackID`);

--
-- Indexes for table `track`
--
ALTER TABLE `track`
  ADD PRIMARY KEY (`trackID`),
  ADD KEY `track_artistfk_1` (`artistID`),
  ADD KEY `track_albumidfk_1` (`albumID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `album_artistfk_1` FOREIGN KEY (`artistID`) REFERENCES `artist` (`artistID`);

--
-- Constraints for table `playlist`
--
ALTER TABLE `playlist`
  ADD CONSTRAINT `playlist_useridfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`userID`);

--
-- Constraints for table `playlist_detail`
--
ALTER TABLE `playlist_detail`
  ADD CONSTRAINT `pldetail_playlistidfk_1` FOREIGN KEY (`playlistID`) REFERENCES `playlist` (`playlistID`),
  ADD CONSTRAINT `pldetail_trackidfk_1` FOREIGN KEY (`trackID`) REFERENCES `track` (`trackID`),
  ADD CONSTRAINT `pldetail_useridfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`userID`);

--
-- Constraints for table `track`
--
ALTER TABLE `track`
  ADD CONSTRAINT `track_albumidfk_1` FOREIGN KEY (`albumID`) REFERENCES `album` (`albumID`),
  ADD CONSTRAINT `track_artistfk_1` FOREIGN KEY (`artistID`) REFERENCES `artist` (`artistID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
