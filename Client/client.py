from bottle import *
from data import queries


@route("/")
@route("/index")
def index_page():
	_stageNumber = queries.getSagesNumber()
	_teacherNumber= queries.getTeachersNumber()
	_enterprisesNumber= queries.getEnterprisesNumber()
	_studentNumber = queries.getStudentsNumber()
	_stageByYear = queries.stageEvolution()
	_stageByTeacher = queries.stageEvolutionByTeacher()
	_stageByEnterprise = queries.stageEvolutionByEnterprise()

	return template("index", {'stageNumber': _stageNumber, 'teacherNumber':_teacherNumber, 'studentNumber':_studentNumber, 'enterprisesNumber':_enterprisesNumber, 'stageByYear': _stageByYear, 'stageByTeacher': _stageByTeacher, 'stageByEnterprise':_stageByEnterprise})

def error404(page):
    return "Cette page n'existe pas" #definir une page et un style pour la page d'erreur 404


#Sert les fichiers statics
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

run(host="localhost", port=80, debug=True, reloader=True);
