'''
python_lesson_11_scope -> main.py

scope : 범위

지역 변수 - 함수 내부에 정의된 변수
전역 변수 - 함수 외부에 정의된 변수
'''

# enemies = 1         # 전역 변수인 enemies = 1
#
# def increase_enemies():     # 함수를 정의
#     enemies = 2             # 지역 변수인 enemies = 2
#     print(f"함수 내부의 적은 {enemies}명입니다.")
#
# increase_enemies()          # 함수 호출
# print(f"함수 외부의 적은 {enemies}명입니다.")

# 함수 정의
def drink_potion():
    potion_strength = 2         # 지역 변수인 potion_strength
    print(potion_strength)

# drink_potion()      # 함수 호출
# print(potion_strength)        # 지역 변수가 선언되고, 이를 호출한다고 해서 이를 전역(main)에서 해당 변수를
                                # 참조할 수 없음

# Global Scope

player_health = 10      # 전역 변수

# 함수 정의
# def game():
#     # 함수 내부에 함수를 정의
#     def drink_potion():
#         global player_health        # global 선언 후에 값을 바꿀 전역 변수 명을 작성 ->
#         player_health += 2          # 함수 하나가 전역 변수 값을 바꾸게 되면
#                                     # 함수를 호출할 때마다 그 값이 바뀌기 때문에
#                                     # 정확한 판단을 위해서 함수 호출 횟수를 알아야 함.
#                                     # 이상을 이유로 함수가 전역 변수의 값을 바꾸는
#                                     # 코딩 방식은 선호되지 않는 편임.
#         print(f"현재 플레이어의 체력인 {player_health}로 증가되었습니다.")
#
#     # 함수 내부에서 정의된 함수 호출
#     drink_potion()

# game()

game_level = 3

def create_enemy():
    enemies = ["좀비", "스켈레톤", "에일리언"]        # list의 선언 및 초기화 / 지역 변수
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()  # 해당 부분은 new_enemy가 if 내부에 있어도 main단계에서 불러낼 수 있음 -> 오류 안생김.
'''
if, while, for와 같이 콜론을 기준으로 들여쓰기가 있는 모든 코드 블록은
지역 범위를 만드는 것으로 간주되지 않음 -> 지역 변수의 용어 정의에 주목할 필요가 있습니다.
'''







