# coding: utf-8
'''
Created on 2013-7-23
folder:F:\tests
filetype:txt
origin:cccd
replacemnt:xxxxxxxxxxxxxxxy

@author: xuechong

use python 32+ please
'''

import os
import re


def execute(path,origin,replacement,regexp="^\S*.txt$"):
    path = os.path.abspath(path)
    mat = lambda x : re.compile(regexp).match(x.replace(' ','').lower())
    for _path in os.listdir(path):
        _path = str(_path)
        absPath = path  + os.path.sep + _path
        
        if mat(_path):
            replaceStr(absPath,origin,replacement)
            
        if os.path.isdir(absPath):
            execute(absPath,origin,replacement,regexp)
        
def replaceStr(filePath,origin,replacement):
    file_ = open(filePath,"r+",-1,"utf-8")
    text = file_.read()
    file_.close()
    dest =  open(filePath,"w",-1,"utf-8")
    dest.write(re.sub(origin, replacement, text))
    dest.flush()
    dest.close()
    
if __name__ == '__main__':
    dest_path = str(input("folder"))
    regexp = "^\S*." + str(input("filetype")) + "$"
    origin = str(input("origin"))
    replace = str(input("replacemnt"))
    execute(path=dest_path,
            regexp=regexp,
            origin=origin,
            replacement=replace)
    pass
