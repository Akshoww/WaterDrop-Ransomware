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

	print("--------Results--------")
	#decrypt of all the files with "test" password (or yours)
	for file in file_list:
		cmd = "openssl enc -d -aes-256-cbc -iter 10000 -pass pass:'test' -in " + file + " -out file_temp && mv file_temp " + file
		subprocess.run(cmd, shell=True)
		print("  [+] File decrypted :", file) 

		#delete script file
		#os.remove(__file__)
else :
	print("Please select a directory to decrypt files")
