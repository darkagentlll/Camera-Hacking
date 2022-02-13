# █▀▀ ▄▀█ █▀▄▀█ █▀▀ █▀█ █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀ #
# █▄▄ █▀█ █░▀░█ ██▄ █▀▄ █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█ #
import requests
from shodan import Shodan
from colorama import Fore
import os
import re
from bs4 import BeautifulSoup
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
try:
    os.system('cls')
except:
    os.system('clear')
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
color_3 = Fore.RED
print(color_3+r'''
       _________
      / ======= \
     / __________\
    |  _________  |
    | | >_      | |
    | |         | |
    | |_________| |
    \=____________/   
    / """"""""""" \                       
   / ::::::::::::: \                  
  (_________________) 
  ''')
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
color_1 = Fore.YELLOW
print(color_1+'[1]Newest Cameras Hacking')
print(color_1+'[2]Camera Hacking Dorks ')
print(color_1+'[3]Scan Ip')
print(color_1+'[4]Ip Range Generator')
print(color_1+'[5]Site Open Camera')
print          ('|')
num = int(input('└──╼ ✞ Enter Your Number ✞ : '))
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
if num == 1:
    api = Shodan("4Y6enwWyp4hmu6YsZJBPzEXwbiTzIqNd")
    results = api.search('webcamxp')
    for result in results['matches']:
        color_2 = Fore.MAGENTA
        print(color_2+str(result['ip_str']) + ":" + str(result['port']))
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
elif num == 2:
    with open('dorks.txt', 'r', encoding='utf-8')as file:
        dork = file.read()
        color_4 = Fore.BLUE
        print(color_4+dork)
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
elif num == 3:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.webportscanner.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'http://www.webportscanner.com/',
        'Upgrade-Insecure-Requests': '1',
    }

    data = {
    'domain': input('Enter Url: '),
    'action': 'Scan'
    }

    response = requests.post('http://www.webportscanner.com/', headers=headers, data=data)

    soup = BeautifulSoup(response.text,'html.parser')
    finder = soup.find('div',{'class':'output'}).find_all('span')
    for i in finder:
        print(i.text)
    
# 卐 卐 卐 卐 卐 卐 卐 卐 卐
elif num == 4:
    start_ip = input('Enter Start Ip: ')
    end_ip = input('Enter End Ip: ')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://ipgen.hasarin.com',
        'Connection': 'keep-alive',
        'Referer': 'https://ipgen.hasarin.com/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    data = {
        'iprangetype': 'plain',
        'ipstart': f'{start_ip}',
        'ipend': f'{end_ip}',
        'ipcidr': '',
        'mask': '32'
    }

    response = requests.post(
        'https://ipgen.hasarin.com/iprange', headers=headers, data=data)

    regex = re.sub('''<!doctype html>|</head>|<html class="no-js" lang="">|<head>|<body>
           |<a href="/">Back</a>|<br>|</html>|<title>Range list</title>|<body>|</body> ''', '', response.text)

    print(regex.replace('</body>','').replace('','').strip())
 # 卐 卐 卐 卐 卐 卐 卐 卐 卐  
elif num == 5:
    color_5 = Fore.LIGHTCYAN_EX
    print(color_5+'''
    http://www.insecam.org/
    http://www.opentopia.com/
    https://www.earthcam.com/
    ''')