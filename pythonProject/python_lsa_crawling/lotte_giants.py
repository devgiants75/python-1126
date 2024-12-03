### 롯데 자이언츠 경기 일정 페이지의 정보 ###

import requests

# 페이지 Url
# : https://www.giantsclub.com/html/?pcode=257

# 기본 BASE URL
# : 'https://www.giantsclub.com/html/'

base_url = 'https://www.giantsclub.com/html/'

# URL 파라미터 설정
paramss={'pcode': '257'}

# User-Agent 설정
# : 웹 서버의 차단을 피하기 위해 설정
headerss = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

response = requests.get(base_url, params=paramss, headers=headerss)

# 조건문을 사용한 상태 코드 관리
# if response.status_code == 200:
    # print(response.text)
# else:
    # print(f'Error: {response.status_code}')
    
### BeautifulSoup 라이브러리를 사용하여 데이터 추출 ###
from bs4 import BeautifulSoup

html = response.text

soup = BeautifulSoup(html, 'html.parser')

a_tag = soup.find('a')
print(a_tag.text) # 메인메뉴 바로가기

a_tag_href = soup.find('a').get('href')
print(a_tag_href) # #inner_nav

span_tag = soup.find_all('span')
for tag in span_tag:
    print(tag.text)