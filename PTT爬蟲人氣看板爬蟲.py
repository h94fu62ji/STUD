import requests
from bs4 import BeautifulSoup

all = 0
re = requests.get("https://www.ptt.cc/bbs/hotboards.html")
soup_PTT = BeautifulSoup(re.text, "html.parser")
all_boards = soup_PTT.findAll("div",{"class":"b-ent"})
for board in all_boards:
    name = board.find("div",{"class":"board-name"}).text
    user_count = board.find("div",{"class":"board-nuser"}).text

    all += 1

    if int(user_count) >= 1 :
        print(name,user_count)
print("總看板數",all)