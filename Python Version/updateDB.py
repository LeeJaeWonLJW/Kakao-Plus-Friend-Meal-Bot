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

def checkcheck():
    if datetime.datetime.today().weekday() == 0:
        conn = sqlite3.connect("db/menu.db")
        cur = conn.cursor()

        cur.execute(Query.select('Qcheck', 'bool'))

        rows = cur.fetchall()

        result = str(rows[0])

        if result == 0:
            import parser

            cur.execute(Query.update('Qcheck', 'bool', 1))
        else:
            pass

        conn.close()
            
    elif datetime.datetime.today().weekday() == 1:
        conn = sqlite3.connect("db/menu.db")
        cur = conn.cursor()

        cur.execute(Query.update('Qcheck', 'bool', 0))

        conn.close()
    
