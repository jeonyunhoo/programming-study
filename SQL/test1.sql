create database test;

use test;

show databases;

create table customer (

	cust_id varchar(16) primary key not null,
	cust_name varchar(50) not null,
    passward varchar(256) not null
);

desc customer;

create table order_t (

	order_id varchar(16) primary key not null,
    cust_id varchar(16) not null,
    order_date varchar(8) not null,
    price int not null,
    destination varchar(100),
    
    constraint fk_cust_id foreign key (cust_id) 
    references customer(cust_id) on delete cascade
);

desc order_t;

insert into customer (cust_id, cust_name, passward) values
('C0001', '홍길동', 'pass1234'),
('C0002', '이순신', 'pass5678'),
('C0003', '강감찬', 'pass9012');

insert into order_t (order_id, cust_id, order_date, price, destination) values
('O1001', 'C0001', '20260801', 15000, '서울'), 
('O1002', 'C0001', '20260803', 45000, '부산'),
('O1003', 'C0002', '20260805', 30000, '대전');

select * from customer;
select * from order_t;

select customer.cust_id, customer.cust_name, order_t.order_id, order_t.order_date, order_t.price
from customer
inner join order_t on customer.cust_id = order_t.cust_id
where customer.cust_name = '홍길동';

select cust_id, cust_name
from customer
where cust_id not in (
	select cust_id
    from order_t
);

select customer.cust_id, sum(order_t.price) as total_price
from customer
inner join order_t
on customer.cust_id = order_t.cust_id
group by customer.cust_id
having sum(order_t.price) >= 30000
order by total_price asc;

-- 연습
select c.cust_id, sum(o.price) as total_price
from customer as c
inner join order_t as o
on c.cust_id = o.cust_id
group by c.cust_id
having sum(o_t.price) >= 30000
order by total_price asc;