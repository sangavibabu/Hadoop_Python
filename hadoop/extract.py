import os
import wget
import time
import shutil
import subprocess
filepath = 'sample.txt'
lines = [line.rstrip('\n') for line in open(filepath)]
for line in lines:
	url = "https://www.ncdc.noaa.gov/orders/qclcd/"+line
	wget.download(url, './')
	extractFolderName = line.replace('.tar.gz', '').replace('.zip', '')
	shutil.unpack_archive('./'+line, './extracted/'+extractFolderName)	
	#to write hdfs upload 
	subprocess.call(['hadoop fs -copyFromLocal /home/hduser/hadoop/extracted/'+extractFolderName+'/  hdfs:///data/'], shell=True)
	print('/home/hduser/hadoop/extracted/'+extractFolderName)
	#seconds
	time.sleep(60*30)
	os.remove('./'+line)
	shutil.rmtree('./extracted/'+extractFolderName)
