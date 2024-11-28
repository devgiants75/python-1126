# matplotlib 라이브러리 #

# 2. bar() 함수
# : 수직 및 수평 막대 그래프를 그리는 데 사용
# : 주로 범주형 데이터의 각 항목에 대한 값을 비교할 때 사용

import matplotlib.pyplot as plt

figure = plt.figure()
axes1 = figure.add_subplot(121) # 1행 2열 1번째
axes2 = figure.add_subplot(122) # 1행 2열 2번째

x = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
y = [8, 6, 5, 11, 3, 9, 2]

# 막대 그래프 커스터마이징
# 1. color: 막대의 색상 설정
# 2. edgecolor: 막대 테두리 색상 설정

axes1.bar(x, y, color='skyblue', edgecolor='black') # bar(): 수직 막대 그래프
axes2.barh(x, y) # barh(): 수평 막대 그래프 (horizon: 수평선)

plt.title('weekday chart')
plt.show()