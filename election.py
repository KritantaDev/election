# election.py
# License is BSD-1 clause ; Don't relicense my code, that's all I care about

import requests
from bs4 import BeautifulSoup
import os, time, json, sys
from collections import namedtuple 
Candidate = namedtuple("Candidate", ('name', 'electoral', 'percentage', 'count'))

if sys.stdout.isatty() and 'noterm' not in sys.argv:
    print("Running in terminal context, updating every 10 seconds on loop")

while True:
    url = "https://www.google.com/search?q=election+results&rlz=1C1SQJL_enUS909US911&oq=election+results&aqs=chrome.0.0i67i131i433i457j0i20i131i263i433j0i131i433j0i67j0i131i433l2j69i60l2.1612j0j9&sourceid=chrome&ie=UTF-8"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    blox = soup.body.select('#main #search div table td span')
    trump = Candidate('Trump', blox[0].get_text(), blox[1].get_text(), blox[2].get_text())
    biden = Candidate('Biden', blox[3].get_text(), blox[4].get_text(), blox[5].get_text())

    if sys.stdout.isatty() and 'noterm' not in sys.argv:
        print(trump)
        print(biden)
    
    else:
        fun = [
            {
                'candidate':'Trump',
                'electoral':trump.electoral,
                'percentage':trump.percentage,
                'count':trump.count
            },
            {
                'candidate':'Biden',
                'electoral':biden.electoral,
                'percentage':biden.percentage,
                'count':biden.count
            }
        ]
        
        print(json.dumps(fun))
        break
    
    if requests.get("https://raw.githubusercontent.com/KritantaDev/election/main/update1").status_code == 200:
        if requests.get("https://raw.githubusercontent.com/KritantaDev/election/main/update1").text == 'update':
            print("UPDATE AVAILABLE - REDOWNLOAD FROM https://github.com/kritantadev/election OR RUN git pull")
    time.sleep(10)