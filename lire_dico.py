#!/usr/bin/python
#-*- coding=utf-8 -*-
#
#imports
import pickle
# 1- Lire le fichier dico sauvegardé, open en mode Read

f = open('dico_pays.txt','r')
t=pickle.load(f)
f.close()
for cle in t.keys():
    print cle, " ",t[cle],
