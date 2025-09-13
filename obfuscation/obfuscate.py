#!/usr/bin/env python3 

import os
import subprocess

cmd = "python3 -m compileall ../encrypt-waterdrop.py"
subprocess.run(cmd, shell=True)
cmd = "mv ../__pycache__/encrypt-waterdrop.cpython-311.pyc encrypt-waterdrop.py"
subprocess.run(cmd, shell=True)

cmd = "python3 -m compileall ../backup.py"
subprocess.run(cmd, shell=True)
cmd = "mv ../__pycache__/backup.cpython-311.pyc backup.py"
subprocess.run(cmd, shell=True)

cmd = "rm -r ../__pycache__"
subprocess.run(cmd, shell=True)

