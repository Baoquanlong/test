from bs4 import BeautifulSoup
import os 
import re
import requests
head = {

    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2772.25 Safari/537.36'
}

data = bytes('hello world')
url = 'https://translate.google.cn/?sl=auto&tl=en&text'
html = requests.post(url,data)
bs = BeautifulSoup(html,'html.parser')
print(bs)
