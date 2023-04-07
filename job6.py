import mysql.connector

mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Pc17svt15",
    database='laplateforme',
)

mon_curseur = mydb.cursor()
mon_curseur.execute('SELECT SUM(capacite) from salles')
capacte_salles= mon_curseur.fetchone()[0]
print("la capacité de toutes les salles est de ", capacte_salles)
