/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2017/4/15 23:18:37                           */
/*==============================================================*/


drop table if exists complaint;

drop table if exists complaint_type;

drop table if exists department;

drop table if exists discount;

drop table if exists discount_type;

drop table if exists discountlist;

drop index is_in_charge_of_FK2 on employee;

drop index is_in_charge_of_FK on employee;

drop table if exists employee;

drop index involves_FK on item;

drop table if exists item;

drop table if exists memberacc;

drop index partakes_in_FK on purchase;

drop index is_responsible_for_FK on purchase;

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
   comp_id              bigint not null,
   mem_id               bigint,
   discount_type        numeric(1,0) not null,
   comp_ctnt            text not null,
   comp_time            datetime not null,
   primary key (comp_id)
);

/*==============================================================*/
/* Table: complaint_type                                        */
/*==============================================================*/
create table complaint_type
(
   discount_type        numeric(1,0) not null,
   discount_type_name   text not null,
   primary key (discount_type)
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

alter table discount comment '设置该实体的目的是便于行政部门人员进行管理以及会员查看优惠信息；实际存储的“单价”是优惠价格而非原价。';

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
/* Index: is_in_charge_of_FK                                    */
/*==============================================================*/
create index is_in_charge_of_FK on employee
(
   
);

/*==============================================================*/
/* Index: is_in_charge_of_FK2                                   */
/*==============================================================*/
create index is_in_charge_of_FK2 on employee
(
   
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
/* Index: involves_FK                                           */
/*==============================================================*/
create index involves_FK on item
(
   
);

/*==============================================================*/
/* Table: memberacc                                             */
/*==============================================================*/
create table memberacc
(
   mem_id               bigint not null,
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
/* Index: is_responsible_for_FK                                 */
/*==============================================================*/
create index is_responsible_for_FK on purchase
(
   
);

/*==============================================================*/
/* Index: partakes_in_FK                                        */
/*==============================================================*/
create index partakes_in_FK on purchase
(
   
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

alter table shelflist comment '一个货架上可以有多种商品，一个商品也可以存放于多种货架；这是一个M:N联系，应以实体方式实现。';

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

alter table complaint add constraint FK_is_of foreign key (discount_type)
      references complaint_type (discount_type) on delete restrict on update restrict;

alter table complaint add constraint FK_makes foreign key (mem_id)
      references memberacc (mem_id) on delete restrict on update restrict;

alter table department add constraint FK_is_in_charge_of foreign key (empl_id)
      references employee (empl_id) on delete restrict on update restrict;

alter table discount add constraint FK_is_of foreign key (disc_type_id)
      references discount_type (disc_type_id) on delete restrict on update restrict;

alter table discountlist add constraint FK_Reference_27 foreign key (disc_id)
      references discount (disc_id) on delete restrict on update restrict;

alter table discountlist add constraint FK_Reference_28 foreign key (item_code)
      references item (item_code) on delete restrict on update restrict;

alter table employee add constraint FK_belongs_to foreign key (dept_id)
      references department (dept_id) on delete restrict on update restrict;

alter table purchase add constraint FK_Reference_22 foreign key (supp_id)
      references supplieracc (supp_id) on delete restrict on update restrict;

alter table purchase add constraint FK_Reference_23 foreign key (empl_id)
      references employee (empl_id) on delete restrict on update restrict;

alter table purchlist add constraint FK_Reference_24 foreign key (shop_id)
      references purchase (shop_id) on delete restrict on update restrict;

alter table purchlist add constraint FK_involves foreign key (item_code)
      references item (item_code) on delete restrict on update restrict;

alter table salary add constraint FK_handles foreign key (emp_empl_id)
      references employee (empl_id) on delete restrict on update restrict;

alter table salary add constraint FK_receives foreign key (empl_id)
      references employee (empl_id) on delete restrict on update restrict;

alter table shelf add constraint FK_Reference_26 foreign key (empl_id)
      references employee (empl_id) on delete restrict on update restrict;

alter table shelflist add constraint FK_put_on foreign key (item_code)
      references item (item_code) on delete restrict on update restrict;

alter table shelflist add constraint FK_put_on foreign key (shelf_id)
      references shelf (shelf_id) on delete restrict on update restrict;

alter table shoplist add constraint FK_involves foreign key (item_code)
      references item (item_code) on delete restrict on update restrict;

alter table shoplist add constraint FK_involves foreign key (shop_id)
      references shopping (shop_id) on delete restrict on update restrict;

alter table shopping add constraint FK_is_responsible_for foreign key (empl_id)
      references employee (empl_id) on delete restrict on update restrict;

alter table shopping add constraint FK_partakes_in foreign key (mem_id)
      references memberacc (mem_id) on delete restrict on update restrict;

alter table staffacc add constraint FK_is_of foreign key (staff_atype_id)
      references staffacc_authtype (staff_atype_id) on delete restrict on update restrict;

alter table staffacc add constraint FK_posssesses foreign key (empl_id)
      references employee (empl_id) on delete restrict on update restrict;

alter table storage add constraint FK_Reference_25 foreign key (empl_id)
      references employee (empl_id) on delete restrict on update restrict;

alter table storelist add constraint FK_is_stored_in foreign key (item_code)
      references item (item_code) on delete restrict on update restrict;

alter table storelist add constraint FK_is_stored_in foreign key (stor_id)
      references storage (stor_id) on delete restrict on update restrict;

