#Use Only Once when you create sqlite3 database
import sqlite3

print('Dasebase Name : ')
dbName = str(input('>> '))

conn = sqlite3.connect(dbName+'.db')
print("Created and Opened database successfully")

print('Table Name : ')
tableName = str(input('>> '))

print('Column Query : ex) NAME TYPE, NAME TYPE, ...')
columnQuery = str(input('>> '))

conn.execute('CREATE TABLE '+tableName+' ('+columnQuery+')')
print('Table created successfully')
conn.close()
