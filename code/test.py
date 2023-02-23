
import sys
import requests
import urllib3
import urllib
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def sqli_exploit_get_csrf(s, url):
    header = {
        "Host": "172.15.15.1:1000",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Sec-GPC": "1"
    }
    res = s.get(url+'/login?279ru2020482',headers=header,verify=False,proxies=False)
    csrf_soup = BeautifulSoup(res.text, 'html.parser')
    csrf_token = csrf_soup.find_all('input')[1].get('value')
    print("magic code is here " + csrf_token)
    return csrf_token


def sqli_exploit_login(s, csrf):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://172.15.15.1:1000",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Sec-GPC": "1"
    }
    data = {'4Tredir': 'https://www.google.com/', 'magic': csrf,
            'username': '20BCS5005', 'password': 'Jatin@410'}
    res = s.post(url+'/login?', headers=header, data=data,
                 verify=False, proxies=False)
    if 'LOGOUT' in res.text:
        print("[+] Logged in succesfully ")
    else:
        print("[-] logged in failed for final login")
    return True


if __name__ == "__main__":
    try:
        url = "http://172.15.15.1:1000"
        s = requests.session()
        num = sqli_exploit_get_csrf(s, url)
        if sqli_exploit_login(s, num):
            print("logged in succesfully")
        else:
            print("failed")
    except IndexError:
        print("failed")
