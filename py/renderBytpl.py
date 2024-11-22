
#coding:utf-8
'''
Created on 2014年8月29日
@author: xuechong
'''

if __name__ == '__main__':
    try:
        
        configList = [
            {'card_key':'attachment', 'card_content':'opinion'},
        ]
        template = '''
        group_concat( case card_key 
		when '{card_key}' then json_extract(card_content,'$.{card_content}')
	    end ) as {card_key}_{card_content}
        '''
            
        for cfg in configList:
            content = template.replace('{card_key}', cfg['card_key'])
            content = content.replace('{card_content}', cfg['card_content'])
            print(content)

        pass
    except Exception as e:
        print(e)
    
        
        
        
        
        
        
        
        
        
    
