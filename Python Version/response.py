import sqlite3
import datetime

class Query(object):
    def insert(table, columns, values):
        return "INSERT INTO {}('{}') VALUES('{}');".format(table, columns, values)

    def findTable(name):
        return "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';".format(name)

    def create(table, columns):
        return "CREATE TABLE {}({})".format(table, columns)

    def update(table, column, value):
        return "UPDATE {} SET {}='{}'".format(table, column, value)

    def select(table, column):
        return "SELECT {} FROM {}".format(column, table)

def fileName(day=0):
    now = datetime.datetime.now()
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))+day

    result = 'a'+str(year)+str(month)+str(day)

    return result

def breakfast():
    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.select(fileName(i), 'breakfast'))

    rows = cur.fetchall()

    result = str(rows[0])

    conn.close()

    return result

def lunch():
    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.select(fileName(i), 'lunch'))

    rows = cur.fetchall()

    result = str(rows[0])

    conn.close()

    return result

def dinner():
    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.select(fileName(i), 'dinner'))

    rows = cur.fetchall()

    result = str(rows[0])

    conn.close()

    return result
