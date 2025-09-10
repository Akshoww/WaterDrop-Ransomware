#!/usr/bin/env python3 
import sys
import os


if len(sys.argv) > 1:
	f = open(sys.argv[1], "x")

	with open(sys.argv[1], "w") as f:
        	f.write("oue ")

	with open(sys.argv[1]) as f:
        	print("Après modifications : ", f.read())

	print("Suppression...")

	os.remove(sys.argv[1])
else :
	print("Veuillez ajouter un fichier en paramètre")
