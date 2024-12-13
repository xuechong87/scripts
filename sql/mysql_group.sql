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


SELECT 
    type,
    COALESCE(GROUP_CONCAT(CASE value_title 
        WHEN '指标A' THEN value_content 
        END ), '无数据') AS 指标A,
    COALESCE(GROUP_CONCAT(CASE value_title 
        WHEN '指标B' THEN value_content 
        END ), '无数据') AS 指标B,
    COALESCE(GROUP_CONCAT(CASE value_title 
        WHEN '指标C' THEN value_content 
        END ), '无数据') AS 指标C
FROM group_test t 
-- where type = 'a'
GROUP BY `type`