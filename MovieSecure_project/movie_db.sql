create database movie_db;

use movie_db;

create table member(

	m_id int primary key auto_increment,
    user_id varchar(30) not null unique,
    user_password varchar(255) not null,
    m_name varchar(30) not null,
    m_role varchar(10) not null default 'USER',
    create_at datetime default current_timestamp
);

desc member;

insert into member(user_id, user_password, m_name)
values
	('hong', '1234', '홍길동'),
	('kim', '5678', '김유신'),
    ('heo', '7777', '허준'),
    ('jeong', '9999', '정약용');
    
select * from member;

insert into member(user_id, user_password, m_name, m_role)
values('admin', 'admin1234', '관리자', 'ADMIN');

select * from member;