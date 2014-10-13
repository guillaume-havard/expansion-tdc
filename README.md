expansion-tdc
=============

Logiciel de recopie de catégorie pour de tableaux croisés dynamiques

Fichier à traiter
-----------------

exemple : input-test.ods

Le fichier source doit être transformé en un fichier nomé "input.csv".  
le délimiteur doit être un ';'.

Utilisation py2exe
------------------

    python3 setup.py py2exe

Ne semble fonctionner que depuis linux ...
Trouver une autre solution.

Utilisation cx-freeze
---------------------

Voir : 
http://cx-freeze.readthedocs.org/en/latest/index.html

Quand même faire attention aux dlls.
