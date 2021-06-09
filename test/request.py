from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import requests


url  = 'https://fagov-api-prd.azurewebsites.us/api/Map/MapData?fundingType=spent&fiscalYear=2020'
head = {

'Host': 'fagov-api-prd.azurewebsites.us'
,'Origin': 'https://foreignassistance.gov'
,'Referer': 'https://foreignassistance.gov/'
,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"'
,'sec-ch-ua-mobile': '?0'
,'Sec-Fetch-Dest': 'empty'
,'Sec-Fetch-Mode': 'cors'
,'Sec-Fetch-Site': 'cross-site'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
,'x-functions-key': '2ARkPz88HONap4guWDEFaI4iCH8vAVpdruaeqSlU2Sd4EWCrb7f4jw=='

}
data = requests.get(headers=head,url =url)
print(data.status_code)
bs = BeautifulSoup(data.text,'html.parser')
# print(bs.prettify())
with open('./worldwild.txt','w+',encoding='utf-8',errors='ignore') as f:
    f.write(str(bs))