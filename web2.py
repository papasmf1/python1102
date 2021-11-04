# web2.py 
#웹서버에 요청 
import urllib.request
#웹크롤링 
from bs4 import BeautifulSoup

#파일에 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
#수열함수로 페이지 번호를 1 ~ 5생성
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    data = urllib.request.urlopen(url)

    #검색이 용이한 객체를 생성
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")

    #반복해서 가져오기
    for tag in cartoons:
        title = tag.find("a").text 
        print( title.strip() ) 
        f.write(title.strip() + "\n")  

f.close() 
 

         