import sqlite3
import datetime
import re

## korean only global regex ##
hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')

class Query(object):
    def insert(table, columns, values):
        return "INSERT INTO {}({}) VALUES({});".format(table, columns, values)

    def findTable(name):
        return "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';".format(name)

    def create(table, columns):
        return "CREATE TABLE {}({})".format(table, columns)

    def update(table, column, value):
        return "UPDATE {} SET {}='{}'".format(table, column, value)

    def select(table, column):
        return "SELECT {} FROM {}".format(column, table)

def fileName(dayN=0):
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = "%02d" % (int(now.strftime("%d"))+dayN)

    result = 'a'+year+month+day

    return result

def checkHour(Type):
    import time
    now = time.localtime()
    
    if Type == 'breakfast':
        if now.tm_hour >= 8:
            return 1
        else:
            return 0
    elif Type == 'lunch':
        if now.tm_hour >= 13:
            return 1
        else:
            return 0
    elif Type == 'dinner':
        if now.tm_hour >= 19:
            return 1
        else:
            return 0

def breakfast():
    global hangul
    
    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    timeValue = checkHour('breakfast')
    cur.execute(Query.select(fileName(timeValue), 'breakfast'))

    rows = cur.fetchall()

    result = str(rows[0])

    conn.close()
    
    return hangul.sub('',result)

def lunch():
    global hangul
    
    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    timeValue = checkHour('lunch')
    cur.execute(Query.select(fileName(timeValue), 'lunch'))

    rows = cur.fetchall()

    result = str(rows[0])

    conn.close()

    return hangul.sub('',result)

def dinner():
    global hangul
    
    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    timeValue = checkHour('dinner')
    cur.execute(Query.select(fileName(timeValue), 'dinner'))

    rows = cur.fetchall()

    result = str(rows[0])

    conn.close()

    #return result
    return hangul.sub(' ',result)
