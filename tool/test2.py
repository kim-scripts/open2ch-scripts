import requests
from os import path
import os
from bs4 import BeautifulSoup
import re

print(path.join(path.dirname(__file__),'ita.txt'))

os.system('cls')

header = {
    'user-agent':'Mozilla/5.0'
}

def sq_o2ch(name):
    r = requests.get(f'https://open.open2ch.net/{name}/',headers=header)

    soup = BeautifulSoup(r.text,"html.parser")
    data_list = soup.find_all(id=re.compile("form_"))
    count = 0
    directory = path.join(path.dirname(__file__),'ita.txt')
    for data in data_list:
        id = data.attrs["id"]
        open(directory,"w",encoding="utf_8").write(id)

sq_o2ch('nohara')