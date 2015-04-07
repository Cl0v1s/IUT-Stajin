# -*- coding: utf-8 -*-


import sys
from FileUtils import Importer
from FileUtils import Mistake
from FileUtils import Errors
from SQLUtils import Saver


debug = False

for arg in sys.argv:
	if "-h" in arg or "--help" in arg:
		print ("--Aide--")
		print ("-h, --help Afficher cet aide.")
		print ("-f, --force Forcer la génération de script sql.")
		sys.exit(0)
	if "--force" in arg or "-f" in arg:
		debug = True

Errors.clear()
print ("Analyse des fichiers de donnees...")
errors = Mistake.mistakes("./../fichier_enseignants.csv", "./../fichier_entreprises.csv", "./../fichier_etudiants.csv", "./../fichier_stages.csv")
keys = list(errors.keys())
found = False
i = 0
while i < len(keys):
	if len(errors[keys[i]]) != 0:
		Errors.render(keys[i],errors[keys[i]])
		found=True
	i+=1

if found == True and (debug == None or debug == False):
	print ("Des erreurs ont ete trouvees dans les fichiers de donnees.")
	print ("Veuillez consulter le fichier errors.log et corriger les dites erreurs.")
else:
	Saver.generateScript(Importer.getData("./../fichier_enseignants.csv"), Importer.getData("./../fichier_etudiants.csv"), Importer.getData("./../fichier_entreprises.csv"), Importer.getData("./../fichier_stages.csv"))
	print ("Aucune erreur n'a ete identifiee.")
	print ("Un fichier data.sql a ete genere afin de vous permettre de creer la base de donnees demandee.")


