# Host: localhost  (Version: 5.7.26)
# Date: 2021-12-03 15:10:07
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "transport_billing_data_table"
#

DROP TABLE IF EXISTS `transport_billing_data_table`;
CREATE TABLE `transport_billing_data_table` (
  `船名` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `航次` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `提单号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `IMO号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `国籍` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `启运港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `目的港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `起运港ETA` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `起运港ATB` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `起运港ATD` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `目的港ETA` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `货物类型` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `客户名称` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `船代公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `提单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `保函` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `签单要求` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `快递单号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `作业公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `报关公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `地面公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `绑扎公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `通关单号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `到货时间` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `到期到齐` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `发货状态` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `船东名称` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `出单方式` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `海运条款` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `货名` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `件数` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `重量` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `体积` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `计费吨` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `发货人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `收货人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `通知人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `唛头` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `货描` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `保险` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `递载费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `报关费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `改单费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `分票费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `电放费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `熏蒸费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `其他` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `预计开船日` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `装货港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `卸货港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `目的地` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `箱型` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `箱量` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `箱号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `品名` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `发票抬头` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `填制日期` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `铅封号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `委托单位` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `业务员` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `代理电话` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `下货纸` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `散货结算单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `散货确认单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `产装通知` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `集装结算单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `集装确认单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `集港通知` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `提单样本` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `装箱委托书` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user1` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user2` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user3` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

#
# Data for table "transport_billing_data_table"
#

/*!40000 ALTER TABLE `transport_billing_data_table` DISABLE KEYS */;
INSERT INTO `transport_billing_data_table` VALUES ('KSL DANYANG','DY2106','V111','12312321',NULL,'XINGANG','UMM QASR,IRAQ',NULL,NULL,NULL,NULL,'钢管','锐金','盛唐',NULL,NULL,NULL,NULL,NULL,'乾航','和洋','善水',NULL,NULL,NULL,'报关','耀洋','正文','FILO','SMLS STEEL PIPE','26 PACKAGES','39822 KGS','24.90CBM','39822 KGS','THREEWAY STEEL CO., LTD.                                      \nSTEEL INDUSTRIAL ZONE,TIANXIN DISTRICT,NO.9 XIANGFU RD,CHANGSHA ,HUNAN ,CHINA','MATAF AL-BAHAR COMPANY\nIRAQ.BASRA.AL-JAZAAR.KUT AL-HEJAJ\nTEL 07801105249 07707093096 07702211722 07733035553\nNUMBER TAX/90100572  EMAIL:MUSLEMALASADY@YAHOO.COM','SAME AS CONSIGNEE','N/M\n','SMLS STEEL PIPE\n\nCLEAN ON BOARD\nFREIGHT PREPAID',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-09-06-16:57.03','2021-10-12-10:04.50','2021-10-12-10:04.50',NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL),('VV2','V2','V222','231312313',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-09-06-17:04.13',NULL,'2021-09-06-17:04.13',NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL),('CS','12','CS1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL),('ZHONG SHAN MEN','V2','ZSM90283012830',NULL,NULL,'CHANGSHU','LAGOS',NULL,NULL,NULL,NULL,NULL,'锐金','瑞达',NULL,NULL,NULL,NULL,NULL,NULL,'大正','善水',NULL,NULL,NULL,NULL,'中源',NULL,NULL,'STEEL PIPE','3125','1000MT','2000CBM','2000CBM','ASDFGHJK','SDFG4423','GF4324',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-10-12-10:08.39','2021-10-12-10:08.39',NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL),('AAL','12','AAL131',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'13',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL),('DASJDAHJF','V1002','DASJ4564564',NULL,NULL,'TIANJIN','AQABA',NULL,NULL,NULL,NULL,NULL,NULL,'盛唐',NULL,NULL,NULL,NULL,NULL,NULL,'瑞涛','善水',NULL,NULL,NULL,NULL,'COSCO',NULL,NULL,'STEEL PIPE','45646','300','415','415','HUNAN','ABCC','ABCC',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-10-12-10:32.46','2021-10-12-10:32.46','2021-10-12-10:32.46',NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL),('U RICH','PG2151','TJDMM005',NULL,NULL,'XINGANG SEAPORT, CHINA','DAMMAM SEAPORT, SAUDI ARABIA','2021-10-12','2021-10-12',NULL,NULL,'钢管','荣锐','盛唐',NULL,NULL,NULL,NULL,'临港4','乾航','和洋','船公司',NULL,'2021-10-12','2021-10-12','已到齐','耀洋',NULL,'FILO','ERW STEEL PIPE','238','348.697',NULL,NULL,'TIANJIN UNIGLORY INTERNATIONAL\nTRADE CO. LTD. NO. 50 YOUYI RD. HEXI\nDISTRICT, SUITE A1103, FRIENDSHIP\nMANSION, TIANJIN, P.R. CHINA\nTEL: +86(22)88371185, FAX: +86(22)88371101','NATIONAL FOUNDRY COMPANY.\nP.O. 11383 RIYADH, B.O. 355404,\nSAUDI ARABIA. TEL: +966114986022\nFAX: +966114986336','NATIONAL FOUNDRY COMPANY.\nP.O. 11383 RIYADH, B.O. 355404,\nSAUDI ARABIA. TEL: +966114986022\nFAX: +966114986336','N/M','ERW STEEL PIPE',NULL,'300','150',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-10-12-11:13.10',NULL,'2021-10-12-11:13.10',NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL),('DASDA','1232','31231','312313','1231','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'','','',NULL,NULL,NULL,NULL,NULL,NULL,'hxx',NULL,NULL),('NEW FAIRY','2110','SGPLG28','UN9560003','中国香港','临港4','新加坡','2021-10-29',NULL,NULL,NULL,'钢管','包头','瑞达',NULL,NULL,NULL,NULL,NULL,'乾航','大正','船公司',NULL,NULL,NULL,NULL,'长凯',NULL,'FOB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL),('TOMINI INTEGRITY','V2769','2769THS101','UN9512630','马绍尔群岛','汇盛','新加坡',NULL,NULL,NULL,NULL,'钢管','惠利通','庆洋',NULL,NULL,NULL,NULL,NULL,'乾航','云盛','鑫海',NULL,NULL,NULL,'放行',NULL,'电放','FOB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-10-27-17:43.54',NULL,NULL,NULL,NULL,NULL,NULL,'zjq',NULL,NULL);
/*!40000 ALTER TABLE `transport_billing_data_table` ENABLE KEYS */;

#
# Structure for table "transport_billing_jizhuangxiang_data_table"
#

DROP TABLE IF EXISTS `transport_billing_jizhuangxiang_data_table`;
CREATE TABLE `transport_billing_jizhuangxiang_data_table` (
  `船名` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `航次` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `提单号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `预计开船日` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `启运港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `装货港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `卸货港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `目的地` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `箱型` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `箱量` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `箱号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `品名` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `发票抬头` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `填制日期` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `铅封号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `委托单位` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `业务员` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `代理电话` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `发货状态` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `出单方式` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `货名` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `件数` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `重量` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `体积` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `计费吨` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `发货人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `收货人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `通知人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `唛头` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `货描` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `产装通知` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `集装结算单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `集装确认单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `集港通知` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `提单样本` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `装箱委托书` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user2` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

#
# Data for table "transport_billing_jizhuangxiang_data_table"
#

/*!40000 ALTER TABLE `transport_billing_jizhuangxiang_data_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `transport_billing_jizhuangxiang_data_table` ENABLE KEYS */;

#
# Structure for table "transport_billing_sanhuo_data_table"
#

DROP TABLE IF EXISTS `transport_billing_sanhuo_data_table`;
CREATE TABLE `transport_billing_sanhuo_data_table` (
  `船名` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `航次` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `提单号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `IMO号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `国籍` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `启运港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `目的港` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `起运港ETA` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `起运港ATB` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `起运港ATD` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `目的港ETA` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `货物类型` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `客户名称` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `船代公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `提单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `保函` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `签单要求` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `快递单号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `作业公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `报关公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `地面公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `绑扎公司` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `通关单号` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `到货时间` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `到期到齐` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `发货状态` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `船东名称` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `出单方式` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `海运条款` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `货名` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `件数` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `重量` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `体积` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `计费吨` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `发货人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `收货人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `通知人` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `唛头` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `货描` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `保险` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `递载费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `报关费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `改单费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `分票费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `电放费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `熏蒸费` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `其他` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `下货纸` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `散货结算单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `散货确认单` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user1` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

#
# Data for table "transport_billing_sanhuo_data_table"
#

/*!40000 ALTER TABLE `transport_billing_sanhuo_data_table` DISABLE KEYS */;
INSERT INTO `transport_billing_sanhuo_data_table` VALUES ('NEW FAIRY','2110','SGPLG28','UN9560003','中国香港','临港4','新加坡','2021-10-29',NULL,NULL,NULL,'钢管','包头','瑞达',NULL,NULL,NULL,NULL,NULL,'乾航','大正','船公司',NULL,NULL,NULL,NULL,'长凯',NULL,'FOB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'zjq'),('TOMINI INTEGRITY','V2769','2769THS101','UN9512630','马绍尔群岛','汇盛','新加坡',NULL,NULL,NULL,NULL,'钢管','惠利通','庆洋',NULL,NULL,NULL,NULL,NULL,'乾航','云盛','鑫海',NULL,NULL,NULL,'放行',NULL,'电放','FOB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-10-27-17:43.54','zjq'),('DASDA','1232','31231','312313','1231','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','hxx');
/*!40000 ALTER TABLE `transport_billing_sanhuo_data_table` ENABLE KEYS */;

#
# Structure for table "user_password_table"
#

DROP TABLE IF EXISTS `user_password_table`;
CREATE TABLE `user_password_table` (
  `user` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `grade` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  UNIQUE KEY `user` (`user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

#
# Data for table "user_password_table"
#

/*!40000 ALTER TABLE `user_password_table` DISABLE KEYS */;
INSERT INTO `user_password_table` VALUES ('admin','admin','1'),('zjq','zjq','2'),('hxx','hxx','2'),('gql','gql','2');
/*!40000 ALTER TABLE `user_password_table` ENABLE KEYS */;
