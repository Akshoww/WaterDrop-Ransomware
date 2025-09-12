#!/usr/bin/env python3 
import sys
import os
import subprocess


if len(sys.argv) > 1:
	
	print("Fichier avant chiffrement : ", open(sys.argv[1]).read()) 

	#chiffrement du fichier avec le mdp : tqt
	cmd = "openssl enc -e -aes-256-cbc -iter 10000 -pass pass:'tqt' -in " + sys.argv[1] + " -out " + sys.argv[1]
	subprocess.run(cmd, shell=True)

	print("-------------------------------------")

	print("Fichier après chiffrement : ") 
	print(subprocess.call(["cat",sys.argv[1]]))

	#supprimer le script actuel
	#os.remove(__file__)
else :
	print("Veuillez ajouter un fichier en paramètre")
