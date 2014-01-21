'''
Created on 2013-2-28
check the empty folder & remove
@author: xuechong87
'''
import os

def pathNotNull(pathStr):
    return len(os.listdir(pathStr))>0

def remove(pathStr):
    os.removedirs(pathStr)
    return

def execute(pathStr):
    if pathNotNull(pathStr)==False :
        remove(pathStr)
    return

def iterate(pathStr):
    flag = True
    if os.path.exists(pathStr)==False:
        print('path ' + pathStr + 'not exists')
        return
    while flag:
        flag = False
        if os.path.exists(pathStr):
            for f in os.listdir(pathStr):
                fPath = pathStr+ "\\" + f
                if os.path.exists(fPath) and os.path.isdir(fPath) :
                    if pathNotNull(fPath):
                        iterate(fPath)
                    else:
                        flag = True
                        print(fPath)
                        remove(fPath)
    return

if __name__=='__main__':
    '''
    flag = 'y'
    while(flag!='n'):
        folderPath = input('input path:')
        try:
            iterate(folderPath)
        except:
            print('erroe')
        print('finished!')
        flag=input('press n finish')
        '''
    iterate('F:\\')
    
    
   
   
    
