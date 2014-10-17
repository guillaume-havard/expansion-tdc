#! /usr/bin/python3

import csv, sys
import xlrd
import xlsxwriter

filename_in = "input.xlsx"
filename_out = "output.xlsx"

def truc(liste, ind, mot):    
    #print("liste :", liste[ind], "mot :", mot[0])
    
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

# commence apres la premiere ligne ou il y a qqchose
# pour toute les lignes
    # prend mot colonne
    # si "Total " dans colone mot à coppier vide
    # si mot pas vide le copier
    # si pas total et re tenue vide récupe mot
# enregistrer

wb_in = xlrd.open_workbook(filename_in)
wb_out = xlsxwriter.Workbook(filename_out)
sheet_names = wb_in.sheet_names()
print("liste des feuilles :", sheet_names)

for sheet_name in sheet_names:
    liste = []
    # extract information from the excel file
    ws_in = wb_in.sheet_by_name(sheet_name)

    listel = []
    for cur_row in range(ws_in.nrows):
        listel.append([])
        for cur_col in range(ws_in.ncols):
            listel[cur_row].append(ws_in.cell_value(cur_row, cur_col))

    # Take out the rows without anything in the first column.
    for l in range(len(listel)):
        if len(listel[l][0]) != 0:
            liste = listel[l:]
            break
               
    mot_b = [""]
    mot_d = [""]
    mot_c = [""]
    mot_e = [""]

    for l in liste:
        #print(l)
        truc(l, 1, mot_b) 
        truc(l, 2, mot_c) 
        truc(l, 3, mot_d)
        truc(l, 4, mot_e)



    ws_out = wb_out.add_worksheet(sheet_name)
    for row, l in enumerate(liste):  
        ws_out.write_row(row, 0, l)  
    
wb_out.close()
    
sys.exit()
        
            
            
