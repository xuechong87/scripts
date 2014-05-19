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
				if(_match("^\w*\.log$") or _match("^\w*\.log\.([^\.]*)$")):
					print(_fullName)
			pass

		if(_dirnames):
			for _dirName in _dirnames:
				cleanDir(os.path.join(_dirpath,_dirName))
				pass

			pass

if __name__ == '__main__':
	try:
		cleanDir("D:/")
	except Exception, e:
		print(e)
	

input("end")