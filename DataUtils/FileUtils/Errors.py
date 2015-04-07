# -*- coding: utf-8 -*-
import os


def clear():
	try:
		os.remove("errors.log")
		return True
	except:
		return False

def render(name, errors):
	fil = open("errors.log", "a")
	fil.write("Vous pouvez trouver le descriptif des codes d'erreurs dans le manuel section 2.b Traitement des erreurs.")
	fil.write("")
	for error in errors:
		fil.write("Erreur P"+str(error['code'])+" dans le fichier "+str(name)+" à la ligne "+str(error['line'])+"\n")
	fil.close()
	return
