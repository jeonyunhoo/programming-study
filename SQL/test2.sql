alter table order_t
rename column destination to dest_code;

alter table order_t
modify dest_code varchar(256);

desc order_t;

create index idx_order_date on order_t(order_date);
alter table order_t drop index idx_order_date;
-- drop index idx_order_data on order_t

create view vw_order as
select count(*) as order_count, sum(price) as total_price
from order_t
group by cust_id;
select * from vw_order;

select cust_id, order_count, total_price
from vw_order
where total_price >= 50000;