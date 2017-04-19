/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2017/4/17 13:23:30                           */
/*==============================================================*/


drop table if exists complaint;

drop table if exists complaint_type;

drop table if exists department;

drop table if exists discount;

drop table if exists discount_type;

drop table if exists discountlist;

drop table if exists employee;

drop table if exists item;

drop table if exists memberacc;

drop table if exists purchase;

drop table if exists purchlist;

drop table if exists salary;

drop table if exists shelf;

drop table if exists shelflist;

drop table if exists shoplist;

drop table if exists shopping;

drop table if exists staffacc;

drop table if exists staffacc_authtype;

drop table if exists storage;

drop table if exists storelist;

drop table if exists supplieracc;

/*==============================================================*/
/* Table: complaint                                             */
/*==============================================================*/
create table complaint
(
   comp_id              bigint not null AUTO_INCREMENT,
   mem_id               bigint,
   comp_type            numeric(1,0) not null,
   comp_ctnt            text not null,
   comp_time            datetime not null,
   primary key (comp_id)
);

/*==============================================================*/
/* Table: complaint_type                                        */
/*==============================================================*/
create table complaint_type
(
   comp_type        numeric(1,0) not null,
   comp_type_name   text not null,
   primary key (comp_type)
);

/*==============================================================*/
/* Table: department                                            */
/*==============================================================*/
create table department
(
   dept_id              numeric(2,0) not null,
   dept_name            text not null,
   empl_id              bigint not null,
   primary key (dept_id)
);

/*==============================================================*/
/* Table: discount                                              */
/*==============================================================*/
create table discount
(
   disc_id              bigint not null,
   disc_type_id         numeric(1,0) not null,
   disc_title           varchar(20) binary,
   disc_desc            text,
   disc_dom             bool,
   disc_btime           datetime,
   disc_etime           datetime,
   disc_note            text,
   primary key (disc_id)
);

/*==============================================================*/
/* Table: discount_type                                         */
/*==============================================================*/
create table discount_type
(
   disc_type_id         numeric(1,0) not null,
   disc_type_name       text not null,
   primary key (disc_type_id)
);

/*==============================================================*/
/* Table: discountlist                                          */
/*==============================================================*/
create table discountlist
(
   disc_id              bigint,
   item_code            bigint
);

/*==============================================================*/
/* Table: employee                                              */
/*==============================================================*/
create table employee
(
   empl_id              bigint not null,
   dept_id              numeric(2,0),
   empl_name            text not null,
   empl_idcnum          text not null,
   empl_mobi            text,
   empl_resi            text,
   empl_addr            text,
   empl_pos             text,
   empl_hiredate        date,
   empl_note            text,
   primary key (empl_id)
);

/*==============================================================*/
/* Table: item                                                  */
/*==============================================================*/
create table item
(
   item_code            bigint not null,
   item_desc            text not null,
   item_spec            text not null,
   item_cate            text not null,
   item_brand           text not null,
   item_price           float(8,2) not null,
   item_manudate        date,
   item_expidate        date,
   item_note            text,
   primary key (item_code)
);

/*==============================================================*/
/* Table: memberacc                                             */
/*==============================================================*/
create table memberacc
(
   mem_id               bigint not null AUTO_INCREMENT,
   mem_name             text not null,
   mem_psw              text not null,
   mem_pnum             text,
   mem_mail             text,
   mem_rtime            datetime not null,
   mem_point            int not null,
   mem_avai             bool not null,
   mem_note             text,
   primary key (mem_id)
);

/*==============================================================*/
/* Table: purchase                                              */
/*==============================================================*/
create table purchase
(
   shop_id              bigint not null,
   supp_id              bigint,
   empl_id              bigint,
   shop_time            datetime not null,
   shop_note            text,
   primary key (shop_id)
);

/*==============================================================*/
/* Table: purchlist                                             */
/*==============================================================*/
create table purchlist
(
   item_code            bigint not null,
   shop_id              bigint not null,
   purch_unitprice      float(8,2) not null,
   purch_unitnum        int not null,
   primary key (item_code, shop_id)
);

/*==============================================================*/
/* Table: salary                                                */
/*==============================================================*/
create table salary
(
   salary_id            bigint not null,
   empl_id              bigint not null,
   emp_empl_id          bigint not null,
   salary_amnt          float(8,2),
   salary_time          datetime,
   primary key (salary_id)
);

/*==============================================================*/
/* Table: shelf                                                 */
/*==============================================================*/
create table shelf
(
   shelf_id             int not null,
   shelf_desc           text not null,
   empl_id              bigint,
   primary key (shelf_id)
);

