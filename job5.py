import mysql.connector

mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Pc17svt15",
    database='laplateforme',
)

mon_curseur = mydb.cursor()
mon_curseur.execute('SELECT SUM(superficie) from etage')
surface = mon_curseur.fetchone()[0]
print("la superficie de la plateforme est ", surface,"m2")