# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 10:47:57 2022

@author: KAYA
"""

import sqlite3 as sl




db = sl.connect("x.db ")
cs = db.cursor()
eski_veri=[]
 
class kalem:                         
   def __init__(self, name): 
      self.name = name 
   def sifirla():
       cs.execute("DELETE FROM karsilastirmaverisi")
       db.commit()
   def yazdir(isim,sembol,adres,tarih,saat):
       
       print(isim)
       print("Sembol: " + sembol)
       print("token adresi: "+adres)
       print(tarih)
       print(saat)
       print("--------")
       
   def veri_tabanina_koy(isim,sembol,adres,tarih,saat):
       cs.execute("insert into yenicoin values (?,?,?,?,?,?,?)",(sembol,isim,saat,tarih,"str(saatanlik)",'a["quote"]["USD"]["price"]',adres,))
       db.commit()
   def gecici(adres,isim):
       cs.execute("insert into karsilastirmaverisi values (?,?)",(adres,isim,))
       db.commit()
   def eskiveri():
       veri= cs.execute('''SELECT * FROM karsilastirmaverisi''')
       eski_veri.clear() 
        
       for a in veri.fetchall():
           b=a[0]
           eski_veri.append(b)
           
       return eski_veri