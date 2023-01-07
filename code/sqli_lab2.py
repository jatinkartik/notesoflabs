import sys
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def get_csrf_token(s,url):
    r = s.get(url,verify=False,proxies=proxies)
    soup = BeautifulSoup(r.text,"html.parser")
    csrf = soup.find("input")['value']
    print(csrf) 

def sqli_exploit(s,url, payload):
    csrf = get_csrf_token(s,url)
    #incomplete 


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print('[-] Usage %s <url> <payload>' % sys.argv[0].strip())
        print('[-] Example %s example.com "payload" ' % sys.argv[0].strip())


    s = requests.Session()

    if sqli_exploit(s,url, payload):
        print('[+] SQL Injection successful')
    else:
        print('[-] SQL Injection failed')
