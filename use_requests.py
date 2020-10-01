import request
import requests

url = 'https://detik.com'
try:
    response = requests.get (url)
    if response.status_code == 200:
     print(f'sukses!! response = {response.status_code}')
     print (f'content {response.text}')
    else:
        print (f'woopss, ada kesalahan requests {response.status_code}')
except Exception as e :
    print ('ada error', e)














