import mysql.connector

mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Pc17svt15",
    database='laplateforme',

)

mycursor = mydb.cursor()
mycursor.execute('select * from etudiant')
print(list(mycursor))