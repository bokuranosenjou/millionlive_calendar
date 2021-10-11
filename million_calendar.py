from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://idolmaster-official.jp/schedule/?b=MILLIONLIVE")

def get_calendar(original_html):
    bs = BeautifulSoup(original_html,"html.parser")
    datelist = bs.find_all("div",class_="date")
    textlist = bs.find_all("p",class_="text")
    for (date,text) in zip(datelist,textlist):
        print(f'{date.get_text()}:{text.get_text()}')

if __name__ == "__main__":
    get_calendar(html)