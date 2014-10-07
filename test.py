#! /usr/bin/python3

import csv, sys
filename = "input.csv"

def truc(liste, ind, mot):
    
    print("liste :", liste[ind], "mot :", mot[0])
    
    if "Total " in liste[ind]:
        mot[0] = ""
    else:
        if len(liste[ind]) == 0:
            if len(mot[0]) == 0:
                #raise Exception("liste vide et mot vide")
                pass
            else:
                liste[ind] = mot[0]
        else:
            mot[0] = liste[ind]

liste = []

with open(filename, newline='') as f:
    reader = csv.reader(f, delimiter=';')

    listel = []
    
    for l in reader:
        print(type(l))
        print(l)
        listel.append(l)
        
# commence apres la premiere ligne ou il y a qqchose
# pour toute les lignes
    # prend mot colonne
    # si "Total " dans colone mot à coppier vide
    # si mot pas vide le copier
    # si pas total et re tenue vide récupe mot
# enregistrer


    for l in range(len(listel)):
        if len(listel[l][0]) != 0:
            print("debut :", l)
            liste = listel[l:]
            break


mot_b = [""]
mot_d = [""]
mot_c = [""]
mot_e = [""]

"""
print("-----------------")         
for l in liste:
    print(l)
print("-----------------")
print("algo")
print("len liste", len(liste))
print()
"""
for l in liste:
    print(l)
    truc(l, 1, mot_b) 
    truc(l, 2, mot_c) 
    truc(l, 3, mot_d)
    truc(l, 4, mot_e)
"""    
print("-----------------")     
for l in liste:
    print(l)
print("-----------------") 
    
    
print(";".join(liste[0]))
"""
    
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    print(csv.list_dialects())
    for l in liste:
        print(l)        
        writer.writerow(l)
    
sys.exit()
    
    
print()
print(liste[5])
for t in liste[5]:
    print(type(t))
    print(t)   
    if "Total " in t:
        print("tagada")
            
            
            
