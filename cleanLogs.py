#coding : utf-8

import os
import re

def cleanDir(_dirpath):

	for (_dirpath,_dirnames,_filenames) in os.walk(_dirpath):
		#print(_dirpath)
		if(_filenames):
			for _fileName in _filenames:
				_fullName = os.path.join(_dirpath,_fileName)
				_match = lambda x : re.compile(x).match(_fileName)
				if(_match("^.*\.log$") or _match("^.*\.log\.([^\.]*)$")):
					print(_fullName)
					os.remove(_fullName)

if __name__ == '__main__':
	try:
		cleanDir("/Users/xuechong/Desktop/hb")
	except Exception as e:
		print(e)
	

input("end")