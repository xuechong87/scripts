-- 查询某个表的所有字段
select 
t.ordinal_position,
t.column_comment,
t.column_name,
t.column_type,
concat_ws(',',
 (case 
 when column_key = 'PRI'
    then '主键' else null end),
    (case 
 when is_nullable = 'NO'
    then '非空' else null end)
),
t.* 
from INFORMATION_SCHEMA.COLUMNS t where table_name = 'TABLE_NAME'
order by ordinal_position ;


-- 查询库中包含某个字段的表

select 
t.table_name,
t.column_name,
t.column_type,
t.column_comment,

concat_ws(',',
 (case 
 when column_key = 'PRI'
    then '主键' else null end),
    (case 
 when is_nullable = 'NO'
    then '非空' else null end)
),
t.* 
from INFORMATION_SCHEMA.COLUMNS 
t where
t.column_name='COLUMN'
order by table_name asc ;