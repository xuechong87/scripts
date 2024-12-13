#coding:utf-8
import pymysql
import pandas as pd # 导入pandas库      

destFile = '/Users/xuechong/Desktop/output.xlsx'
conn2 = pymysql.connect(
    host='172.26.3.121',      # 数据库主机地址
    user='root',          # 数据库用户名
    password='vffcmMCkEUr',    # 数据库密码
    database='elcube_hbf_dev',      # 数据库名称
    charset='utf8',# 字符编码
    port=3306   
)

if __name__ == '__main__':
    try:
        
        configList = [
            {'card_key':'attachment', 'card_content':'opinion'},
            {'card_key':'CategoryBeneficial', 'card_content':'standard'},
            {'card_key':'CategoryBeneficial', 'card_content':'legalKindFour'},
            {'card_key':'CustomerAssessment', 'card_content':'effectiveness'}
        ]

        template = '''
        group_concat( case card_key 
		when '{card_key}' then json_extract(card_content,'$.{card_content}')
	    end ) as {card_key}_{card_content}
        ,'''    
        sql = '''
        select
        {selectquery}
        from nk_doc_i i 
        where doc_id in (select  doc_id from nk_doc_h where DOC_TYPE = 'FX01')
        group by doc_id 
        '''

        selectquery = ''
        for cfg in configList:
            content = template.replace('{card_key}', cfg['card_key'])
            content = content.replace('{card_content}', cfg['card_content'])
            selectquery += content

        selectquery= selectquery[:len(selectquery)-2]
        print(selectquery)
        sql = sql.replace('{selectquery}', selectquery)
        
        print(sql)


        # 创建游标对象
        cursor = conn2.cursor()   

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
        
        df.to_excel(destFile, index=False)
        # 打印总行数
        
        print("总导出行数:", len(df))
        print("数据已成功导出到Excel文件:" + destFile)

    except Exception as e:
        print("Error:", e)

    finally:
        # 关闭数据库连接
        cursor.close()
        conn2.close()
        pass
    
        