/*==============================================================*/
/* Table: shelflist                                             */
/*==============================================================*/
create table shelflist
(
   item_code            bigint not null,
   shelf_id             int not null,
   shelf_num            int not null,
   primary key (item_code, shelf_id)
);

/*==============================================================*/
/* Table: shoplist                                              */
/*==============================================================*/
create table shoplist
(
   item_code            bigint not null,
   shop_id              bigint not null,
   item_unitprice       float(8,2) not null,
   item_unitnum         int not null,
   primary key (item_code, shop_id)
);

/*==============================================================*/
/* Table: shopping                                              */
/*==============================================================*/
create table shopping
(
   shop_id              bigint not null,
   mem_id               bigint,
   empl_id              bigint not null,
   shop_time            datetime not null,
   shop_acce            numeric(1,0),
   shop_note            text,
   primary key (shop_id)
);

/*==============================================================*/
/* Table: staffacc                                              */
/*==============================================================*/
create table staffacc
(
   empl_id              bigint not null,
   staff_psw            text not null,
   staff_atype_id       int not null,
   staff_regi           datetime not null,
   staff_avai           bool not null,
   staff_note           text,
   primary key (empl_id)
);

/*==============================================================*/
/* Table: staffacc_authtype                                     */
/*==============================================================*/
create table staffacc_authtype
(
   staff_atype_id       int not null,
   staff_atype_name     text not null,
   primary key (staff_atype_id)
);

/*==============================================================*/
/* Table: storage                                               */
/*==============================================================*/
create table storage
(
   stor_id              int not null,
   stor_desc            text not null,
   empl_id              bigint,
   primary key (stor_id)
);

/*==============================================================*/
/* Table: storelist                                             */
/*==============================================================*/
create table storelist
(
   item_code            bigint not null,
   stor_id              int not null,
   number               int not null,
   primary key (item_code, stor_id)
);

/*==============================================================*/
/* Table: supplieracc                                           */
/*==============================================================*/
create table supplieracc
(
   supp_id              bigint not null,
   supp_usname          varchar(15) not null,
   supp_pswd            varchar(20) not null,
   supp_regtime         datetime,
   supp_cname           varchar(10),
   supp_mobinum         varchar(15),
   supp_email           varchar(30),
   supp_addr            varchar(60),
   supp_avai            bool,
   supp_note            text,
   primary key (supp_id)
);

INSERT INTO memberacc VALUES(1,'sgz','bangbang','15201752137','bangbang@fudan.cn','2017-4-1',0,true,'');
INSERT INTO memberacc VALUES(2,'wps','peigong','15333333333','peigong@fudan.cn','2017-4-2',0,true,'');
INSERT INTO memberacc VALUES(3,'zcg','guangguang','13333333333','guanguang@fudan.cn','2017-4-3',0,true,'');
INSERT INTO memberacc VALUES(4,'zyn','xiaozheng','14444444444','xiaozhengyining@fudan.cn','2017-4-4',0,true,'');
INSERT INTO supplieracc VALUES(10,'xiaozheng','123','1111-1-1','123','21312312','asdasdasd','asdasdasd',true,'');

insert into staffacc values(15307130021,'wps',1,'2010-1-1',true,'');
insert into staffacc values(15307130224,'sgz',1,'2011-1-1',true,'');
insert into staffacc values(15307130096,'zcg',1,'2012-1-1',true,'');

/*
insert into item values (10001,'张曾光的亲笔书法','很大','古董','张曾光',88888.88,'2012-2-12','2020-2-12','');
insert into item values (10002,’蛇果阵的山地自行车’,’非常大’,’越野’,’急速’,28888.88,’2017-2-12’,’2020-2-12’,’’);
insert into item values (10003,’小郑的妹子’,’不可描述’,’妹子’,’小郑’,999999.99,’1996-2-12’,’2020-2-12’,’’);
insert into item values (10004,’mac电脑’,’挺大’,’电子产品’,’苹果’,120000.00,’2017-2-12’,’2020-2-12’,’’);
insert into item values (10005,’奥利奥饼干’,’小’,’食物’,’oreo’,15.88,’2017-4-12’,’2020-2-12’,’’);
insert into item values (10006,’数据库系统教程’,’小’,’书籍’,’高等教育出版社’,18.88,’2012-2-12’,’2020-2-12’,’’);
insert into item values (10007,’C+’,’较小’,’饮料’,’怡泉’,4.00,’2017-4-12’,’2020-2-12’,’’);
*/


