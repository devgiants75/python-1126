### 네이버 스포츠 뉴스 헤드라인 크롤링 ###

import requests
from bs4 import BeautifulSoup

naver_sports_news='https://sports.news.naver.com/kbaseball/index'

response_news = requests.get(naver_sports_news)
html_news = response_news.text
soup = BeautifulSoup(html_news, 'html.parser')

# select 메서드로 원하는 태그를 찾기
# class 속성: .클래스명
# id 속성: #아이디명
headlines = soup.select('.link_news_end')
print(headlines)

for headline in headlines:
    print(headline.text.strip())
# 문자열.strip(): 문자열 양 끝의 공백과 줄바꿈을 제거