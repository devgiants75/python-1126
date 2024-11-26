'''
python_lesson_17_prettyTable -> main.py

외부 패키지 설치 방법

좌측 상단 메뉴 버튼 클릭(햄버거 모양) -> setting(설정) 클릭 혹은 ctrl + alt + s
-> 좌측 리스트에서 project : 프로젝트명으로 돼있는 부분 클릭
-> python interpreter
-> + 버튼 눌러서 필요한 패키지 설치
'''
from prettytable import PrettyTable     # 모듈 불러오는 방식 기억하셔야 합니다. from 모듈명 import 클래스명
from pokemon_data import pokemon_data

# PrettyTable 클래스의 객체 생성
table = PrettyTable()

# 객체의 fied_names 속성에 값 대입
table.field_names = ["번호", "이름", "속성"]
# table.add_row([pokemon_data[0][0], pokemon_data[0][1], pokemon_data[0][2]])
# table.add_row([pokemon_data[1][0], pokemon_data[1][1], pokemon_data[1][2]])
# table.add_row(pokemon_data[2])
#반복문을 사용하여 pokemon_data에 있는 모든 데이터를 prettytable로 정리하시오.

# in range를 이용한 고전적 for문 사용
# for i in range(26):             # 인덱스의 개수를 정확하게 알고 있어야만 하는 단점이 있음
#     table.add_row(pokemon_data[i])

# for i in range(len(pokemon_data)):  # 인덱스 넘버를 몰라도 쓸 수 있도록 len() 함수 활용
#     table.add_row(pokemon_data[i])

# 향상된 for문 활용
for pokemon in pokemon_data:
    table.add_row(pokemon)

print(table)

