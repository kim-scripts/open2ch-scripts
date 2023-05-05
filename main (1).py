#Made by 金日成
import requests
import random
import time
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
    
url = "https://open.open2ch.net/test/bbs.cgi"

lines = open('corpus.txt', encoding="utf-8").read().splitlines()

headers = {
        "referer": "https://open2ch.net",
	"sec-fetch-dest": "empty",
	"x-debug-options": "bugReporterEnabled",
	"sec-fetch-mode": "cors",
        "sec-ch-ua-platform": "Windows",
	"sec-fetch-site": "same-origin",
	"accept": "*/*",
	"accept-language": "en-GB",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; rv:111.0) Gecko/20100101 Firefox/111.0",
	"X-Requested-With": "XMLHttpRequest"
}

scraper = requests.Session()

for i in range(3):
    scraper.cookies.clear()
    time.sleep(5)
    for i in range(5):
        chars = list(range(97, 122)) + list(range(12354, 12435))
        time.sleep(0.1)
        response1 = scraper.post("https://open.open2ch.net")
        response2 = scraper.post(url, data={
        'MESSAGE': random.choice(lines),
        'bbs': "livejupiter",
        'key': "1683216865",
        'submit': "書"
        },
        headers=headers)
        print(response2.text)
