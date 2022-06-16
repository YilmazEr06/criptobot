
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import datetime
from datetime import date,timedelta


eski_veri=[] 

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'df566d9e-ee41-4c86-806e-11b4599396f1',
}

session = Session()
session.headers.update(headers)

yesterday= str(date.today() - timedelta(days=1))
yesterday_datetime= datetime.datetime.strptime(yesterday, "%Y-%m-%d")

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  for a in data["data"]:
      
      try:
          
          tarih,saatd=a["date_added"].split("T")
          saat=saatd.split(".")[0]
          
          if 1:
              date_added= datetime.datetime.strptime(a["date_added"][:10], "%Y-%m-%d")
              
              if yesterday_datetime<date_added:
                  
                  
                  print(a["name"])
                  print("Sembol: "+ a["symbol"])
                  print('USD ',a["quote"]["USD"]["price"])
                  print("token adresi: "+a["platform"]["token_address"])
                  print(tarih)
                  print(saat)
                  print("--------")
                  eski_veri.append(a["platform"]["token_address"])
                  print()
              else :
                  pass
              
          else:
              if a["platform"]["token_address"] in eski_veri:
                  print("aaaaaa")
      
      except:
          
          print("--------")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  