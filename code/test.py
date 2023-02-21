
import sys
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}




def sqli_exploit_get_csrf(s, url):
    res = s.get(url + '/login?', verify=False, proxies=proxies)
    csrf_soup = BeautifulSoup(res.text, 'html.parser')
    csrf_token = csrf_soup.find("magic")['value']
    print("magic code is here " + csrf_token)
    return csrf_token


def sqli_exploit_login(s,csrf):
    data = {'4Tredir':'https://www.google.com/','magic': csrf, 'username': '20BCS5005', 'password': 'Jatin@410'}
    res = s.post(url+'/login?', data=data, verify=False, proxies=proxies)
    if 'LOGOUT' in res.text:
        print("[+] Logged in succesfully ")
    else:
        print("[-] logged in failed for final login")
    return True


if __name__ == "__main__":
    try:
        url = "http://172.15.15.1:1000"
        s = requests.session()
        num = sqli_exploit_get_csrf(s,url)
        if sqli_exploit_login(s,num):
            print("logged in succesfully")
        else:
            print("failed")
    except IndexError:
        print("failed")

