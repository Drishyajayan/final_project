/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - heartfailure
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`heartfailure` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `heartfailure`;

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` varchar(100) DEFAULT NULL,
  `to` varchar(100) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`id`,`from`,`to`,`message`,`date`) values 
(1,'3','5','kjdsfbslf','2023-04-20'),
(2,'3','7','hello','2023-04-20'),
(3,'7','3','hi','2023-04-20'),
(4,'7','3','hellllo','2023-04-20'),
(5,'7','3','fghjk','2023-04-20'),
(6,'7','3','yyjko89j','2023-04-20'),
(7,'3','5','hjk\r\n','2023-04-20'),
(8,'7','3','hloooo','2023-04-20'),
(9,'3','7','yess tell me','2023-04-20'),
(10,'7','3','hlooo','2023-05-15'),
(11,'3','6','hloo','2023-05-15'),
(12,'3','7','yes tell me','2023-05-15');

/*Table structure for table `chatbot` */

DROP TABLE IF EXISTS `chatbot`;

CREATE TABLE `chatbot` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `question` varchar(500) DEFAULT NULL,
  `answers` text,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `chatbot` */

insert  into `chatbot`(`cid`,`uid`,`question`,`answers`) values 
(1,7,'hello','hi'),
(2,7,'good morning','good morning'),
(3,7,'who are you','I am a chatbot'),
(4,7,'how old are you','I am 21'),
(5,7,'hw oldr u','Sorry, I can not understand the question'),
(6,7,'hloo','Sorry, I can not understand the question'),
(7,7,'hai','Sorry, I can not understand the question'),
(8,7,'Hi','Hello'),
(9,7,'Thank you','you are welcome'),
(10,7,'Who are you','I am a chatbot'),
(11,3,'Hi','Hello'),
(12,7,'hello','hi'),
(13,7,'Are there any dietary restrictions for individuals with heart failure?','Depending on the severity of the condition, individuals with heart failure may be advised to limit t'),
(14,7,'Are there any dietary restrictions for individuals with heart failure?','Depending on the severity of the condition, individuals with heart failure may be advised to limit t'),
(15,7,'hi','Sorry, I can not understand the question'),
(16,7,'Hi','Hello'),
(17,7,'Hi','Hello'),
(18,7,'What is heart failure?','Heart failure is a chronic condition where the heart’s ability to pump blood efficiently is impaired, resulting in symptoms such as fatigue, shortness of breath, and fluid retention.\r\n'),
(19,7,'What are the warning signs or symptoms of worsening heart failure?','Symptoms of worsening heart failure can include increased shortness of breath, fatigue, persistent coughing or wheezing, rapid weight gain, swelling in the legs or ankles, and increased heart rate. It’s important to promptly report any concerning symptoms to a healthcare professional for evaluation and management.'),
(20,7,'hi','Sorry, I can not understand the question'),
(21,7,'hi','Sorry, I can not understand the question'),
(22,7,'hi','Hello');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`id`,`lid`,`complaint`,`date`,`reply`) values 
(1,5,'asdfghjndfgh',NULL,'zsdxfdtgfyhfty'),
(4,7,'sdfghj','2023-04-20','gu'),
(5,0,'bhbjnkk',NULL,NULL),
(6,7,'qwertyui','2023-04-20','pending'),
(7,7,'tooo slow','2023-04-20','pending'),
(8,7,'lkoiuj00000','2023-05-15','pending'),
(9,7,'12345','2023-05-15','pending'),
(10,7,'jjkhllhh6p','2023-05-15','pending'),
(11,3,'bad service','2023-05-20','pending');

/*Table structure for table `datasets` */

DROP TABLE IF EXISTS `datasets`;

CREATE TABLE `datasets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(100) DEFAULT NULL,
  `answer` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

/*Data for the table `datasets` */

