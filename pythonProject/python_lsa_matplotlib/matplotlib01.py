# matplotlib01.py

# matplotlib 라이브러리 사용
# : pyplot 모듈을 사용
# : 이름을 plt로 수정하는 import 형식을 사용
import matplotlib.pyplot as plt

# 1. figure & subplot

# figure
# : 하나의 그래프 창을 나타냄, 여러 개의 subplot을 포함 가능
# - 사용법 -
# : plt.figure() 함수를 사용하여 Figure 객체를 생성
# : plt.figure(figsize=(너비, 높이)) - 선택적

figure = plt.figure(figsize=(8, 6)) # 너비가 8, 높이가 6인 Figure을 생성

# subplot
# : 실제로 그래프를 그리는 영역
# - 사용법 -
# : add_subplot() 함수를 사용하여 Figure 안에 subplot을 추가
# >> 3가지 파라미터를 필요로 함
#       첫 번째(nrows): 그리드의 행 수
#       두 번째(ncols): 그리드의 열 수
#       세 번째(index): 그래프를 그릴 위치 (1부터 시작)

# 2행 2열의 subplot을 생성

# vsc 단축키: 줄복사(alt + shift + 방향키)
axes1 = figure.add_subplot(2, 2, 1) # 2행 2열 1번째 subplot
axes2 = figure.add_subplot(2, 2, 2) # 2행 2열 2번째 subplot
axes3 = figure.add_subplot(2, 2, 3) # 2행 2열 3번째 subplot
axes4 = figure.add_subplot(2, 2, 4) # 2행 2열 4번째 subplot

# 그래프 출력
plt.show()

# 여러 개의 subplot을 동시에 생성
# : subplots() 함수를 사용
axes = plt.subplots(nrows=3, ncols=3)
plt.show()