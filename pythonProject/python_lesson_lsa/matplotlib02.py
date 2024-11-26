# matplotlib 라이브러리 #

# 1. plot() 함수
# : 선 그래프를 그리기 위한 함수 (꺾은 선형 그래프)
# : x값, y값을 사용하여 2차원 선 그래프 생성
# : plot(x, y)
#   >> x와 y의 값에 각각 데이터를 리스트 형태로 전달

import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111) # 1행 1열 1번째

# x축의 값
x1 = [0, 1, 2, 3, 4]
x2 = [0, 1, 2, 3, 4]

# y축의 값
y1 = [4, 1, 3, 5, 2]
y2 = [1, 7, 5, 3, 1]

# plot() 함수 커스터마이징
# 1. linestyle: 선 스타일 설정 (실선: solid, 점선: dotted, 대시: dashed)
# 2. linewidth: 선 두께 설정 (pt 포인트 단위의 실수)
# 3. color: 선 색상 설정 (영단어 키워드 사용)
# 4. marker: 각 데이터의 포인터에 대한 마커 설정(원: o, 삼각형: ^, 사각형: s)

axes.plot(x1, y1, color='red', linestyle='dotted', marker='o')
axes.plot(x2, y2, color='blue', linestyle='dashed', marker='s')

plt.title('Data Visualization - plot')
plt.xlabel('x축')
plt.ylabel('y축')

plt.show()