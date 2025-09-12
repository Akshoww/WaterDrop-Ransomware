#!/usr/bin/env python3

import requests
import os
import subprocess
import sys

print("------Files found------")
dir_path = sys.argv[1]
archive = "export.tar.gz"
cmd = "tar -zcvf " + archive + " " + dir_path
subprocess.run(cmd, shell=True)
print("------Export------")
cmd = "scp -o StrictHostKeyChecking=no " + archive + " ilyes@127.0.0.1:~/Desktop/receive"
subprocess.run(cmd, shell=True)
os.remove(archive)
