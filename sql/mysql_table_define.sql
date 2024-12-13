-- 查询某个表的所有字段
SELECT 
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
   ) constraints,
   t.* 
FROM INFORMATION_SCHEMA.COLUMNS t 
WHERE table_name = 'TABLE_NAME'
ORDER BY ordinal_position ;


-- 查询库中包含某个字段的表

SELECT 
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
   ) constraints,
   t.* 
FROM INFORMATION_SCHEMA.COLUMNS t 
WHERE t.column_name='COLUMN'
ORDER BY table_name ASC ;