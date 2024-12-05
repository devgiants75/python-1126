# crawling.py #

# 웹 크롤링
# : 웹 페이지의 데이터를 자동으로 추출하는 과정

# cf) request 라이브러리
# : 웹 페이지의 웹 문서에 대한 정보를 가져오는 요청을 위한 라이브러리

# === 셀레니움(Selenium) ===
# : 웹 크롤링을 지원하는 프레임워크

# cf) 프레임워크(frame + work)
# frame(틀) + work(일하다): 제공받은 일정한 요소와 틀, 규약을 가지고 무언가를 만드는 일

# cf) BeautifulSoup
#   : request 라이브러리로 가져온 웹 문서에서 데이터를 추출하는 라이브러리

# 셀레니움 사용 이유
# : BeautifulSoup보다 데이터의 추출이 용이
# : 동적 페이지에서 틀과 별도로 호출된 정보를 추출, 사용자 이벤트까지 크롤링이 가능

# 셀레니움 사용 방법
# 1) selenium 설치
# : pip install selenium

# cf) pip 설치 목록 확인: pip list

# 2) 크롬 웹 드라이버 다운
# : https://developer.chrome.com/docs/chromedriver/downloads?hl=ko
# : https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.87/win64/chromedriver-win64.zip

# 3) 셀레니움으로 브라우저 창 열기
# : 셀레니움으로 원하는 주소를 자동으로 실행하는 웹 브라우저 구동

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome://settings/help

options = Options()

driver = webdriver.Chrome(options=options)
url = 'https://www.naver.com'
driver.get(url)

# === 네이버 자동 검색 수행 ===
# 1. 네이버 메인 페이지 접속(www.naver.com)
# 2. 오른쪽 마우스 클릭 > 바로가기 메뉴 > [페이지 소스 보기] 클릭
# 3. 열리는 창에서 ctrl + F: 검색창 열기
# 4. input 입력: 태그 검색

#? <input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element/>

# id 속성: 특정 태그를 지시하기 위해 사용되는 속성 (중복 X)
# class 속성: 여러 태그를 하나로 지시하기 위해 사용되는 속성 (중복 O)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 5. id 값 확인 > 해당 태그 불러오기
# : find_element(By.ID, "아이디명")
query = driver.find_element(By.ID, "query");

# 6. 해당 요소(태그)에 대한 작업 수행
# 1) send_keys(키 입력값): 키보드를 통한 키 입력
# 2) click(): 마우스를 통한 클릭

query.send_keys("파이썬") # 검색창에 "파이썬" 입력
query.send_keys(Keys.RETURN) # Enter 키 입력 (검색 실행)

input("...")
driver.quit()