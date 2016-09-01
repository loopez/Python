#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ftplib import FTP 


print "\033[H\033[2J"
host     = "10.17.0.79"                      # adresse du serveur FTP
user     = "ftp"                            # votre identifiant
password = "ftp"                            # votre mot de passe
ftp      = FTP(host,user,password)          # on se connecte au serveur ftp
#
# Création d'une liste ( files ) des fichiers du répertoire /var/ftp/pub ( du serveur FTP ) ( liste au sens python )
#
ftp.cwd("pub")
files = ftp.nlst()   # attention files avec s ( car file est un mot reservé )
dic={}

#
# Travail à faire
#
# a) Affichez le contenu de ce dictionnaire comme suit 
#
#    1 Cours_Python.zip
#    2 Red_Hat_Enterprise_Linux-6-Deployment_Guide-en-US.pdf
#    3 hist01.txt
#    4 initiation_python.pdf
#
for i in range(len(files)):
        dic[str(i+1)]=files[i]
print "{0:4d} {1}".format(i+1,dic[str(i+1)])


# b) Choisir le rang (cle) du fichier à télécharger
#    Faire les controles nécéssaires ( existence de cle )
#
#has_key permnet de verifier l existance dune cle

print "\n"


while 1:
        choix=raw_input("Choisir l'index du fichier a telecharger ou  0 (zero) pour quitter: ")
        if choix == "0":
                break
        if dic.has_key(choix):
                ftp.retrbinary("RETR "+dic[choix],open(dic[choix], 'wb').write)
                print "Fichier "+dic[choix]+" telecharge!"
                # c) Télecharger le fichier en question ; utilisation de la methode ftp.retrbinary()
#    
# d) Faire une bouche (while) sur le choix tant que c'est different de 0 (zero)    
#
# Exemple
#
# Index Fichier
#    1 Cours_Python.zip
#    2 Red_Hat_Enterprise_Linux-6-Deployment_Guide-en-US.pdf
#    3 hist01.txt
#    4 initiation_python.pdf



#Donnez l'index du fichier à télécharger ou 0 pour quitter : 1
# Cours_Python.zip  : télécharger correctement  
#Donnez l'index du fichier à télécharger ou 0 pour quitter : 0


#       Fin Ftp

