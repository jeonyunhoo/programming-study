create user 'user1'@'localhost'
identified by 'sql123';

grant select, insert on order_t to 'user1'@'localhost';

revoke insert on order_t from 'user1'@'localhost';
show grants for 'user1'@'localhost';

set autocommit = 0;
-- set autocommit = false; 동일함

-- 트랜젝션 시작 -> 변경 -> 복구 지점 설정
start transaction;

update order_t
set price = 20000
where order_id = 'O1003';

select * from order_t;
savepoint P1;

-- 삭제 이후 P1으로 복구
set SQL_SAFE_UPDATES = 0; -- 안전 모드 비활성화

delete from order_t
where order_id = 'O1003';

select * from order_t;

rollback to P1;

commit;

drop user 'user1'@'localhost';
show grants;