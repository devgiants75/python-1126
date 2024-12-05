# crawlingPractice.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrom_options = Options()

driver = webdriver.Chrome(options=chrom_options)

import time

try:
    driver.get("https://www.youtube.com")
    time.sleep(2)
    
    #? <input name="search_query" type="text" autocomplete="off" autocorrect="off" class="YtSearchboxComponentInput yt-searchbox-input title" placeholder="검색">
    search_box = driver.find_element(By.NAME, "search_query")
    search_keyword = "christmas"
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    
    video_titles = driver.find_elements(By.CSS_SELECTOR, "#video-title")
    
    print(f"'{search_keyword}' 검색결과: ")
    
    # 빈 배열 작성 - 크롤링한 데이터를 저장할 빈 리스트
    titles = []
    for idx, title in enumerate(video_titles, start=1):
        print(f"{idx} - {title.text}")
        
        # .append()를 사용하여 추출한 데이터를 배열의 요소로 저장
        titles.append(title.text)
finally:
    driver.quit()

# 웹 크롤링한 데이터를 활용한 데이터 시각화
# : matplotlib 라이브러리 사용

# 제목 길이 계산
title_lengths = [len(title) for title in titles]

# 데이터 시각화
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(title_lengths, bins=10, edgecolor="black", alpha=0.7)
plt.title("Distribution of Video Title Lengths", fontsize=16)
plt.xlabel('Title Length', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.show()