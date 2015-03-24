import os

_dirpath = os.getcwd()

for _filename in os.listdir(_dirpath):
	os.rename(_dirpath+os.sep+_filename,_dirpath+os.sep+_filename.replace('asdf','jkl'))		
	pass
