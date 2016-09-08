#!/usr/bin/python
#-*- coding=utf-8 -*-
#
#1-Lire le fichier cpays.txt et afficher son contenu.

#on fait une instantiation pour ouvrir le fichier
fic=open("cpays.txt")

#dictionnaire vide
dico_pays={}

#lecture ligne par ligne
for l in fic:
    #remplacement des tabulations. On fait un array avec les resultats dun split pour eliminer les pipes |
    [cle,valeur]=l.split("|")   
    #et on supprime  les tabulations
    cle=cle.replace("\t","")
    #on envoie les donnees dans le dictionnaire, on fait rstrip pour enlever le retour charriot
    dico_pays[cle]=valeur.rstrip()
#fermeture du fichier
fic.close()



#recuperation des cles du dico avec fonction key 
l1=dico_pays.keys()
#tri des cles
l1.sort()

#boucle pour affichage
for e in l1:
    print e,
    print "***",
    print dico_pays[e]
