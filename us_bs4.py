import request
import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get (url)
    if response.status_code == 200:
     print(f'sukses!! response = {response.status_code}')
     #print (f'content {response.text}')
     soup = BeautifulSoup (response.text, features="html.parser")
     print (f'Hasil pemanggilan {url}')
     print (f'Title: {soup.title.string}')
    else:
        print (f'woopss, ada kesalahan requests {response.status_code}')
except Exception as e :
    print ('ada error', e)