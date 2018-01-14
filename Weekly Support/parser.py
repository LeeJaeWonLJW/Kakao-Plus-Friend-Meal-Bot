from bs4 import BeautifulSoup
import requests
import datetime

url='http://www.dukwon.hs.kr/user/carte/list.do?menuCd=#meals_date'
r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")

mr=soup.find_all(class_="meals_table_day01")

now = datetime.datetime.now()
year=now.strftime("%Y")
month=now.strftime("%m")
day=int(now.strftime("%d"))

for i in range(0,7):
    tmp=mr[i].find("dd").get_text()
    
    if(tmp==""):
        tmp="No Breakfast"

    tmp=tmp.replace("ㆍ","")
    if day+i<10:
        f = open("/home/dukwonlunch/www/data/josik" + year + month + '0' + str(day + i) + ".txt", 'w', encoding="utf-8")
    else:
        f=open("/home/dukwonlunch/www/data/josik"+year+month+str(day+i)+".txt",'w',encoding="utf-8")
    f.write(tmp)
    f.close()

for i in range(7,14):
    tmp=mr[i].find("dd").get_text()
    
    if(tmp==""):
        tmp="No Lunch"

    tmp=tmp.replace("ㆍ","")
    if day+i<10:
        f = open("/home/dukwonlunch/www/data/jungsik" + year + month + '0' + str(day + i - 7) + ".txt", 'w', encoding="utf-8")
    else:
        f=open("/home/dukwonlunch/www/data/jungsik"+year+month+str(day+i-7)+".txt",'w',encoding="utf-8")
    f.write(tmp)
    f.close()

for i in range(14,21):
    tmp=mr[i].find("dd").get_text()
    
    if(tmp==""):
        tmp="No Dinner"

    tmp=tmp.replace("ㆍ","")
    if day+i<10:
        f = open("/home/dukwonlunch/www/data/dinner" + year + month + '0' + str(day + i - 14) + ".txt", 'w', encoding="utf-8")
    else:
        f=open("/home/dukwonlunch/www/data/dinner"+year+month+str(day+i-14)+".txt",'w',encoding="utf-8")
    f.write(tmp)
    f.close()
