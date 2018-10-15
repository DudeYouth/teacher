-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 2018-10-16 01:50:02
-- 服务器版本： 10.1.10-MariaDB
-- PHP Version: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `phpyun_test`
--

-- --------------------------------------------------------

--
-- 表的结构 `zpcomclass`
--

CREATE TABLE `zpcomclass` (
  `id` int(11) NOT NULL,
  `keyid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `variable` varchar(50) NOT NULL,
  `sort` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- 转存表中的数据 `zpcomclass`
--

INSERT INTO `zpcomclass` (`id`, `keyid`, `name`, `variable`, `sort`) VALUES
(1, 0, '测试', '1231531', 1);

-- --------------------------------------------------------

--
-- 表的结构 `zpcompany`
--

CREATE TABLE `zpcompany` (
  `uid` int(11) NOT NULL,
  `name` varchar(25) NOT NULL DEFAULT '',
  `shortname` varchar(25) NOT NULL DEFAULT '',
  `hy` int(5) DEFAULT NULL,
  `pr` int(5) DEFAULT NULL,
  `provinceid` int(5) DEFAULT NULL,
  `cityid` int(5) DEFAULT NULL,
  `three_cityid` int(5) DEFAULT NULL,
  `mun` int(3) DEFAULT NULL,
  `sdate` varchar(20) NOT NULL DEFAULT '',
  `money` int(11) DEFAULT NULL,
  `moneytype` int(11) DEFAULT '1',
  `content` text NOT NULL,
  `address` varchar(100) NOT NULL DEFAULT '',
  `zip` varchar(10) NOT NULL DEFAULT '',
  `linkman` varchar(50) NOT NULL DEFAULT '',
  `linkjob` varchar(50) NOT NULL DEFAULT '',
  `linkqq` varchar(20) NOT NULL DEFAULT '',
  `linkphone` varchar(100) NOT NULL DEFAULT '',
  `linktel` varchar(50) NOT NULL DEFAULT '',
  `linkmail` varchar(150) NOT NULL DEFAULT '',
  `website` varchar(100) NOT NULL DEFAULT '',
  `x` varchar(100) NOT NULL DEFAULT '',
  `y` varchar(100) NOT NULL DEFAULT '',
  `logo` varchar(100) NOT NULL DEFAULT '',
  `payd` int(8) DEFAULT '0',
  `integral` int(10) DEFAULT '0',
  `lastupdate` varchar(10) NOT NULL DEFAULT '',
  `cloudtype` int(2) DEFAULT NULL,
  `jobtime` int(11) DEFAULT NULL,
  `r_status` int(2) DEFAULT '0',
  `firmpic` varchar(100) NOT NULL DEFAULT '',
  `rec` int(11) DEFAULT '0',
  `hits` int(11) DEFAULT '0',
  `ant_num` int(11) DEFAULT '0',
  `pl_time` int(11) DEFAULT NULL,
  `pl_status` int(11) DEFAULT '1',
  `order` int(11) UNSIGNED DEFAULT '0',
  `admin_remark` varchar(255) NOT NULL DEFAULT '',
  `email_dy` int(11) DEFAULT '0',
  `msg_dy` int(11) DEFAULT '0',
  `sync` int(11) UNSIGNED DEFAULT '0',
  `hy_dy` varchar(100) NOT NULL DEFAULT '',
  `moblie_status` int(1) DEFAULT '0',
  `email_status` int(1) DEFAULT '0',
  `yyzz_status` int(1) DEFAULT '0',
  `hottime` int(11) DEFAULT '0',
  `did` int(11) DEFAULT NULL,
  `busstops` text NOT NULL,
  `infostatus` int(11) DEFAULT '1',
  `conid` int(11) DEFAULT NULL,
  `addtime` int(11) DEFAULT NULL,
  `comqcode` varchar(200) NOT NULL DEFAULT '',
  `crm_uid` int(11) DEFAULT '0',
  `crm_time` int(11) DEFAULT NULL,
  `crm_status` tinyint(1) DEFAULT '0',
  `welfare` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `zpcompany`
--

INSERT INTO `zpcompany` (`uid`, `name`, `shortname`, `hy`, `pr`, `provinceid`, `cityid`, `three_cityid`, `mun`, `sdate`, `money`, `moneytype`, `content`, `address`, `zip`, `linkman`, `linkjob`, `linkqq`, `linkphone`, `linktel`, `linkmail`, `website`, `x`, `y`, `logo`, `payd`, `integral`, `lastupdate`, `cloudtype`, `jobtime`, `r_status`, `firmpic`, `rec`, `hits`, `ant_num`, `pl_time`, `pl_status`, `order`, `admin_remark`, `email_dy`, `msg_dy`, `sync`, `hy_dy`, `moblie_status`, `email_status`, `yyzz_status`, `hottime`, `did`, `busstops`, `infostatus`, `conid`, `addtime`, `comqcode`, `crm_uid`, `crm_time`, `crm_status`, `welfare`) VALUES
(2, '测试01', '测试01', 35, 23, 6, 76, 693, 30, '', NULL, 1, '<p>测试01</p>', '珠江新城', '', '黄先生', '', '', '', '18312168363', '1157536217@qq.com', '', '', '', '', 0, 0, '1539535099', NULL, 1539608831, 0, '', 0, 7, 0, NULL, 1, 0, '', 0, 0, 0, '', 0, 0, 0, 0, NULL, '', 1, NULL, NULL, '', 0, NULL, 0, '');

-- --------------------------------------------------------

--
-- 表的结构 `zpcompany_job`
--

CREATE TABLE `zpcompany_job` (
  `id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL DEFAULT '',
  `com_name` varchar(50) NOT NULL DEFAULT '',
  `hy` int(5) DEFAULT NULL,
  `job1` int(5) DEFAULT NULL,
  `job1_son` int(5) DEFAULT NULL,
  `job_post` int(5) DEFAULT NULL,
  `provinceid` int(5) DEFAULT NULL,
  `cityid` int(5) DEFAULT NULL,
  `three_cityid` int(5) DEFAULT NULL,
  `cert` varchar(50) NOT NULL DEFAULT '',
  `type` int(5) NOT NULL,
  `number` int(2) NOT NULL,
  `exp` int(5) NOT NULL,
  `report` int(5) NOT NULL,
  `sex` int(5) NOT NULL,
  `edu` int(5) NOT NULL,
  `marriage` int(5) NOT NULL,
  `description` text NOT NULL,
  `xuanshang` int(11) NOT NULL DEFAULT '0',
  `xsdate` int(11) DEFAULT NULL,
  `sdate` int(11) NOT NULL,
  `edate` int(11) NOT NULL,
  `jobhits` int(10) NOT NULL DEFAULT '0',
  `lastupdate` varchar(10) NOT NULL DEFAULT '',
  `rec` int(2) DEFAULT '0',
  `cloudtype` int(2) DEFAULT NULL,
  `state` int(2) DEFAULT '0',
  `statusbody` varchar(200) NOT NULL DEFAULT '',
  `age` int(11) DEFAULT NULL,
  `lang` text NOT NULL,
  `welfare` text NOT NULL,
  `pr` int(5) DEFAULT NULL,
  `mun` int(5) DEFAULT NULL,
  `com_provinceid` int(5) DEFAULT NULL,
  `rating` int(5) DEFAULT NULL,
  `status` int(1) NOT NULL DEFAULT '0',
  `urgent` int(1) DEFAULT NULL,
  `r_status` int(1) DEFAULT '1',
  `end_email` int(1) DEFAULT '0',
  `urgent_time` int(11) DEFAULT NULL,
  `com_logo` varchar(100) NOT NULL DEFAULT '',
  `autotype` int(11) DEFAULT '0',
  `autotime` int(11) DEFAULT '0',
  `is_link` int(1) DEFAULT '1',
  `link_type` int(1) DEFAULT '1',
  `source` int(1) DEFAULT '1',
  `rec_time` int(11) DEFAULT '0',
  `snum` int(11) DEFAULT '0',
  `operatime` int(11) DEFAULT NULL,
  `did` int(11) DEFAULT NULL,
  `is_email` int(1) DEFAULT '1',
  `minsalary` int(11) DEFAULT NULL,
  `maxsalary` int(11) DEFAULT NULL,
  `sharepack` int(11) NOT NULL DEFAULT '0',
  `rewardpack` int(11) NOT NULL DEFAULT '0',
  `is_graduate` int(11) DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `zpcompany_job`
--

INSERT INTO `zpcompany_job` (`id`, `uid`, `name`, `com_name`, `hy`, `job1`, `job1_son`, `job_post`, `provinceid`, `cityid`, `three_cityid`, `cert`, `type`, `number`, `exp`, `report`, `sex`, `edu`, `marriage`, `description`, `xuanshang`, `xsdate`, `sdate`, `edate`, `jobhits`, `lastupdate`, `rec`, `cloudtype`, `state`, `statusbody`, `age`, `lang`, `welfare`, `pr`, `mun`, `com_provinceid`, `rating`, `status`, `urgent`, `r_status`, `end_email`, `urgent_time`, `com_logo`, `autotype`, `autotime`, `is_link`, `link_type`, `source`, `rec_time`, `snum`, `operatime`, `did`, `is_email`, `minsalary`, `maxsalary`, `sharepack`, `rewardpack`, `is_graduate`) VALUES
(1, 2, '测试', '测试01', 43, 43, 87, 689, 6, 86, 787, '', 0, 40, 127, 54, 3, 65, 72, '<p>瓦达达娃大<br/></p>', 0, NULL, 1538793498, 0, 5, '1539535099', 0, NULL, 1, '', 88, '101', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 15, 0, 0, 0),
(2, 2, '测试02', '测试01', 43, 43, 87, 689, 2, 52, 516, '', 0, 40, 127, 54, 3, 65, 72, '<p>啊大碗大碗大碗阿瓦蒂</p>', 0, NULL, 1538793557, 0, 2, '1539535099', 0, NULL, 1, '', 88, '101', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 15, 0, 0, 0),
(3, 2, '测试01', '测试01', 43, 43, 87, 687, 2, 52, 517, '', 0, 40, 127, 54, 3, 65, 72, '<p>哇大碗大碗大碗大大哇好看；考了托福分数大大</p>', 0, NULL, 1538795417, 0, 0, '1539535099', 0, NULL, 1, '', 88, '100', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 12, 0, 0, 0),
(4, 2, '测试03', '测试01', 43, 43, 87, 689, 2, 52, 516, '', 0, 40, 13, 59, 2, 67, 112, '<p>伟大我的娃大</p>', 0, NULL, 1538815334, 0, 2, '1539535099', 0, NULL, 1, '', 85, '100', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 12, 0, 0, 0),
(5, 2, '测试04', '测试01', 43, 43, 87, 688, 2, 52, 0, '', 0, 41, 14, 58, 1, 67, 112, '<p>伟大伟大伟大阿瓦大大王大大王啊</p>', 0, NULL, 1538815444, 0, 1, '1539535099', 0, NULL, 1, '', 86, '100,101,109', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 12, 0, 0, 0),
(6, 2, '测试011', '测试01', 35, 43, 87, 686, 6, 76, 693, '', 0, 40, 12, 54, 3, 66, 72, '<p>4884648648</p>', 0, NULL, 1539482844, 0, 0, '1539535099', 0, NULL, 1, '', 87, '100', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 21, 0, 0, 0),
(7, 2, '测试0001', '测试01', 43, 43, 87, 690, 6, 76, 693, '', 0, 0, 15, 54, 3, 66, 72, '<p>wdawdqawdawdawdaw</p>', 0, NULL, 1539526162, 0, 0, '1539535099', 0, NULL, 1, '', 88, '100', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 15, 0, 0, 0),
(8, 2, '5315315313', '测试01', 35, 43, 87, 689, 6, 76, 693, '', 0, 40, 13, 54, 3, 66, 72, '<p>5135315315315315315</p>', 0, NULL, 1539526321, 0, 0, '1539535099', 0, NULL, 1, '', 88, '100', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 15, 0, 0, 0),
(9, 2, '45634534354', '测试01', 43, 43, 87, 693, 2, 52, 0, '', 0, 40, 13, 54, 3, 66, 72, '<p>534534</p>', 0, NULL, 1539526821, 0, 1, '1539535099', 0, NULL, 1, '', 88, '100', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 21, 0, 0, 0),
(10, 2, '45634534354', '测试01', 35, 43, 87, 693, 2, 52, 517, '', 0, 40, 13, 54, 3, 66, 72, '<p>534534</p>', 0, NULL, 1539608119, 0, 0, '1539608119', 0, NULL, 1, '', 88, '100', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 21, 0, 0, 0),
(11, 2, '45634534354', '测试01', 35, 43, 87, 693, 2, 52, 516, '', 0, 40, 127, 54, 3, 65, 72, '<p>534534</p>', 0, NULL, 1539608831, 0, 0, '1539608831', 0, NULL, 1, '', 88, '100', '', 23, 30, 6, 3, 0, NULL, 1, 0, NULL, '', 0, 0, 1, 1, 1, 0, 0, NULL, 0, 1, 11, 21, 0, 0, 0);

-- --------------------------------------------------------

--
-- 表的结构 `zpcompany_job_link`
--

CREATE TABLE `zpcompany_job_link` (
  `id` int(11) NOT NULL,
  `uid` int(11) DEFAULT NULL,
  `jobid` int(11) DEFAULT NULL,
  `link_man` varchar(100) DEFAULT NULL,
  `link_moblie` varchar(20) DEFAULT NULL,
  `email_type` int(2) DEFAULT NULL,
  `is_email` int(2) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `link_type` int(2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `zpcompany_job_link`
--

INSERT INTO `zpcompany_job_link` (`id`, `uid`, `jobid`, `link_man`, `link_moblie`, `email_type`, `is_email`, `email`, `link_type`) VALUES
(1, 2, 1, NULL, NULL, 1, 1, '', 1),
(2, 2, 2, NULL, NULL, 1, 1, '', 1),
(3, 2, 3, NULL, NULL, 1, 1, '', 1),
(4, 2, 4, NULL, NULL, 1, 1, '', 1),
(5, 2, 5, NULL, NULL, 1, 1, '', 1),
(6, 2, 6, NULL, NULL, 1, 1, '', 1),
(7, 2, 7, NULL, NULL, 1, 1, '', 1),
(8, 2, 8, NULL, NULL, 1, 1, '', 1),
(9, 2, 9, NULL, NULL, 1, 1, '', 1),
(10, 2, 10, NULL, NULL, 1, 1, '', 1),
(11, 2, 11, NULL, NULL, 1, 1, '', 1);

-- --------------------------------------------------------

--
-- 表的结构 `zpjob_class`
--

CREATE TABLE `zpjob_class` (
  `id` int(11) NOT NULL,
  `keyid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `sort` int(11) NOT NULL,
  `content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- 表的结构 `zplssave`
--

CREATE TABLE `zplssave` (
  `id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `save` text NOT NULL,
  `savetype` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `zpcomclass`
--
ALTER TABLE `zpcomclass`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `zpcompany`
--
ALTER TABLE `zpcompany`
  ADD KEY `uid` (`uid`) USING BTREE;

--
-- Indexes for table `zpcompany_job`
--
ALTER TABLE `zpcompany_job`
  ADD PRIMARY KEY (`id`),
  ADD KEY `uid` (`uid`),
  ADD KEY `lastupdate` (`lastupdate`),
  ADD KEY `cityid` (`provinceid`,`cityid`,`three_cityid`),
  ADD KEY `jobid` (`job1`,`job1_son`,`job_post`),
  ADD KEY `urgent` (`urgent_time`),
  ADD KEY `rectime` (`rec_time`),
  ADD KEY `sharepcak` (`sharepack`),
  ADD KEY `rewardpack` (`rewardpack`),
  ADD KEY `xsdate` (`xsdate`),
  ADD KEY `isgraduate` (`is_graduate`);

--
-- Indexes for table `zpcompany_job_link`
--
ALTER TABLE `zpcompany_job_link`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `zpjob_class`
--
ALTER TABLE `zpjob_class`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `zplssave`
--
ALTER TABLE `zplssave`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `zpcomclass`
--
ALTER TABLE `zpcomclass`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- 使用表AUTO_INCREMENT `zpcompany_job`
--
ALTER TABLE `zpcompany_job`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- 使用表AUTO_INCREMENT `zpcompany_job_link`
--
ALTER TABLE `zpcompany_job_link`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- 使用表AUTO_INCREMENT `zpjob_class`
--
ALTER TABLE `zpjob_class`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `zplssave`
--
ALTER TABLE `zplssave`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
