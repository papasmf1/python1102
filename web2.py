# web2.py 
#웹서버에 요청 
import urllib.request
#웹크롤링 
from bs4 import BeautifulSoup

#패키지명.파일명.함수명 
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

#검색이 용이한 객체를 생성
soup = BeautifulSoup(data, "html.parser")
# 다중라인: ctrl + / 
# <td class="title">
# 				<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# 						</td>
cartoons = soup.find_all("td", class_="title")
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

                        