# matplotlib 라이브러리 #

#! 3. scatter() 함수
#? : 2차원 데이터에 대한 선점도를 그리는데 사용
#* : 데이터 포인트 간의 관계를 시각화 하는데 사용

import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)

x = [1, 2, 3, 4, 5, 6]
y = [6, 4, 1, 2, 7, 5]

# 커스터마이징 (데이터에 대한 크기, 색상 지정 - 옵션)
area = [50, 100, 150, 200, 250, 300]
color = ['red', 'green', 'blue', 'orange', 'aqua', 'crimson']

axes.scatter(x, y, area, color)
plt.show()