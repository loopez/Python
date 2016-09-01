#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ftplib import FTP
import os
print "\033[H\033[2J"
host     = "10.17.0.79"                  # adresse du serveur FTP
user     = "ftp"                            # votre identifiant
password = "ftp"                            # votre mot de passe
ftp      = FTP(host,user,password)          # on se connecte au serveur ftp
#
# Création d'une liste ( files ) des fichiers du répertoire /var/ftp/pub ( du serveur FTP ) ( liste au sens python )
#
ftp.cwd("pub")
files = ftp.nlst()   # attention files avec s ( car file est un mot reservé )
#
# Travail à faire
#
# a) A partir de la liste (files) creer un dictionnaire ( tableau associatif ) nomme dico_files
#
# Structure du dictionnaire 
#  
#   cle     : rang du fichier dans la liste ( sous forme string )   
#   valeur  : nom du fichier   
dic={}
#
# b) Affichez le contenu de ce dictionnaire comme suit ( utilisez un format )
#
#    1 Cours_Python.zip
#    2 Red_Hat_Enterprise_Linux-6-Deployment_Guide-en-US.pdf
#    3 hist01.txt
#    4 initiation_python.pdf
#

#srt parce quon transforme des chiffres(les indices) en chaine
for i in range(len(files)):
        dic[str(i+1)]=files[i]
        print "{0:4d} {1}".format(i+1,dic[str(i+1)])
