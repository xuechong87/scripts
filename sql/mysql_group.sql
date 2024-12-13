-- 将多个类型合成一条数据

CREATE TABLE `test`.`group_test` (
  `id` VARCHAR(255) NOT NULL,
  `type` VARCHAR(45) NULL,
  `value_title` VARCHAR(45) NULL,
  `value_content` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
INSERT INTO `test`.`group_test` (`id`, `type`, `value_title`, `value_content`) VALUES ('1', 'a', '指标A', 'aaaaa');
INSERT INTO `test`.`group_test` (`id`, `type`, `value_title`, `value_content`) VALUES ('2', 'a', '指标B', 'bbbbbb');
INSERT INTO `test`.`group_test` (`id`, `type`, `value_title`, `value_content`) VALUES ('3', 'a', '指标C', 'ccccc');
INSERT INTO `test`.`group_test` (`id`, `type`, `value_title`, `value_content`) VALUES ('4', 'b', '指标A', '2aaaa');
INSERT INTO `test`.`group_test` (`id`, `type`, `value_title`, `value_content`) VALUES ('5', 'b', '指标B', '2bbbb');
INSERT INTO `test`.`group_test` (`id`, `type`, `value_title`, `value_content`) VALUES ('6', 'b', '指标C', '2CCC');


select 
	type,
	group_concat( case value_title 
		when '指标A' then value_content
	end ) as 指标A,
    group_concat( case value_title 
		when '指标B' then value_content
	end ) as 指标B,
    group_concat( case value_title 
		when '指标C' then value_content
	end ) as 指标C
    
from group_test t 
-- where type = 'a'
group by `type`