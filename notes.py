# coding: utf-8
'''
Created on 2014-1-21
@author: xuechong
'''
try:
    destFolder = "I:/GitHub/scripts/"
    origin = "I:/GitHub/scripts/" + "tests.txt"
    #origin = os.getcwd() + os.sep + "tests.txt"
    import os
    
    txtCache = dict()
    txt = open(origin)
    
    def puts (head,con):
        if txtCache.get(head):
            txtCache.get(head).append(con)
        else:
            txtCache[head] = [con,]
    
    for blok in txt.read().split("========\n"):
        splits = blok.split("\n")
        print(splits)
        if(splits[0]):
            head = str(splits[0])
            puts(splits[0],"".join(splits[1:]))
            
    for k in txtCache.keys():
        if k:
            fi = open((destFolder + os.sep + k + ".txt").decode("utf8"),"w")
            fi.write("\n".join(txtCache.get(k)))
            fi.close()
    txt.close()
    pass
    
except Exception,e:
    print(e)
print ("end")
input("exit")
