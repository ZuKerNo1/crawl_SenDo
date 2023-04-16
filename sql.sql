create database crawl_sd;

use crawl_sd;

create table product
(
	product_id int primary key,
    name_product varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
	price float,
    thumbnail_url varchar(1000),
    shop_name varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
);

