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

    python3 setup_2exe.py py2exe

Ne semble fonctionner que depuis linux ...
Trouver une autre solution.

Utilisation cx-freeze
---------------------
Pareil il faut être sur Windows pour avoir un .exe
Voir :   
http://cx-freeze.readthedocs.org/en/latest/index.html  
Sur Windows

    python setup_freeze.py build  < Dossier avec exe et ressources
    python setup_freeze.py bdist_msi  < Fichier msi pour installer même chose que le résultat de "build"

Quand même faire attention aux dlls.
