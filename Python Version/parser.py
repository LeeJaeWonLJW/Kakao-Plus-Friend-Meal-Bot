#Lunch Dukwon High School Weekly Parser
from bs4 import BeautifulSoup
import requests
import datetime
import sqlite3

def check_breakfast(result):
    result = result.replace("'", "")
    result = result.replace("(", "")
    result = result.replace(")", "")
    result = result.replace(",", "")

    if result == fileName():
        return True
    else:
        return False

def fileName(day=0):
    now = datetime.datetime.now()
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))+day

    result = 'a'+str(year)+str(month)+str(day)

    return result

class Query(object):
    def insert(table, columns, values):
        return "INSERT INTO {}('{}') VALUES('{}');".format(table, columns, values)

    def findTable(name):
        return "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';".format(name)

    def create(table, columns):
        return "CREATE TABLE {}({})".format(table, columns)

    def update(table, column, value):
        return "UPDATE {} SET {}='{}'".format(table, column, value)

url = 'http://www.dukwon.hs.kr/user/carte/list.do?menuCd=#meals_date'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

mr = soup.find_all(class_="meals_table_day01")

now = datetime.datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = int(now.strftime("%d"))

for i in range(0, 7):
    tmp = mr[i].find("dd").get_text()

    if (tmp == ""):
        tmp = "아침 없음!"

    tmp = tmp.replace("ㆍ", "")

    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.create(fileName(i), 'breakfast text, lunch text, dinner text'))

    cur.execute(Query.insert(fileName(i), "','','"))

    cur.execute(Query.update(fileName(i), 'breakfast', tmp))

    conn.close()

for i in range(7, 14):
    tmp = mr[i].find("dd").get_text()

    if (tmp == ""):
        tmp = "점심 없음!"

    tmp = tmp.replace("ㆍ", "")

    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.update(fileName(i), 'dinner', tmp))

    conn.close()

for i in range(14, 21):
    tmp = mr[i].find("dd").get_text()

    if (tmp == ""):
        tmp = "저녁 없음!"

    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.update(fileName(i), 'dinner', tmp))

    conn.close()
