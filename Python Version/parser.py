#Lunch Dukwon High School Weekly Parser
from bs4 import BeautifulSoup
import requests
import sqlite3
import re

## SQLite3 Query func ##
class Query(object):
    def insert(table, columns, values):
        return "INSERT INTO {}({}) VALUES({});".format(table, columns, values)

    def findTable(name):
        return "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';".format(name)

    def create(table, columns):
        return "CREATE TABLE {}({});".format(table, columns)

    def update(table, column, value):
        return "UPDATE {} SET {}='{}';".format(table, column, value)
    
## korean only regex ##
hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')

## Parser Set ##
url = 'http://www.dukwon.hs.kr/user/carte/list.do?menuCd=#meals_date'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

## meal list ##
mr = soup.find_all(class_="meals_table_day01")

## date ##
mrt = soup.find_all(class_="meals_table_date")

## weekday ##
mrh = soup.find_all("th")

date = list()
header = list()
for i in range(7):
    ## date ##
    text = ''.join(mrt[i].get_text().split('-'))
    regex = re.compile(r'\d+')
    matchobj = regex.search(text)
    date.append('a'+matchobj.group())

    ## weekday ##
    subText = hangul.sub('',str(mrh[i])).replace(' ','')
    header.append(subText+'  ')

## breakfast ##
for i in range(0, 7):
    tmp = mr[i].find("dd").get_text()

    if (tmp == ""):
        tmp = "아침 없음!"

    tmp=hangul.sub('',tmp)
    
    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.create(date[i], 'breakfast text, lunch text, dinner text'))
    conn.commit()
    cur.execute(Query.insert(date[i],"'breakfast','lunch','dinner'", "'a','b','c'"))
    conn.commit()
    cur.execute(Query.update(date[i], 'breakfast', header[i] + tmp))
    conn.commit()

    conn.close()

## lunch ##
for i in range(7, 14):
    tmp = mr[i].find("dd").get_text()

    if (tmp == ""):
        tmp = "점심 없음!"

    tmp=hangul.sub('',tmp)

    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.update(date[i-7], 'lunch', header[i-7] + tmp))
    conn.commit()

    conn.close()

## dinner ##
for i in range(14, 21):
    tmp = mr[i].find("dd").get_text()

    if (tmp == ""):
        tmp = "저녁 없음!"

    tmp=hangul.sub('',tmp[1:].replace('ㆍ',' '))

    conn = sqlite3.connect("db/menu.db")
    cur = conn.cursor()

    cur.execute(Query.update(date[i-14], 'dinner', header[i-14] + tmp))
    conn.commit()

    conn.close()
