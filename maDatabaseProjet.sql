-- MariaDB dump 10.19  Distrib 10.11.4-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: maDatabaseProjet.sql
-- ------------------------------------------------------
-- Server version	10.11.4-MariaDB-1~deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES
(2,'student'),
(1,'teacher');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES
(1,1,1),
(2,1,2),
(3,1,3),
(4,1,4),
(5,1,5),
(6,1,6),
(7,1,7),
(8,1,8),
(9,1,9),
(10,1,10),
(11,1,11),
(12,1,12),
(13,1,13),
(14,1,14),
(15,1,15),
(16,1,16),
(17,1,17),
(18,1,18),
(19,1,19),
(20,1,20),
(21,1,21),
(22,1,22),
(23,1,23),
(24,1,24),
(25,1,25),
(26,1,26),
(27,1,27),
(28,1,28),
(29,1,29),
(30,1,30),
(31,1,31),
(32,1,32),
(34,2,29),
(35,2,30);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add session survey',7,'add_sessionsurvey'),
(26,'Can change session survey',7,'change_sessionsurvey'),
(27,'Can delete session survey',7,'delete_sessionsurvey'),
(28,'Can view session survey',7,'view_sessionsurvey'),
(29,'Can add survey answer',8,'add_surveyanswer'),
(30,'Can change survey answer',8,'change_surveyanswer'),
(31,'Can delete survey answer',8,'delete_surveyanswer'),
(32,'Can view survey answer',8,'view_surveyanswer');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES
(1,'pbkdf2_sha256$720000$AShLfZbQCBhsJi8BvXRdHB$OrnGkz99BJn1ktiumQ0VPcrEtQ4ivyE/jkdZrtq6GBs=','2024-02-08 22:18:52.727143',1,'vincent','Vincent','Panouilleres','vincent@local.lan',1,1,'2024-02-03 16:36:33.000000'),
(2,'pbkdf2_sha256$720000$0RBU7DoBUDtkSMjNcNacdy$rAiB28+yyqD1dlaL/TRKpDnq9nF8UlkljCO++RZ4R88=','2024-02-08 22:19:33.146868',1,'aline','Aline','Gamelin','',1,1,'2024-02-04 18:14:07.000000'),
(3,'pbkdf2_sha256$720000$kVLcakvogUL0TR6m3aZJkB$3VIjMu8Rj6T0nOa4xgr2xQp0v6D7pdCieHfxaA6t5xg=','2024-02-08 22:10:08.372359',0,'lucy','Lucy','Lambert','',0,1,'2024-02-04 18:14:32.000000'),
(4,'pbkdf2_sha256$720000$Xe1eTpEeMVGQrGkBtv95gw$0u3/DgDBy3HR3sgPwODJ7vtVs69xCs3VajObPZlUcAg=','2024-02-08 21:44:10.745657',0,'marc','Marc','Boisvert','',0,1,'2024-02-04 18:14:49.000000'),
(5,'pbkdf2_sha256$720000$hS5h52czpCZuuCqWbdz5hD$QwdtzxOpYputwuD2q0D1RlSXwQABcCCwbZwyYguxu/c=','2024-02-08 22:15:55.647724',0,'marie','Marie','Busson','',0,1,'2024-02-04 18:16:15.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES
(5,1,1),
(4,2,1),
(3,3,2),
(2,4,2),
(1,5,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES
(1,'2024-02-03 16:37:14.384935','1','SessionSurvey object (1)',1,'[{\"added\": {}}]',7,1),
(2,'2024-02-04 18:12:21.560915','1','teacher',1,'[{\"added\": {}}]',3,1),
(3,'2024-02-04 18:13:16.033478','2','student',1,'[{\"added\": {}}]',3,1),
(4,'2024-02-04 18:14:07.654510','2','antoine',1,'[{\"added\": {}}]',4,1),
(5,'2024-02-04 18:14:32.870725','3','lucy',1,'[{\"added\": {}}]',4,1),
(6,'2024-02-04 18:14:49.718016','4','marc',1,'[{\"added\": {}}]',4,1),
(7,'2024-02-04 18:16:16.102188','5','marie',1,'[{\"added\": {}}]',4,1),
(8,'2024-02-04 18:16:34.472414','5','marie',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),
(9,'2024-02-04 18:16:59.536060','4','marc',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),
(10,'2024-02-04 18:17:08.742106','3','lucy',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),
(11,'2024-02-04 18:17:18.303526','2','antoine',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),
(12,'2024-02-04 18:18:05.193898','2','aline',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,1),
(13,'2024-02-04 18:18:21.512004','1','vincent',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),
(14,'2024-02-07 19:38:08.412514','2','aline',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),
(15,'2024-02-07 19:38:52.392057','3','lucy',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),
(16,'2024-02-07 19:39:25.549850','4','marc',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),
(17,'2024-02-07 19:39:41.700744','5','marie',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),
(18,'2024-02-07 19:39:54.943957','1','vincent',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),
(19,'2024-02-08 20:08:24.510677','2','student',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),
(20,'2024-02-08 21:09:00.366066','1','vincent',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),
(21,'2024-02-08 21:13:45.077979','2','aline',2,'[{\"changed\": {\"fields\": [\"Superuser status\"]}}]',4,1),
(22,'2024-02-08 21:14:55.170560','2','aline',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'python2_django','sessionsurvey'),
(8,'python2_django','surveyanswer'),
(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2024-02-03 16:13:52.993873'),
(2,'auth','0001_initial','2024-02-03 16:13:53.039978'),
(3,'admin','0001_initial','2024-02-03 16:13:53.052259'),
(4,'admin','0002_logentry_remove_auto_add','2024-02-03 16:13:53.055734'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-02-03 16:13:53.058350'),
(6,'contenttypes','0002_remove_content_type_name','2024-02-03 16:13:53.068707'),
(7,'auth','0002_alter_permission_name_max_length','2024-02-03 16:13:53.075817'),
(8,'auth','0003_alter_user_email_max_length','2024-02-03 16:13:53.080142'),
(9,'auth','0004_alter_user_username_opts','2024-02-03 16:13:53.083118'),
(10,'auth','0005_alter_user_last_login_null','2024-02-03 16:13:53.089656'),
(11,'auth','0006_require_contenttypes_0002','2024-02-03 16:13:53.090130'),
(12,'auth','0007_alter_validators_add_error_messages','2024-02-03 16:13:53.092504'),
(13,'auth','0008_alter_user_username_max_length','2024-02-03 16:13:53.096462'),
(14,'auth','0009_alter_user_last_name_max_length','2024-02-03 16:13:53.100595'),
(15,'auth','0010_alter_group_name_max_length','2024-02-03 16:13:53.105743'),
(16,'auth','0011_update_proxy_permissions','2024-02-03 16:13:53.109199'),
(17,'auth','0012_alter_user_first_name_max_length','2024-02-03 16:13:53.114979'),
(18,'python2_django','0001_initial','2024-02-03 16:13:53.134464'),
(19,'python2_django','0002_alter_sessionsurvey_datecreation_and_more','2024-02-03 16:13:53.154804'),
(20,'python2_django','0003_rename_datecreation_sessionsurvey_datestarted','2024-02-03 16:13:53.159499'),
(21,'sessions','0001_initial','2024-02-03 16:13:53.163959'),
(22,'python2_django','0004_alter_sessionsurvey_url','2024-02-04 19:50:25.108438'),
(23,'python2_django','0005_surveyanswer_dateinitialsend','2024-02-06 19:46:53.602210'),
(24,'python2_django','0006_alter_surveyanswer_student','2024-02-08 22:06:19.114578');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('mgbkqq4tqlc4iie18lhjpxogd67ud0l6','.eJxVjEEOwiAQAP_C2ZDa3Qp49N43kIVdpGogKe3J-HdD0oNeZybzVp72Lfu9yeoXVlcF6vTLAsWnlC74QeVedaxlW5ege6IP2_RcWV63o_0bZGq5b5H4nCI4FmchCKAZbKCBIBA7w9OYwsSYXISLjZwYHTCglSgGrRnV5wsFeDip:1rXsv4:Qdbw7QluORemPegEHc-2TyQK7e2acJueMCwHYwlzNTc','2024-02-22 01:09:38.386131');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `python2_django_sessionsurvey`
--

DROP TABLE IF EXISTS `python2_django_sessionsurvey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `python2_django_sessionsurvey` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `dateStarted` datetime(6) NOT NULL,
  `dateEnd` datetime(6) NOT NULL,
  `url` varchar(250) NOT NULL,
  `createdBy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `python2_django_sessionsurvey_url_c25be271_uniq` (`url`),
  KEY `python2_django_sessi_createdBy_id_da26231f_fk_auth_user` (`createdBy_id`),
  CONSTRAINT `python2_django_sessi_createdBy_id_da26231f_fk_auth_user` FOREIGN KEY (`createdBy_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `python2_django_sessionsurvey`
--

LOCK TABLES `python2_django_sessionsurvey` WRITE;
/*!40000 ALTER TABLE `python2_django_sessionsurvey` DISABLE KEYS */;
INSERT INTO `python2_django_sessionsurvey` VALUES
(2,'Mon enquête',0,'2024-02-08 21:41:09.000000','2024-02-09 00:41:09.000000','7LN7uQQb',1),
(3,'Mon enquête 3',1,'2024-02-08 21:41:32.000000','2024-02-09 00:41:32.000000','Bp064sh3',1),
(4,'Mon enquête à long terme',1,'2024-02-08 21:41:54.000000','2024-03-29 00:41:54.000000','7W8cz4Wk',1),
(6,'Mon enquête à court terme',0,'2024-02-08 21:42:55.000000','2024-02-09 00:42:55.000000','2Vae47DH',2),
(7,'Cours Python 2',1,'2024-02-08 21:43:15.000000','2024-03-31 00:43:15.000000','CTeVsRgX',2);
/*!40000 ALTER TABLE `python2_django_sessionsurvey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `python2_django_surveyanswer`
--

DROP TABLE IF EXISTS `python2_django_surveyanswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `python2_django_surveyanswer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `percentage` smallint(6) NOT NULL,
  `progression` varchar(2) NOT NULL,
  `difficulty` varchar(2) NOT NULL,
  `dateSend` datetime(6) NOT NULL,
  `session_id` bigint(20) NOT NULL,
  `student_id` int(11) NOT NULL,
  `dateInitialSend` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `python2_django_surve_session_id_e3f63813_fk_python2_d` (`session_id`),
  KEY `python2_django_surveyanswer_student_id_ce735eed` (`student_id`),
  CONSTRAINT `python2_django_surve_session_id_e3f63813_fk_python2_d` FOREIGN KEY (`session_id`) REFERENCES `python2_django_sessionsurvey` (`id`),
  CONSTRAINT `python2_django_surveyanswer_student_id_ce735eed_fk_auth_user_id` FOREIGN KEY (`student_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `python2_django_surveyanswer`
--

LOCK TABLES `python2_django_surveyanswer` WRITE;
/*!40000 ALTER TABLE `python2_django_surveyanswer` DISABLE KEYS */;
INSERT INTO `python2_django_surveyanswer` VALUES
(17,100,'AC','HA','2024-02-08 22:01:50.318667',3,4,'2024-02-08 21:45:51.590290'),
(30,0,'NA','NO','2024-02-08 22:07:47.192142',4,4,'2024-02-08 22:07:47.192142'),
(31,80,'IP','VA','2024-02-08 22:09:25.278598',7,4,'2024-02-08 22:09:25.278598'),
(32,100,'AC','EA','2024-02-08 22:11:16.098678',3,3,'2024-02-08 22:11:16.098678'),
(33,0,'NA','EX','2024-02-08 22:13:03.467196',4,3,'2024-02-08 22:13:03.467196'),
(34,80,'AC','EA','2024-02-08 22:14:27.911280',7,3,'2024-02-08 22:14:27.911280'),
(35,50,'IP','HA','2024-02-08 22:17:03.282101',3,5,'2024-02-08 22:17:03.282101'),
(36,30,'AC','VA','2024-02-08 22:18:34.962520',7,5,'2024-02-08 22:18:34.962520');
/*!40000 ALTER TABLE `python2_django_surveyanswer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-09  0:04:23
