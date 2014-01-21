# coding: utf-8
'''
压缩保存
'''
try:
	originFolder = ''
	destPath = ''
	import os
	import zipfile
	import datetime

	if(not os.path.exists(destPath)):
		os.mkdir(destPath)

	todayStr = lambda :(datetime.datetime.utcnow() \
		+ datetime.timedelta(hours=+8)).strftime("%Y%m%d%H%M%S")
	destFile = zipfile.ZipFile(destPath + os.sep + todayStr() + '.zip','w', zipfile.ZIP_DEFLATED)
	
	for root, dirs, files in os.walk(originFolder):
		for fi in files:
			print(root + os.sep + fi)
			destFile.write(root + os.sep + fi , \
			root[len(originFolder):]+ os.sep + fi )

	destFile.close()
	pass
except Exception, e:
	print (e)
print ("end")
input ("exit")

