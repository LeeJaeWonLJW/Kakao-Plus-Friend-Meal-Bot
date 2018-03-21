import datetime
import sqlite3

class Query(object):
    def insert(table, columns, values):
        return "INSERT INTO {}('{}') VALUES('{}');".format(table, columns, values)

    def findTable(name):
        return "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';".format(name)

    def create(table, columns):
        return "CREATE TABLE {}({});".format(table, columns)

    def update(table, column, value):
        return "UPDATE {} SET {}='{}';".format(table, column, value)

    def select(table, column):
        return "SELECT {} FROM {};".format(column, table)

def fileName(dayN=0):
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = "%02d" % (int(now.strftime("%m")))
    day = "%02d" % (int(now.strftime("%d"))+dayN)

    result = 'a'+year+month+day

    return result

def checkcheck():
    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    try:
        cur.execute(Query.select(fileName(),'*'))
        rows=cur.fetchall()
        if not rows:
            conn.commit()
    except sqlite3.Error as e:
        error=e
    finally:
        if conn:
            conn.close()

    #print("PRINT:"+str(rows[0]))
    
    if 'error' in locals():
        import parser
    else:
        pass

checkcheck()
