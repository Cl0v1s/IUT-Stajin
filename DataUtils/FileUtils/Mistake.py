# -*- coding: utf-8 -*-
from FileUtils import Importer
import time

def mistakes(enseignants, entreprises, etudiants, stages):
	stu =  mistakes_students(etudiants)
	tea = mistakes_teacher(enseignants)
	ent = mistakes_enterprises(entreprises)
	sta = mistake_stages(enseignants, entreprises, etudiants, stages)
	return {"students": stu, "teachers": tea, "enterprises": ent, "stages": sta }

#Teste si une adresse mail est valide ou non
def check_mail(mail):
	if ("@" in mail) == False or ("." in mail.split("@")[1]) == False:
		return False
	return True

def mistake_stages(enseignants, entreprises, etudiants,stages):
	entr_info = Importer.getData(entreprises)

	etd_info = Importer.getData(etudiants)

	ens_info = Importer.getData(enseignants)

	reader = Importer.getData(stages)

	counter = 1
	errors = [] #{line, type, text}
	row_old = []


	for row in reader:
		error = 0

		#CSV Mal formé
		if len(row) != 11:
			error = 8

		#Absence de données
		i = 0
		occ = 0
		while i<len(row):
			if row[i] == None or row[i] == "":
				if i != 6 and i != 8 and i != 9:
					occ+=1
			i = i + 1

		#usage d'un compteur afin de ne pas prendre en considération les lignes vides
		if occ >=len(row)-3:
			counter +=1
			continue
		elif occ != 0:
			error = 4



		#Présence de l'étudiant dans étudiant
		if error == 0:
			i = 0
			error = 6
			while error == 6 and i<len(etd_info):
				if etd_info[i][0] == row[4]  and etd_info[i][1] == row[5]:
					error = 0
				i = i + 1

		#Présence de l'entreprise dans le fichier entreprise
		if error ==  0:
			i = 0
			error = 5
			while error == 5 and i<len(entr_info):
				if entr_info[i][0] == row[0]:
					error = 0
				i = i + 1

		#Présence de l'enseignant dans le fichier enseignant
		if error == 0:
			i = 0
			error = 7
			while error == 7 and i<len(ens_info):
				if ens_info[i][2] == row[10]:
					error = 0
				i = i + 1


		if error !=0 and counter != 0:
			errors.append({'line':counter,'code': error,'text': row})
		counter += 1
		row_old.append(row)
	return errors

#Recherch d'erreurs et d'incohérences dans les fichiers étudiants
def mistakes_students(students):
	reader = Importer.getData(students)
	counter = 1
	errors = [] #{line, type, text}
	row_old = []
	for row in reader:
		error = 0

		#CSV mal formé
		if len(row) != 3:
			error = 8

		#Ne dispose pas des informatins nécessaires
		if error == 0 and (row[0] == None or row[0] == "" or row[1] == None or row[1] == "" or check_mail(row[2]) == False):
			error = 3

		#Doublon
		i = 0
		while error == 0 and i <len(row_old):
			if row[0] == row_old[i][0] and row[1] == row_old[i][1]:
				error = 11
			i = i + 1


		if error !=0 and counter != 0:
			errors.append({'line':counter,'code': error,'text': row})
		counter += 1
		row_old.append(row)
	return errors

#Recherche erreurs et incohérenaces dans le fichier enseignant
def mistakes_teacher(enseignants):
	reader = Importer.getData(enseignants)
	counter = 1
	errors = [] #{line, type, text}
	row_old = []
	for row in reader: #Parcours de toutes les entrées présentent dans le fichier enseignant
		error = 0

		#CSV Mal formé
		if len(row) != 3:
			error = 8

		#Ne dispose pas des informatins nécessaires
		if error == 0 and (row[0] == None or row[0] == "" or row[1] == None or row[1] == "" or row[2] == None or row[2] == ""):
			error = 3

		#Doublon de surnom
		i = 0
		while error == 0 and i<len(row_old):
			if row[2] == row_old[i][2]:
				error = 9
			i = i + 1


		if error != 0 and counter != 0:
			errors.append({'line':counter,'code': error,'text': row})
		counter += 1
		row_old.append(row)
	return errors

#Recherches erreurs entreprises
def mistakes_enterprises(enterprises):
	reader = Importer.getData(enterprises)
	counter = 1
	errors = []
	row_old = []
	for row in reader: #Parcours de toutes les entrées dans le fichier entreprises
		error = 0

		#CSV Mal formé
		if len(row) != 8:
			error = 8

		#Vérification de la précense des données obligatoires
		if error == 0 and (row[0] == None or row[0] == "" or row[5] == None or row[5] == "" or row[6] == None or row[6] == "" or row[7] == None or row[7] == ""):
			error = 2

		#Doublon de nom
		i = 0
		while error == 0 and i<len(row_old):
			if row[0] == row_old[i][0]:
				error = 10
			i = i + 1


		if error != 0 and counter !=0:
			errors.append({'line':counter,'code': error,'text': row})
		counter += 1
		row_old.append(row)
	return errors
