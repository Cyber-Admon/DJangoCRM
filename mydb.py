import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Olayiwola123#',
)

# prepare cursor object 

cursorObject = dataBase.cursor()

# create dataBase

cursorObject.execute("CREATE DATABASE elderco")

print('All Done!')