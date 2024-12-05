# crawling02.py

# 셀레니움을 사용하여 뉴스 제목을 자동으로 추출

# 뉴스 제목의 태그와 속성 파악
# 네이버 메인 화면 - kpop 검색 - 개발자 도구 열기(f12)

#? <a href="https://en.yna.co.kr/view/AEN20241205010400315?input=2106m" class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws_all*e.tit&amp;r=1&amp;i=880000D8_000000000000000015087320&amp;g=001.0015087320&amp;u='+urlencode(this.href));" title="Rose's 'APT.' sets record as fastest K-pop song to reach 500 mln views">Rose's 'APT.' sets record as fastest <mark>K</mark>-<mark>pop</mark> song to reach 500 mln views</a>

# class 속성
# : 태그를 지시하기 위해 사용 (같은 class 이름 사용 가능)

# 드라이버.find_elements(By.CLASS_NAME, "클래스명")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# chrome://settings/help

options = Options()

driver = webdriver.Chrome(options=options)

url = 'https://www.naver.com'
driver.get(url)

query = driver.find_element(By.ID, "query")
query.send_keys("kpop")

query.send_keys(Keys.RETURN)

news_tit = driver.find_elements(By.CLASS_NAME, "news_tit")

for title in news_tit:
    print(title.text)
    
input("...")
driver.quit()