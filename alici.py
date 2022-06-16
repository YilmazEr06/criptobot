import pyautogui
import time
from pyperclip import paste
 
class xx:                         
   def __init__(self, name): 
      self.name = name    
                          
     
   def yazdir(a):
       print(a)
       
   def token(a):
       try:
           try:
               pyautogui.click('kimlik.PNG')
               pyautogui.write(a)
               time.sleep(1)
               pyautogui.press('enter')
           except:
               pyautogui.click('kimlik2.PNG')
               pyautogui.write(a)
               time.sleep(1)
               pyautogui.hotkey('enter')
       except:
            print('coin sayfasına girilemedi.')
            
   def ayarla(miktar):
       try:
            time.sleep(0.5)
            pyautogui.click('trade.PNG')
            time.sleep(1)
            pyautogui.click('BNB.PNG')
            currentMouseX, currentMouseY = pyautogui.position()
            time.sleep(0.5)
            pyautogui.click('BUSD.PNG')
            time.sleep(0.5)
            pyautogui.click(currentMouseX-150, currentMouseY)
            pyautogui.press('backspace')
            pyautogui.write(miktar)
       except:
           print('Miktar ayralanamadı')
           xx.anasayfayadon()
          
   def anasayfayadon():
       try:
            pyautogui.scroll(400)
            time.sleep(0.5)
            pyautogui.click('anasayfa.PNG')
       except:
            print('Anasayfaya dönülemedi')
          
            
               
   def link():
       try:
            
            pyautogui.click('link.PNG')
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.click(currentMouseX, currentMouseY+20)
            time.sleep(10)
            
       except:
           print('Bağlantıya Girilemedi')
               
   def onayla():
       try:
           
            pyautogui.scroll(-200)
            time.sleep(0.5)
            pyautogui.click('swap.PNG')
            pyautogui.moveRel(300,-200,duration=2)
            pyautogui.scroll(-200)
            time.sleep(1)
            pyautogui.click('reddet.PNG')
            time.sleep(10)
       except:
            print('İşlem onaylanmadı')
           
   def hacim():
       try:
           
            time.sleep(3)
            pyautogui.click('hacim.PNG')
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveRel(50,20,duration=0)
            pyautogui.dragRel(-110,0,duration=1)
            pyautogui.hotkey('ctrl', 'c')
            return paste()
       except:
           print('Hacim Verisi Alınamadı')
           xx.anasayfayadon()
           
        
        
        
     
        

            
