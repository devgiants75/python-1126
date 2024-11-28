### 파이썬 데이터 시각화 예제 ###

# 라인 차트 생성
# : 시간의 경과에 따른 데이터의 변화를 보여주는 예제
# > 일주일 간의 온도 변화를 나타내는 차트

import matplotlib.pyplot as plt;

# 1행 2열의 subplot 구성
# : 각각의 축(ax1, ax2)를 반환
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 데이터 #
# 1. 요일별 기온 변화 그래프 (라인 그래프)
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [17, 12, 12, 11, 12, 9, 7]

ax1.plot(weeks, temperature, marker='o', color='blue', label='Temperature')
ax1.set_xlabel('Day of the Week')

# Windows 이모지 활용: 시작버튼 + .(마침표)
ax1.set_ylabel('Temperature (℃)')
ax1.set_title('Daily Temperatures in November')
ax1.grid(True) # 격자선 추가
ax1.legend() # 범례 추가


# 2. 도시별 강수량 비교 그래프 (막대 그래프)
cities = ['NY', 'LA', 'CCG']
rainfall = [1200, 900, 850]

ax2.bar(cities, rainfall, color='skyblue')
ax2.set_xlabel('City')
ax2.set_ylabel('Annual Rainfall (mm)')
ax2.set_title('Annual Rainfall by City')

plt.show()