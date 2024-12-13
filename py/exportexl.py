# coding: utf-8
# 连接mysql数据库执行查询语句并导出为excel文件  

import pymysql
import pandas as pd # 导入pandas库          

# 连接数据库
#   conn = pymysql.connect(
#     host='localhost',      # 数据库主机地址
#     user='root',          # 数据库用户名
#     password='root@12345',    # 数据库密码
#     database='test',      # 数据库名称
#     charset='utf8'        # 字符编码
#   )

conn2 = pymysql.connect(
    host='172.26.3.121',      # 数据库主机地址
    user='root',          # 数据库用户名
    password='',    # 数据库密码
    database='',      # 数据库名称
    charset='utf8',# 字符编码
    port=3306   
)

try:
    # 创建游标对象
    cursor = conn2.cursor()
    
    # 执行SQL查询
    sql ='''
select 
	group_concat( case card_key 
		when 'attachment' then json_extract(card_content,'$.opinion')
	end ) as attachment_opinion,
    group_concat( case card_key 
		when 'CategoryBeneficial' then json_extract(card_content,'$.standard')
	end ) as CategoryBeneficial_standard,
    group_concat( case card_key 
		when 'CategoryBeneficial' then json_extract(card_content,'$.legalKindFour')
	end ) as CategoryBeneficial_legalKindFour,
    group_concat( case card_key 
		when 'CustomerAssessment' then json_extract(card_content,'$.effectiveness')
	end ) as CustomerAssessment_effectiveness,
    group_concat( case card_key 
		when 'CustomerAssessment' then json_extract(card_content,'$.effectiveness33')
	end ) as CustomerAssessment_effectiveness33
    
from nk_doc_i i 
where doc_id = '845649f5-40285dbd-0184-564ae629-0001'
group by doc_id
    '''  # 替换为您的查询语句

    cursor.execute(sql)
    
    # 获取所有记录
    results = cursor.fetchall()
    
     # 去掉字段内容最外层的双引号
    results = [[value.strip('"') if value !=None and isinstance(value, str)  else value for value in row] for row in results]
    
    # 获取列名
    columns = [desc[0] for desc in cursor.description]
    
    # 创建DataFrame
    df = pd.DataFrame(list(results), columns=columns)
    
    # 导出到Excel文件
    df.to_excel('/Users/xuechong/Desktop/output.xlsx', index=False)
    print("数据已成功导出到Excel文件")

except Exception as e:
    print("Error:", e)

finally:
    # 关闭数据库连接
    cursor.close()
    conn2.close()
