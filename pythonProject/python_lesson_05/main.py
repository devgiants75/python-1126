'''
reeborg's world hurdle #1
# 사용자 정의 함수 정의 방법의 예시 -> 추후 설명 예정
def turn_right():
    turn_left()
    turn_left()
    turn_left()

for _ in range(6):
    move()
    turn_left()
    move()
    turn_right()    -> 사용자 정의 함수 호출(call)
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

# 허들 하나를 넘는 사용자 정의 함수
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for _ in range(6):
    jump()


# hurdle #2

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()

hurdle # 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

hurdle # 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()


p 36

문자열 인덱싱(indexing)
str = string(: '줄'이라는 의미)
index란 : 문자열을 구성하는 모든 문자에 부여한 고유의 번호. 시작 번호는 0
    번호는 문자가 들어가 있는 주소라고 생각할 수 있다. a[0]은 a라는 문자열의 [0]번째로 찾아간다는 의미.

마이너스 인덱스 : 문자열의 뒤에서 부터 부여하는 번호. 마지막 문자의 인덱스는 -1이다.
'''
string_example = "excellent"

# print(string_example[0])
# print(string_example[1])
# print(string_example[2])
# print(string_example[3])
# print(string_example[4])
# print(string_example[5])
# print(string_example[6])
# print(string_example[7])
# print(string_example[8])
#
# print()
#
# print(string_example[-1])
'''
문자열 슬라이싱(slicing) : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용하는 방법

형식 : a[시작인덱스:종료인덱스:증감값]

*
시작인덱스 : 생략하면 처음부터 추출합니다.
종료인덱스 : 생략하면 끝까지 추출합니다. -> 생략하지 않으면 종료인덱스 이전까지 추출함.
증감값 : 생략하면 1씩 변화합니다.
'''
# a = "apple"
# print(a[:2:])
# 보통 증감값은 코딩에서 자주 쓰이지 않고 시작/종료 인덱스만 지정하는 편이나 자격증 시험 등에서 증감값이 나옴.
# b = "banana"
# print(b[:4:2])
# print(b[-3])
'''
기본 예시

네 자리 숫자를 입력 받아 그 숫자의 맨 마지막 자리를 출력하시오.
실행 예
네 자리 숫자를 입력하세요 >>> 2024
맨 마지막 자리의 숫자는 4입니다.
'''
# num = input("네 자리 숫자를 입력하세요 >>> ")
# print(f"맨 마지막 자리의 숫자는 {num[3]}입니다.")
# print(f"맨 마지막 자리의 숫자는 {num[-1]}입니다.")
'''
응용 예제
미세 먼저 저감 활동의 일환으로 차량 2부제를 실시하고자 합니다. 사용자로부터 차량 번호를 입력 받아 차량 번호가
짝수로 끝나면 '운행가능', 아니면 '운행 불가'가 출력되는 프로그램을 구현하세요.
단, 차량 번호는 '237가1234'와 같은 형식으로 입력받는다고 가정합니다.

실행 예
차량 번호를 입력하세요 >>> 237가1234
차량번호 237가1234는 오늘 운행가능입니다.
'''
# car_num = input("차량 번호를 입력하세요 >>> ")
# 차량 번호가 홀/짝수인지 판별하기 위해서는 맨 마지막 숫자만 뽑아내면 됨 -> car_num[-1]
# last_car_num = int(car_num[-1])
# if last_car_num % 2 == 0:
#     driving = "운행 가능"
# else:
#     driving = "운행 불가능"
# print(f"차량번호 {car_num}은 오늘 {driving}입니다.")

'''
차량 번호를 입력 받아서 그 차량 번호의 뒤 네 자리를 인덱스 / 마이너스 인덱스를 이용하여 추출하시오.
차량 번호를 입력하세요 >>> 370수5690
차량 번호의 뒤 네 자리는 5690입니다.

차량 번호를 입력하세요 >>> 27가1234
차량 번호의 뒤 네 자리는 1234입니다.
'''
car_num = input("차량 번호를 입력하세요 >>> ")
# 인덱스 사용
# 앞 자리가 세 자리인 경우 370수5690 -> 012->앞자리 3->문자 4567->뒷자리
# last_car_num = car_num[4::]     # 슬라이싱에서 시작인덱스를 기준으로 끝까지 추출
# print(last_car_num)
# 앞 자리가 두 자리인 경우 27가1234 01 -> 앞자리 2 -> 문자 3456 -> 뒷자리
# last_car_num = car_num[3::]
# print(last_car_num)

# 마이너스 인덱스
# last_car_num = car_num[-4::]
# print(last_car_num)
