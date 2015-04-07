import time
from data import database

def getSagesNumber():
	d = time.strftime("%Y")
	lastyear = int(d)-1
	firstyear = int(d)-2
	d = str(firstyear)+"-"+str(lastyear)
	cnx = database.init()
	cnx[1].execute("SELECT COUNT(Stage.numero_stage) FROM Stage WHERE Stage.anne_universitaire_stage = '"+d+"'")
	res= cnx[1].fetchall()
	database.close(cnx)
	return res[0][0]

def getEnterprisesNumber():
	cnx = database.init()
	cnx[1].execute("SELECT COUNT(Entreprise.numero_entreprise) FROM Entreprise")
	res = cnx[1].fetchall()
	database.close(cnx)
	return res[0][0]

def getTeachersNumber():
	cnx = database.init()
	cnx[1].execute("SELECT COUNT(Enseignant.surnom_enseignant) FROM Enseignant")
	res = cnx[1].fetchall()
	database.close(cnx)
	return res[0][0]

def getStudentsNumber():
	cnx = database.init()
	cnx[1].execute("SELECT COUNT(Etudiant.numero_etudiant) FROM Etudiant")
	res = cnx[1].fetchall()
	database.close(cnx)
	return res[0][0]

def stageEvolution():
	cnx = database.init()
	cnx[1].execute("SELECT anne_universitaire_stage, COUNT(numero_stage) FROM Stage GROUP BY anne_universitaire_stage")
	res = cnx[1].fetchall()
	l  = sorted(list(res))
	database.close(cnx)
	return l

def stageEvolutionByTeacher():
	cnx = database.init()
	cnx[1].execute("SELECT Stage.anne_universitaire_stage, Stage.surnom_enseignant, COUNT(numero_stage) FROM Stage GROUP BY Stage.surnom_enseignant, Stage.anne_universitaire_stage")
	res = cnx[1].fetchall()
	cnx[1].execute("SELECT anne_universitaire_stage FROM Stage")
	ye = cnx[1].fetchall()
	l = {"years" : []}
	for y in ye:
		if y[0] not in l["years"]:
			l["years"].append(y[0])
	l["years"] = sorted(l["years"])
	for re in res:
		if re[1] not in l:
			l[re[1]] = []
			for y in l["years"]:
				l[re[1]].append([y, 0])
		for r in l[re[1]]:
			if r[0] == re[0]:
				r[1]+=int(re[2])

	for li in l:
		li = sorted(li)

	database.close(cnx)
	return l

def stageEvolutionByEnterprise():
	cnx = database.init()
	cnx[1].execute("SELECT Stage.anne_universitaire_stage, Stage.nom_entreprise, COUNT(numero_stage) FROM Stage GROUP BY Stage.nom_entreprise, Stage.anne_universitaire_stage")
	res = cnx[1].fetchall()
	cnx[1].execute("SELECT anne_universitaire_stage FROM Stage")
	ye = cnx[1].fetchall()
	l = {"years" : []}
	for y in ye:
		if y[0] not in l["years"]:
			l["years"].append(y[0])
	l["years"] = sorted(l["years"])
	for re in res:
		if re[1] not in l:
			l[re[1]] = []
			for y in l["years"]:
				l[re[1]].append([y, 0])
		for r in l[re[1]]:
			if r[0] == re[0]:
				r[1]+=int(re[2])

	for li in l:
		li = sorted(li)

	database.close(cnx)
	return l



