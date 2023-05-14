import requests
from os import path
from bs4 import BeautifulSoup
import re

print(path.join(path.dirname(__file__),'ita.txt'))


header = {
    'user-agent':'Mozilla/5.0'
}

def sq_o2ch(name,sub_domain):
    r = requests.get(f'https://{sub_domain}.open2ch.net/{name}/',headers=header)

    soup = BeautifulSoup(r.text,"html.parser")
    data_list = soup.find_all(id=re.compile("form_"))
    count = 0
    directory = path.join(path.dirname(__file__),'ita.txt')
    for data in data_list:
        id = data.attrs["id"]
        if count == 0:
            open(directory,"w",encoding="utf_8").write(id)
        else:
            open(directory,"a",encoding="utf_8").write(f"\n{id}")
        count += 1
    return open(path.join(path.dirname(__file__),'ita.txt')).read()