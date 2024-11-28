# b_wikipedia.py

### 파이썬을 이용한 워드 클라우드 생성 ###
# : 위키피디아 페이지 활용
# : Wikipedia 사이트에서 인공 지능(Articicial Intelligence)를 
#   , 검색한 내용을 기반으로 워드 클라우드를 생성

#! 필요 라이브러리
# WordCloud, matplotlib, wikipedia
# >> wikipedia에서 제공하는 python 라이브러리를 설치
#   : 해당 페이지의 검색 결과를 python으로 쉽게 가져올 수 있음
#   : pip install wikipedia

#! 라이브러리 가져오기(import)
from wordcloud import WordCloud # 워드 클라우드 생성
import matplotlib.pyplot as plt # 워드 클라우드 시각화
import wikipedia # Wikipedia의 내용을 검색하고 추출

#! 텍스트 가져오기
# 1. wikipedia에서 키워드 검색
wiki = wikipedia.search('artificial intelligence')

# 2. wikipedia 페이지의 내용을 추출
# : 위의 검색된 내용의 첫 번째 검색 결과의 상세 페이지로 이동
wiki = wikipedia.page(wiki[0])
text = wiki.content # 페이지의 전체 텍스트 내용을 추출

#! 워드 클라우드 생성
wordcloud = (WordCloud(background_color='white', colormap='winter').generate(text))

#! 워드 클라우드 시각화
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud)
plt.axis('off') # 축 정보를 표시하지 않음
plt.show()