# web2.py
#웹서버에 요청 
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#파일 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for i in range(1,11):
    try:
        url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" \
            + str(i)
        print(url)
        data = urllib.request.urlopen(url)
        soup = BeautifulSoup(data, "html.parser")
        cartoons = soup.find_all("td", class_="title")	
        # <td class="title">
        # 	<a href="/webtoon/detail?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
        # </td>
        for item in cartoons:
            title = item.text.strip()
            print(title)
            f.write(title + "\n")
    except:
        pass 
f.close() 

                
