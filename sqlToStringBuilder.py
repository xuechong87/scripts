#coding:utf-8
'''
Created on 2014年8月29日
@author: xuechong
'''

if __name__ == '__main__':
    path = ''
    open(path)
    result = 'StringBuilder sql = new StringBuilder();\n'
    warp = lambda x :'sql.append("' + x.replace('"', '\\"').replace('\n',' ') + '");\n'
    for line in open(path).readlines():
        result = result + warp(line)
    print (result)
