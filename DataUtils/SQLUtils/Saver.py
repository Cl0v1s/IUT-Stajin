# -*- coding: utf-8 -*-

from FileUtils import Importer


def generateScript(teachers, students, enterprises, stages):
	result = """
-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u1
-- http://www.phpmyadmin.net
--
-- Client: info-arie.iut.bx1
-- Généré le: Mer 25 Mars 2015 à 15:39
-- Version du serveur: 5.5.41
-- Version de PHP: 5.4.39-0+deb7u1


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: stajin
--

-- --------------------------------------------------------

--
-- Structure de la table Enseignant
--

CREATE TABLE Enseignant (
  surnom_enseignant varchar(5) NOT NULL,
  nom_enseignant varchar(30) NOT NULL,
  prenom_enseignant varchar(30) NOT NULL,
  PRIMARY KEY (surnom_enseignant)
);

--
-- Structure de la table Entreprise
--

CREATE TABLE  Entreprise (
  numero_entreprise int NOT NULL IDENTITY(1,1),
  nom_entreprise varchar(30) NOT NULL,
  adresse_entreprise varchar(100) NOT NULL,
  secteur_entreprise varchar(30) NOT NULL,
  nom_ville varchar(30) NOT NULL,
  code_postal_ville int NOT NULL,
  PRIMARY KEY (numero_entreprise)
);

--
-- Structure de la table Etudiant
--

CREATE TABLE  Etudiant (
  numero_etudiant int NOT NULL IDENTITY(1,1),
  nom_etudiant varchar(30) NOT NULL,
  prenom_etudiant varchar(30) NOT NULL,
  mail_etudiant varchar(100) NOT NULL,
  PRIMARY KEY (numero_etudiant)
);

--
-- Structure de la table Stage
--

CREATE TABLE  Stage (
  numero_stage int NOT NULL IDENTITY(1,1),
  nom_entreprise varchar(10) NOT NULL,
  titre_stage varchar(1000) DEFAULT NULL,
  anne_universitaire_stage varchar(30) NOT NULL,
  date_debut_stage varchar(30) DEFAULT NULL,
  date_fin_stage varchar(30) DEFAULT NULL,
  nom_responsable_stage varchar(30) NOT NULL,
  prenom_responsable_stage varchar(30) NOT NULL,
  mail_responsable_stage varchar(100) NOT NULL,
  nom_etudiant varchar(30) NOT NULL,
  prenom_etudiant varchar(30) NOT NULL,
  surnom_enseignant varchar(5) NOT NULL,
  PRIMARY KEY (numero_stage)
);

--
-- Structure de la table Ville
--

CREATE TABLE  Ville (
  numero_ville int NOT NULL IDENTITY(1,1),
  nom_ville varchar(30) NOT NULL,
  code_postal_ville int NOT NULL,
  PRIMARY KEY (numero_ville)
);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
"""

	result = result + generateTeachers(teachers)
	result = result + generateEnterprises(enterprises)
	result = result + generateStudents(students)
	result = result + generateStages(stages)
	result = result + generateCities(enterprises)

	save = open("data.sql", "w", encoding="latin-1")
	save.write(result)
	save.close()


def generateCities(enterprises):
	res = ""
	first = True
	for e in enterprises:
		if first == False:
			l = Importer.purify(e)
			res = res + "INSERT INTO Ville (nom_ville, code_postal_ville) VALUES ('"+l[3]+"', '"+l[2]+"');\n"
		first = False
	return res


def generateTeachers(teachers):
	res = ""
	first = True
	for t in teachers:
		if first == False:
			l = Importer.purify(t)
			res = res + "INSERT INTO Enseignant (surnom_enseignant, nom_enseignant, prenom_enseignant) VALUES ('"+l[2]+"', '"+l[0]+"', '"+l[1]+"');\n"
		first = False
	return res

def generateEnterprises(enterprises):
	res = ""
	first = True
	for e in enterprises:
		if first == False:
			l = Importer.purify(e)
			res = res + "INSERT INTO Entreprise (nom_entreprise, adresse_entreprise, secteur_entreprise, nom_ville, code_postal_ville) VALUES ('"+l[0]+"', '"+l[1]+"', '"+l[4]+"', '"+l[3]+"', '"+l[2]+"');\n"
		first = False
	return res


def generateStudents(students):
	res = ""
	first = True
	for s in students:
		if first == False:
			l = Importer.purify(s)
			res =res + "INSERT INTO Etudiant (nom_etudiant, prenom_etudiant, mail_etudiant) VALUES ('"+l[0]+"', '"+l[1]+"', '"+l[2]+"');\n"
		first = False
	return res

def generateStages(stages):
	res = ""
	first = True
	for s in stages:
		if first == False:
			l = Importer.purify(s)
			if l[0] == None or l[0] == '':
				continue
			res = res + "INSERT INTO Stage (nom_entreprise,titre_stage, anne_universitaire_stage, date_debut_stage, date_fin_stage, nom_responsable_stage, prenom_responsable_stage, mail_responsable_stage, nom_etudiant, prenom_etudiant, surnom_enseignant) VALUES ('"+l[0]+"', '"+l[6]+"', '"+l[7]+"', '"+l[8]+"', '"+l[9]+"', '"+l[1]+"', '"+l[2]+"', '"+l[3]+"', '"+l[4]+"','"+l[5]+"', '"+l[10]+"');\n"
		first = False
	return res
