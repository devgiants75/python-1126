# matplotlib 라이브러리 한글 처리 #

# matplolib 라이브러리 내의 
#   font_manager, rc 를 사용하여 한글 폰트 등록

# C:\Windows\Fonts\H2PORM.TTF

from matplotlib import font_manager, rc

import matplotlib.pyplot as plt
import matplotlib

# 폰트 경로 직접 지정
font_path = 'C:\\Windows\\Fonts\\H2PORM.TTF'

# 폰트 이름 가져오기
font_name = font_manager.FontProperties(fname=font_path).get_name()

# matplotlib과 rc 함수를 사용하여 폰트 설정
matplotlib.rc('font', family=font_name)

x = ['봄', '여름', '가을', '겨울']
y = [20, 30, 15, 10]

plt.plot(x, y)
plt.title('한글 깨짐 방지')
plt.show()