insert  into `datasets`(`id`,`question`,`answer`) values 
(1,'who are you','I am a chatbot'),
(2,'hi','Hello'),
(3,'hello','hi'),
(4,'how old are you','I am 21'),
(5,'are you happy','Yes i am'),
(6,'thank you','you are welcome'),
(7,'where are you from','I am from hfps '),
(8,'are you there','Yes i am here'),
(9,'good morning','good morning'),
(10,'take care','bye'),
(35,'are there any dietary restrictions for individuals with heart failure?','Depending on the severity of the condition, individuals with heart failure may be advised to limit their sodium (salt) intake to manage fluid retention. They may also be recommended to follow a heart-healthy diet, which includes consuming nutrient-rich foods, reducing saturated and trans fats, and limiting added sugars and processed foods.'),
(36,'what is heart failure?','Heart failure is a chronic condition where the heart’s ability to pump blood efficiently is impaired, resulting in symptoms such as fatigue, shortness of breath, and fluid retention.\r\n'),
(37,'what are the risk factors for heart disease?','Risk factors for heart disease include high blood pressure, high cholesterol, smoking, obesity, diabetes, and a family history of heart problems'),
(38,'what is a heart attack?','A heart attack occurs when the blood flow to a section of the heart muscle becomes blocked, usually due to a blood clot, resulting in damage or death of the affected heart tissue.'),
(39,'what are the common symptoms of a heart attack?','Common symptoms of a heart attack include chest pain or discomfort, shortness of breath, nausea, lightheadedness, and pain radiating to the arm, neck, jaw, or back.'),
(40,'how is high blood pressure linked to heart disease?',': High blood pressure puts strain on the heart and blood vessels, increasing the risk of heart disease, heart attack, and stroke.'),
(41,'what is arrhythmia?','Arrhythmia refers to an irregular heartbeat.'),
(42,'can stress affect heart health?','Yes, prolonged or chronic stress can contribute to high blood pressure, heart disease, and other cardiovascular problems.'),
(43,'how does cholesterol impact heart health?','High levels of LDL (low-density lipoprotein) cholesterol, often referred to as\r\n\r\n\"bad\" cholesterol, can lead to plaque buildup in the arteries, increasing the risk of heart disease.'),
(44,'is a Heart failure a normal consequence of getting old?','Heart Failure can affect all age groups. Most people with heart failure are elderly; however, heart failure isn’t necessarily a consequence of age. It’s a serious cardiovascular condition that can often be prevented and managed well with available treatment options.'),
(45,'what is the consequence of not availing timely treatment?','Heart failure is a serious, chronic condition that gradually worsens over time. Eventually, it can shorten your life. Starting the medical treatment on noticing symptoms can help manage the same.\r\n'),
(46,'what are the dietary restrictions?','Limiting sugary, fatty and salty meals and snacks\r\nConsume green leafy vegetables, wholegrain, fruit, nuts, and seeds every day,\r\nChoosing healthier fats and cooking oils such as olive oil,\r\nUsing herbs and spices to flavor food instead of salt'),
(47,'what are the warning signs or symptoms of worsening heart failure?','Symptoms of worsening heart failure can include increased shortness of breath, fatigue, persistent coughing or wheezing, rapid weight gain, swelling in the legs or ankles, and increased heart rate. It’s important to promptly report any concerning symptoms to a healthcare professional for evaluation and management.'),
(48,'is driving safe for a person with heart failure?','Most people can safely drive however if there is a history of fainting due to abnormal heart rhythm then consultation with the doctor is necessary. Refrain from driving a heavy goods vehicle or public transport.'),
(49,' can heart failure be cured?	','While heart failure is a chronic condition that currently has no cure, with appropriate medical management and lifestyle changes, individuals with heart failure can often lead fulfilling lives and effectively manage their symptoms.'),
(51,NULL,NULL);

/*Table structure for table `expert` */

DROP TABLE IF EXISTS `expert`;

CREATE TABLE `expert` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `expert` */

