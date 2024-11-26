'''
python_lesson_04 -> main.py 생성

p 102

반복문(loop)
    어떤 수행 작업을 한 번이 아니라 계속해서 수행해야 할 때 사용하는 방식
    종류 : while / for

while : 특정 조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할 때 사용

형식 :
while 조건식:
    반복실행문

if처럼 들여쓰기가 필수
'''
# while 예문
# num1 = 1
# while num1 < 11:            # num1 = 1이기 때문에 현재 True
#     print(num1)
#     num1 += 1               # 복합대입연산자에 해당       : num1 = num1 + 1
# while문을 사용할 때는 특정 조건에서 조건식이 False로 바뀌게 되는 구간을 설정할 필요가 있음.
'''
기본 예제
1부터 10 사이의 모든 정수를 역순으로 출력하는 프로그램을 작성하시오 -> while문을 사용하여 작성하시오.
'''
# num2 = 10
# while num2 > 0:
#     print(num2)
#     num2 -= 1
'''
while문이 필요한 경우 : while문으로 반복해서 처리해야 할 작업 범위가 명확하지 않을 경우 사용

중첩 if/while문 : if/while문 내에 if/while문이 나타나는 것을 중첩 if/while문 이라고 함.

ex)
총 5일 동안 매일 3 시간씩 수업을 진행합니다. 매일 '1일차 1교시입니다'와 같은 메시지를 출력해야 합니다.
1일차부터 5일차까지의 반복되는 일수와 1교시부터 3교시까지 반복되는 시간이라는 2 개의 반복처리 대상이 있으니
중첩 while문을 사용 해야 합니다.
'''
# day = 1
# while day < 6:              # 1일차 - 5일차까지 출력하기 위해 -> 반복문 5번 반복
#     hour = 1
#     while hour < 4:         # 1교시 - 3교시까지 출력하기 위해 -> 반복문 3번 반복 -> 총 반복 15번
#         print(f"{day}일차 {hour}교시입니다.")
#         hour += 1           # hour를 증가시켜 무한 루프에 빠지지 않기 위해
#     day += 1                # day를 증가시켜 무한 루프에 빠지지 않기 위해
'''
기본 예제

구구단 2단부터 9단까지 출력하는 프로그램을 작성하세요(while문을 사용하여).

실행 결과
2 x 1 = 2
2 x 2 = 4
...
9 x 9 = 81
'''
# dan = 2
# while dan < 10:
#     num = 1
#     while num < 10:
#         print(f"{dan} x {num} = {dan*num}")
#         num += 1
#     dan += 1
'''
1부터 100까지의 모든 정수 중에서 7의 배수만 출력하는 프로그램을 구현하세요.
-> while / if문을 사용해야 함.
-> % 연산자를 사용해야 함.
'''
# num = 1
# while num < 101:
#     if num % 7 == 0:
#         print(num)
#     num += 1
'''
응용 예제

1부터 100까지의 모든 정수 중에서 숫자 하나를 입력 받아 그 숫자의 배수만 출력하는 프로그램을 작성하시오.

실행 예
숫자를 입력하세요 >>> 3
3
6
9
12
...
99
'''
# 위의 문제와 같이 중첩 while/if문을 사용한 풀이
# num1 = 1
# num2 = int(input("숫자를 입력하세요 >>> "))
# while num1 < 101:
#     if num1 % num2 == 0:
#         print(num1)
#     num1 +=1

# 중첩 if문을 사용하지 않는 방법
# num1 = int(input("숫자를 입력하세요 >>> "))
# num2 = 1
# while num1 * num2 < 101:
#     print(num1*num2)
#     num2 += 1
'''
응용 예제
1부터 100 사이의 모든 정수를 한 줄에 10개씩 출력하는 프로그램을 작성하시오.

실행 예

1  2  3  3  4  5  6  7  8  9 10
11  12  13  13  14  15  16  17  18  19 20
21  22  23  23  24  25  26  27  28  29 30
31  32  33  33  34  35  36  37  38  39 40
41  42  43  43  44  45  46  47  48  49 50
51  52  53  53  54  55  56  57  58  59 60
61  62  63  63  64  65  66  67  68  69 70
71  72  73  73  74  75  76  77  78  79 80
81  82  83  83  84  85  86  87  88  89 90
91  92  93  93  94  95  96  97  98  99 100
'''
# n = 1
# while n < 101:
#     print(n, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9)
#     n += 10

# n = 0
# while n < 100:
#   print(f"{n+1} {n+2}  {n+3}  {n+3}  {n+4}  {n+5}  {n+6}  {n+7}  {n+8}  {n+9} {n+10}")
#   n += 10
'''
p 116

for 문 : 값의 범위나 횟수가 정해져있을 때 사용하면 편리한 반복문 -> while문의 경우 범위나 횟수를 모를 때 사용 가능
    어떤 때에 for / while문을 쓸지 고민을 할 필요가 있음.
    
형식 :
for 변수 in 반복가능객체:
    반복실행문
    
* 반복가능객체(iterable) : 반복해서 사용할 수 있는 객체. 객체 내부에 요소가 여러 개 저장되어 있고 한 번에 하나씩
    꺼내어 사용할 수 있는 객체를 의미함. str, list, tuple, set, dict 등이 해당되며 추후 수업 예정
    
p 119

for문과 문자열
for 문자(변수명-처음 선언) in 문자열:
    반복실행문
'''
str_example = "Hello"
# for letter in str_example:
#     print(letter)

# print(str_example[0])
# print(str_example[1])
# print(str_example[2])
# print(str_example[3])
# print(str_example[4])

# for letter in "nice":
#     print(letter)

'''
p 123

for문과 range() 함수

range() 함수는 정수 범위를 만들어 낼 때 사용하는 함수, 특히 for문과 range() 함수를 사용하면 개발자가 원하는
범위의 값을 쉽게 생성 가능

형식 :
range(초깃값, 종료값, 증감값)

1. 초깃값부터 종료값 '이전'까지의 숫자(n)들의 컬렉션을 만듭니다.
    (초깃값 <= n < 종료값)
2. 초깃값을 생략하면 0부터 시작
3. 종료값은 생략 불가능
4. 증감값을 생략하면 1씩 증가
'''

# 0부터 5까지 출력 -> 종료값만 설정
# for i in range(6):
#     print(i)

# 1부터 5까지 출력 -> 초깃값, 종료값 설정
# for i in range(1, 6):
#     print(i)

# 1, 3, 5를 출력 -> 초깃값, 종료값, 증감값 설정
# for i in range(1, 6, 2):
#     print(i)

# 0부터 시작해서 6 미만으로 하는데, 증감값을 2로 설정하고 싶다면
# for i in range(0, 6, 2):
#     print(i)

'''
기본 예제

출력하고자 하는 구구단을 입력 받아 해당 구구단을 출력하는 프로그램을 작성하시오.

실행 예
출력할 구구단을 입력하세요 >>> 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
'''
# dan = int(input("출력할 구구단을 입력하세요 >>> "))
# # for문을 사용하고 초깃값, 종료값, 증감값을 고려하여 작성할 것.
#
# for i in range(1, 10):       # 초깃값을 1로, 종료값을 10 미만으로 설정
#     print(f"{dan} x {i} = {dan*i}")

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
'''


'''
다음 시간 수업 예정 :
str에서의 인덱싱 / 마이너스인덱싱

p 36
'''









