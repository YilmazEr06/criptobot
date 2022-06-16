# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 00:59:35 2022

@author: Kaya Eryılmaz
"""


from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import datetime
from datetime import date, timedelta

import sqlite3 as sl
i=0

db = sl.connect("x.db ")
cs = db.cursor()



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
  'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'be23fc7f-0aee-4d28-a84e-c5e947be53c2',
}

session = Session()
session.headers.update(headers)

yesterday = str(date.today() - timedelta(days=1))
yesterday_datetime = datetime.datetime.strptime(yesterday, "%Y-%m-%d")

an = datetime.datetime.now()

saatanlik = an.time()

eski_veri=[]


date_time_str = '01:05:00.243860'
date_time_obj = datetime.datetime.strptime(date_time_str, '%H:%M:%S.%f')

baslangic=date_time_obj.time()

date_time_str = '01:05:15.243860'
date_time_obj = datetime.datetime.strptime(date_time_str, '%H:%M:%S.%f')

bitis =date_time_obj.time()



print(saatanlik<bitis)

#saatanlik<12 and saatanlik>6

while 1:
    #saatanlik<bitis and saatanlik>baslangic
    while 2>i:
        veri= cs.execute('''SELECT * FROM karsilastirmaverisi''')
        
        
        for a in veri.fetchall():
            b=a[0]
            eski_veri.append(b)
        
            cs.execute("delete FROM karsilastirmaverisi WHERE key=?",[b])
            db.commit()
        
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            for a in data["data"]:
        
                try:
        
                    tarih, saatd = a["date_added"].split("T")
                    saat = saatd.split(".")[0]
        
                    date_added = datetime.datetime.strptime(
                          a["date_added"][:10], "%Y-%m-%d")
        
                    if yesterday_datetime <= date_added:
                        
                          if a["platform"]["token_address"] in eski_veri:
                              print("eski veri")
                          
                          else:
                              
                              print(a["name"])
                              print("Sembol: " + a["symbol"])
                              print('USD ', a["quote"]["USD"]["price"])
                              print("token adresi: "+a["platform"]["token_address"])
                              print(tarih)
                              print(saat)
                              print("--------")
                              
                              
                              cs.execute("insert into yenicoin values (?,?,?,?,?,?,?)",(a["symbol"],a["name"],saat,tarih,str(saatanlik),a["quote"]["USD"]["price"],a["platform"]["token_address"],))
                              
        
                                              
                          cs.execute("insert into karsilastirmaverisi values (?,?)",(a["platform"]["token_address"],a["name"],))
                          db.commit()
                          
                          
                         
                    else:
                        continue
                  
                   
                except:
        
                    print("--------")
            i+=1
            an = datetime.datetime.now()
            saatanlik = an.time()
    
            print(i)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
    
    an = datetime.datetime.now()

    saatanlik = an.time()
db.close()
