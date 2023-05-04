#Made by 金日成
import cloudscraper
import random
import time

url = "https://open.open2ch.net/test/bbs.cgi"

lines = open('corpus.txt', encoding="utf-8").read().splitlines()

headers = {
        "referer": "https://open.open2ch.net/test/read.cgi/",
	"sec-fetch-dest": "empty",
	"x-debug-options": "bugReporterEnabled",
	"sec-fetch-mode": "cors",
        "sec-ch-ua-platform": "Windows",
	"sec-fetch-site": "same-origin",
	"accept": "*/*",
        "Cookie": "", # Headerに表示されているCookieの値を入力
	"accept-language": "en-GB",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64",
	"X-Requested-With": "XMLHttpRequest"
}

scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    }
)

for i in range(50):
    time.sleep(random.uniform(3,5))
    response = scraper.post(url, data={
    'MESSAGE': random.choice(lines), #
    'bbs': "", #板を指定
    'key': "", #スレッド番号を指定
    'submit': "書"
    },

    #chars = list(range(97, 122)) + list(range(12354, 12435))
    #response = scraper.post(url, data={
    #'MESSAGE': random.choice(lines),
    #'bbs': "",
    #'key': "",
    #'submit': "書"
    #},
 headers=headers)
    print(response.text)
