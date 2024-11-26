# 파이썬 데이터 시각화 #

# Matplotlib 라이브러리 사용법
# : 외부 라이브러리 - 설치 후 사용
# : pip install matplotlib 명령어를 사용하여 설치

# Matplotlib의 pyplot 모듈을 불러옴 (plt라는 별칭으로 가져옴)

# 'as': alias의 축약어 (별칭)
import matplotlib.pyplot as plt

# 차트에 사용할 데이터 준비
x = [1, 2, 3, 4, 5] # x축 데이터
y = [10, 20, 25, 30, 35] # y축 데이터

# 그래프 생성
plt.plot(x, y) # 선 그래프 생성
plt.title('Simple Line Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show() # 그래프 표시