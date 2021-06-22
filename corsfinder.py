#!/usr/bin/python3

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import urllib3
import os
import sys
import time
from subprocess import check_output


pwd = check_output('pwd').strip()
filename_demo = sys.argv[1]
pwd = pwd.decode('utf-8')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def reqsender(url):
        url = url[:-1]

        origind = url.split('http')[1].split('/')[2]
        if url[:5] == 'https':
                origin = 'https://'+origind

        elif url[:4] == 'http':
                origin = 'http://'+origind

        res = requests.get(url, headers={'Origin': origin}, verify=False, stream=True)
        #print(res.headers)
        #print(url)
        if 'Access-Control-Allow-Origin' in res.headers:

                if 'Access-Control-Allow-Credentials' in res.headers:
                        print(url,'\033[1;31;40m  =>[Access-Control-Allow-Credentials] \033[1;37;40m')
                        file1 = open('corsmis', 'a')
                        file1.write(url+'[ACAC]\n')
                        file1.close()

        else:
                print(url)

filename = 'b{}/{}'.format(pwd, filename_demo)[1:]
print(filename)
file = open(filename, 'r')
Lines = file.readlines()
file.close()

processes = []
with ThreadPoolExecutor(max_workers=100) as executor:
        for line in Lines:
                url = line[:-1]
                processes.append(executor.submit(reqsender,line))
