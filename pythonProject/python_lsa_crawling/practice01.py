### 영화 예매 사이트(CGV) 정보 추출 ###

# >>> 보안에 따른 접근 방지: 코드 실행의 결과를 확인 불가 <<<

import requests
from bs4 import BeautifulSoup

url='https://www.cgv.co.kr/'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

class_elements = soup.find_all('div', class_='movieName')
for element in class_elements:
    print(element.text)