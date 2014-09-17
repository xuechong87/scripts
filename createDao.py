#coding:utf-8
'''
Created on 2014年8月29日
@author: xuechong
'''

if __name__ == '__main__':
    try:
        outputFolder = "F:/DAOS/"
        classNames = []
        packageName = ''
        template = 'package ' + packageName +'.dao;\n\n'+\
        'import org.springframework.data.jpa.repository.JpaSpecificationExecutor;\n'+\
        'import org.springframework.data.repository.PagingAndSortingRepository;\n'+\
        'import ' + packageName + '.entity.${className};\n\n' +\
        'public interface ${className}Dao extends PagingAndSortingRepository<${className}, String>,' +\
        'JpaSpecificationExecutor<${className}>{\n\n' +\
        '}'
            
        for _className in classNames:
            content = template.replace('${className}', _className)
            _fileName = outputFolder + _className + 'Dao.java'
            _file = open( _fileName,"w")
            print(_fileName)
            _file.write(content)
            _file.flush()
            _file.close()
        pass
    except Exception, e:
        print(e)
    
        
        
        
        
        
        
        
        
        
    
