from veritabani import kalem
import time
from Telagram import data
from alici import xx
i=0
time.sleep(3)

while i<1:    
    eski= kalem.eskiveri()
    yeni= data.token()
    isim= data.isim()
    sembol = data.platform()

    #yeni== str(eski[0])
    if 1:
        print("yeni veri tespit edildi")
        kalem.gecici(yeni,isim)
        xx.token(yeni)
        hacim=xx.hacim()
        if len(hacim)<=7:
            xx.ayarla("12")
            xx.onayla()
            xx.anasayfayadon()
            kalem.veri_tabanina_koy(isim,sembol,yeni,str(time),"s")
            
        else:
            xx.anasayfayadon()
    i+=1


