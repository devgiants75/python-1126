import matplotlib.pyplot as plt
import numpy as np

# 데이터
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [17, 12, 12, 11, 12, 9, 7]
rainfall = [5, 8, 15, 20, 25, 10, 5]

cities = ['NY', 'LA', 'CCG', 'HT', 'SSC']
months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
# 임의의 월간 강수량 데이터 생성 (50~300 mm)
monthly_rainfall = np.random.randint(50, 300, size=(len(cities), len(months)))

# 서브플룻 생성 (1행 1열)
# : 한 개의 그래프를 배치 (전체 크기를 12X10 인치로 설정)
fig, ax_combined = plt.subplots(figsize=(12,10))

# 1. 다중 축 차트: 시간 흐름에 따른 온도와 강수량
ax_temp = ax_combined # 온도 데이터를 그릴 축
ax_rain = ax_combined.twinx() # 동일한 x축을 공유하면서 강수량 데이터를 그릴 새로운 축 생성

# 1-1) 온도 라인 차트
ax_temp.plot(days_of_week, temperatures, marker='o', color='red', label='Temperature (℃)')
ax_temp.set_xlabel('Day of the Week')
ax_temp.set_ylabel('Temperature (℃)', color='red')
ax_temp.tick_params(axis='y', labelcolor='red') # y축 눈금과 레이블 색상 설정
ax_temp.set_title('Daily Temperature and Rainfall')

# 1-2) 강수량 막대 그래프
ax_rain.bar(days_of_week, rainfall, alpha=0.5, color='blue', label='Rainfall (mm)')
ax_rain.set_ylabel('Rainfall (mm)', color='blue')
ax_rain.tick_params(axis='y', labelcolor='blue') # y축 눈금과 레이블 색상 설정

# 범례 추가
ax_temp.legend(loc='upper left')
ax_rain.legend(loc='upper right')

plt.show()