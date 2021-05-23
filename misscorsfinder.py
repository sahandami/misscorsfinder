#!/usr/bin/python3

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import urllib3
import os
import sys
import time
from subprocess import check_output

os.system('> corsmis')

pwd = check_output('pwd').strip()
filename_demo = sys.argv[1]
pwd = pwd.decode('utf-8')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def reqsender(url):
        url = url[:-1]
        res = requests.get(url, headers={'Origin': url}, verify=False, stream=True)
        #print(res.headers)
        #print(url)
        if 'Access-Control-Allow-Origin' in res.headers:
                print(url,'\033[1;31;40m  =>[Access-Control-Allow-Origin] \033[1;37;40m')
                file1 = open('corsmis', 'a')
                file1.write(url+'\n')
                file1.close()

        elif 'Access-Control-Allow-Credentials' in res.headers:
                print(url,'\033[1;31;40m  =>[Access-Control-Allow-Credentials] \033[1;37;40m')
                file1 = open('corsmis', 'a')
                file1.write(url+'\n')
                file1.close()

        elif 'access-control-allow-origin' in res.headers:
                print(url,'\033[1;31;40m  =>[access-control-allow-origin] \033[1;37;40m')
                file1 = open('corsmis', 'a')
                file1.write(url+'\n')
                file1.close()

        elif 'access-control-allow-credentials' in res.headers:
                print(url,'\033[1;31;40m  =>[access-control-allow-credentials] \033[1;37;40m')
                file1 = open('corsmis', 'a')
                file1.write(url+'\n')
                file1.close()
        else:
                print(url)

filename = 'b{}/{}'.format(pwd, filename_demo)[1:]
print(filename)
file = open(filename, 'r')
Lines = file.readlines()
file.close()

processes = []
with ThreadPoolExecutor(max_workers=20) as executor:
        for line in Lines:
                url = line[:-1]
                processes.append(executor.submit(reqsender,line))