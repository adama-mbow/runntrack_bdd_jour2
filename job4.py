import mysql.connector

mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Pc17svt15",
    database='laplateforme',
)

mon_curseur = mydb.cursor()
mon_curseur.execute('select nom,capacite from salles')
print(list(mon_curseur))