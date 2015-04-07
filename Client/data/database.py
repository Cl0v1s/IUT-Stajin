import pymssql

def init():
	conn = pymssql.connect(host='info-simplet',user='ETD',password='ETD',database='PT2_PPSV')
	cursor = conn.cursor()
	return [conn, cursor]

def save(cnx):
	cnx[0].commit()

def close(cnx):
	cnx[0].close()
