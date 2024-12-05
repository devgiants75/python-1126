### 실습) 원하고자하는 페이지의 데이터 수집 ###


import requests
from bs4 import BeautifulSoup

api_url='https://www.mcdonalds.co.kr/kor/menu/list.do'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    
    # 'burger' 카테고리의 메뉴 아이템 추출
    for category in data.get('categories', []):
        if category.get('code') == 'burger':
            for item in category.get('items', []):
                print(item.get('name_ko'))  # 한글 이름 출력
else:
    print(f'{response.status_code}')


