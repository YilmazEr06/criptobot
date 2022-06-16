from pyperclip import paste
import pyautogui


class data:                         
   def __init__(self, name): 
      self.name = name    
   def isim():
       try:
           pyautogui.click('coinnametext.PNG')
           currentMouseX, currentMouseY = pyautogui.position()
           pyautogui.click(currentMouseX+100, currentMouseY)   
           return paste()
       except:
           print("kopyalanamadı")
           
           
    
   def token():
       try:
           pyautogui.click('token.PNG')
           currentMouseX, currentMouseY = pyautogui.position()
           pyautogui.click(currentMouseX+100, currentMouseY)   
           return paste()
       except:
           print("kopyalanamadı")
       
   def platform():
       try:
           pyautogui.click('platform.PNG')
           currentMouseX, currentMouseY = pyautogui.position()
           pyautogui.click(currentMouseX+70, currentMouseY)   
           return paste()
       except:
           print("kopyalanamadı")
       
       
   def time():
       try:
           pyautogui.click('time.PNG')
           currentMouseX, currentMouseY = pyautogui.position()
           pyautogui.click(currentMouseX+100, currentMouseY)   
           return paste()
       except:
           print("kopyalanamadı")
      