insert  into `expert`(`id`,`lid`,`name`,`place`,`post`,`pin`,`email`,`phno`) values 
(3,3,'anu','kannur','kuttikol','2345','banu11@gmail.com','7845436472'),
(4,13,'teena','knr','pnr','670307','teena@gmail.com','9876543456');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`id`,`lid`,`feedback`,`date`) values 
(1,5,'fghjk','12/12/12'),
(2,7,'sdfghj','2023-04-20'),
(3,7,'cvbn','2023-04-20'),
(4,7,'kljjryry','2023-04-20');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `utype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`uname`,`password`,`utype`) values 
(1,'admin','123','admin'),
(3,'anu231','231','expert'),
(4,'riya','123','user'),
(6,'ram21','21','user'),
(7,'malu345','345','user'),
(8,'dris','123','user'),
(9,'tanu','1234','user'),
(10,'kkk','1234','user'),
(11,'dfg11','55','user'),
(12,'asdfg','Abcghtd@11','user'),
(13,'teena','Malavika@11','expert');

/*Table structure for table `tip` */

DROP TABLE IF EXISTS `tip`;

CREATE TABLE `tip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tip` text,
  `exid` int(11) NOT NULL,
  PRIMARY KEY (`id`,`exid`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `tip` */

insert  into `tip`(`id`,`tip`,`exid`) values 
(1,'Adopt a balanced diet: Focus on consuming a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats. Minimize your intake of processed foods, saturated and trans fats, sodium, and added sugars.',3),
(2,'Regular physical activity: Engage in moderate-intensity aerobic exercises like brisk walking, cycling, swimming, or jogging for at least 150 minutes per week. Include strength training exercises two days a week to improve overall cardiovascular health.',3),
(4,'jjk',1),
(5,' Maintain a healthy weight: Aim for a body mass index (BMI) within the normal range (18.5-24.9). Excess weight, particularly around the waist, can increase the risk of heart disease.',3),
(6,'Avoid smoking and limit alcohol consumption: Smoking damages blood vessels and significantly increases the risk of heart disease. If you consume alcohol, do so in moderation (up to one drink per day for women and up to two drinks per day for men).',3),
(7,'Manage stress: Chronic stress can contribute to heart disease. Practice stress management techniques such as deep breathing exercises, meditation, yoga, or engaging in activities you enjoy.',3),
(8,'Get quality sleep: Aim for 7-9 hours of restful sleep each night. Poor sleep is associated with an increased risk of high blood pressure, obesity, and heart disease.\r\n',3),
(9,'Control blood pressure and cholesterol levels: Regularly monitor and manage your blood pressure and cholesterol levels with the help of your healthcare provider. Follow their recommendations regarding medication, lifestyle changes, and dietary modifications.',3),
(10,'Limit sodium intake: Excessive sodium consumption can raise blood pressure. Avoid adding extra salt to your meals and limit processed and packaged foods, as they often contain high amounts of sodium.',3),
(11,'Develop Good Sleep Hygiene\r\nTo improve your sleep, adopt a bedtime routine:\r\n\r\n•Go to bed and wake up at the same time every day, even on weekends.\r\n• Keep your room dark and cool.',3),
(12,'not smoking, eating fruits and vegetables (4 servings/d), and moderate alcohol intake (1 drink/d).',3),
(13,'Specific medicines that lower blood pressure and are also effective in lowering heart failure risk include diuretics, angiotensin-converting enzyme inhibitors, angiotensin receptor blockers, and ?-blockers.',3),
(14,'The earlier action is taken, the better the outcome',3),
(15,'Regular physical activity (exercising <5 d/wk) and maintaining a health body weight are key ingredients to preventing heart fail',3),
(16,'heavy alcohol/binge drinking and cocaine/amphetamine abuse can lead to heart failure and other health problems and thus should be avoided',3);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(500) DEFAULT NULL,
  `lname` varchar(500) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(500) DEFAULT NULL,
  `place` varchar(500) DEFAULT NULL,
  `post` varchar(500) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`lid`,`fname`,`lname`,`age`,`gender`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,5,'anju','sdfg',21,'f','knr','pnr',670307,8976789876,'anju@gmail.com'),
(2,6,'ram','rk',21,'male','kannur','kannur',6584,9846372165,'hagsh2@gmail.com'),
(3,7,'malu','B',21,'on','PAYYANNUR','RAMANTHALI',670305,9846372865,'hssh2@gmail.com'),
(4,8,'drishya','k',21,'on','kannur','kannur',670778,5987643225,'dris2@gmail.com'),
(5,9,'tanu','pradeep',45,'on','tirur','malapuram',670141,97,'gjejenm@hen'),
(6,10,'teena','2345',45,'on','f56','r5',670307,67675,'teena@gmail.com'),
(7,11,'53333','4567',1000,'on','36333','55555',667098,55258,'sss@gmail.com'),
(8,12,'ert','dfgh',44,'on','dfghj','dfgh',670307,7878909654,'sdf@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
