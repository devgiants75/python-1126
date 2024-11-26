'''
python_lesson_09_functions -> main.py

Functions

1. 함수(Function) : 특정 작업을 수행하는 코드 블럭을 정의하는 방법

예를 들어 '사진을 찍는다'라는 행위에 대해 생각해보면,
1) 주머니에서 폰을 꺼내고,
2) 잠금 화면을 풀고,
3) 카메라를 켜고,
4) 사진을 찍고자 하는 대상에 폰을 조준하고,
5) 셔터를 누릅니다.

컴퓨터는 시키는대로만 하기 때문에 사진을 찍기 위해서는 1) - 5)까지의 명령어를 입력해줘야만 합니다.
하지만 '사진을 찍는다'라는 함수 내에 1) - 5)의 명령어들을 미리 입력하고 나서, '사진을 찍는다'라는 명령어를
실행시키기만 하면 1) - 5)까지의 명령을 순서대로 수행하는 것을 함수의 개념이라고 볼 수 있겠습니다.

주요 수업 예시로는 reeborg's world에서 turn_right()를 정의하는 방법이었습니다.

함수 정의
def turn_right():
    turn_left()
    turn_left()
    turn_left()
함수 호출
turn_right()

2. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드
    3) 사용자 함수

3. 함수 용어 정리 p185
    1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def를 생각하셔야 합니다. cf. def -> define)
    2) 인수(argument) : 사용자 함수에 전달할 입력(input)을 의미
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값(return) : 사용자 함수의 출력(output)을 의미
    5) 함수 호출(call) : 만들어진 함수를 실제로 사용하는 것을 의미

4. (사용자) 함수의 형식 :
def 함수_이름(매개변수):
    실행문

변수 = 함수_이름(인수)
'''
# 함수 정의
# def write_name(name):
#     print(f"당신의 이름은 {name}입니다.")
# #함수 호출
# write_name("안근수")

# def write_name_age(name, age):
#     print(f"당신의 이름은 {name}이고, 나이는 {age}살입니다.")
# #함수 호출
# write_name_age(name="안근수", age=37)  # keyword argument -> 키워드 인자
# write_name_age(age=40, name="안근순")

'''
우리가 예를 들어 input("이름을 입력하세요 >>> ")을 이용해서 이것을 name이라는 변수에 담았다고 가정하면,
name = input("이름을 입력하세요 >>> ")로 작성하게 됩니다. 즉, 저희는 여태까지 함수의 결과값을 
변수에 담아오고 있었습니다.
즉, 파이썬 내장 함수는 이미 함수가 정의되어 있고, 함수 호출만 잘 사용하시면 됩니다.
사용자 함수는 자신이 함수를 만들어 내서 정의하는 것부터 시작, 그 후에 호출한다고 생각할 수 있습니다. 

2. 메서드(method) : 특정 객체가 가지고 있는 함수를 의미. 특정 데이터 자료형에 포함돼있는 함수.
사실은 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있습니다.
함수는 독립적으로 사용할 수 있지만, 메서든느 특정 객체를 통해서만 호출할 수 있습니다.
즉, print(), input() 등은 함수
'''
# eng_name = input("당신의 이름을 소문자로 입력하세요 >>> ").upper()  #.upper()는 메서드 -> str에 종속
# print(eng_name)
'''
객체이름.메서드명() -> 객체의 자료형이 중요합니다
'''
# li = [1, 2, 3]
# print(li)   # 함수 호출
# li.append(4)    # 메서드 호출
# print(li)   # 함수 호출
# eng_name2 = input("당신의 이름을 소문자로 입력하세요 >>> ").title()
# print(eng_name2)
'''
3. 사용자(정의) 함수
'''
# 함수 정의
# def greet():            # parameter는 필수사항이 아님
#     print("안녕")
#     print("오늘 날씨 어때?")
#     print("뭐해?")

# 함수 호출
# greet()                 # argument가 없음 -> 함수를 정의할 때 parameter를 설정하기 않았기 때문

# 함수 정의(파라미터포함)
# def greet_with_name(name):
#     print(f"안녕, {name}")
#     print(f"오늘 날씨 어때?, {name}")
#     print(f"뭐해?, {name}")

# 함수 호출(argument 포함)
# greet_with_name(name="안근수")
# name = input("당신의 이름을 입력하세요 >>> ")
# greet_with_name(name)   # input함수의 결과값이 greet_with_name의 argument가 되는 함수형 프로그래밍

# 함수 정의(복수의 파라미터)
# def greet_with(name, location, weather):
#     print(f"안녕, {name}")
#     print(f"{location} 날씨는 어때?")
#     print(f"{location}의 날씨는 {weather}(이)야.")
#
# name = input("당신의 이름을 입력하세요 >>> ")
# city = input("당신의 주소지를 시만 입력하세요 >>> ")
#
# greet_with(name=name, location=city, weather="맑음")  #keyword argument로 작성 -> 해외의 매너

# 함수 정의 -> parameter 2 개
# def add(num1, num2):
#     return num1 + num2
# 함수 호출 -> argument 2 개
# number1 = int(input("첫 번째 숫자를 입력하세요 >>> "))
# number2 = int(input("두 번째 숫자를 입력하세요 >>> "))
# add(num1=number1, num2=number2) #keyword argument 적용하여 함수 호출

# 변수에 담아준다
# sum1 = add(num1=number1, num2=number2)
# print(f"두 숫자의 합은 {sum1}입니다.")

'''
700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 
그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현하세요.

함수 정의
- 반환값 : 없음
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vending_machine():
    #함수 구현
    
vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''
# def vending_machine(money):      #매개변수 정수 money를 집어넣으라고 했으니까 소괄호 내에 money위치
    # pass    # 함수 입력 안하더라도 오류가 나지 않는 명령어 pass
    # for i in range((money//700) + 1):   # 음료의 가격이 700이기 때문에 700으로 나누지만, range()함수는 int를 argument로 요구하기 때문에
                                        # // 연산자를 사용해야 함. 그리고 실행 예를 확인했을 때 반복문이 5번 돌아가는데, 3000 // 7 = 4 이기
                                        # 때문에 range( (money//700) + 1)으로 작성해야 함.
#         print(f"음료수 = {i}개, 잔돈 = {money - (700*i)}원")
#
# vending_machine(3000)
#
# def vending_machine2(money):
#     price = 700
#     max_drinks = money // price
#     for i in range(max_drinks + 1):
#         drinks = i
#         charge = money - (drinks * price)
#         print(f"음료수 = {drinks}개, 잔돈 = {charge}원")

# print()
# vending_machine2(3000)

'''
예제 : 짝수와 홀수의 개수 세기
문제 : list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의 :
함수 이름 : conut_even_odd
매개변수 : list numbers(요소는 모두 정수일 것)

함수 실행
count_even_odd([1,2,3,4,5,6,7,8,9,10])

실행 예

짝수의 개수 : 5개
홀수의 개수 : 5개
'''
# 함수 정의
def count_even_odd(numbers):
    # pass
    even_count = 0                      #  지역 변수
    odd_count = 0

    # list 내부의 요소가 짝수인지 홀수인지 구분해야 함. -> 반복문을 통해서
    for num in numbers:         # collections의 변수명은 보통 복수형 -> 그 내부의 반복문 돌릴 때 단수형
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # pirnt() 함수는 반복문을 탈출해서 작성해야 함.
    print(f"짝수의 개수 {even_count}개\n홀수의 개수 : {odd_count}개")

count_even_odd([1,2,3,4,5,6,7,8,9,10])

'''
예제 : 구구단 출력하기

함수 정의 :
함수 이름 : multiply
매개변수 : 정수 n

함수 실행
multiply(dan)
실행 예
몇 단을 출력하시겠습니까? >>> 3
3 x 1 = 3
3 x 2 = 6
.
.
.
3 x 9 = 27
'''
# def multiply(n):
#     for i in range(1, 10):
#         print(f"{n} x {i} = {n*i}")
#
# dan = int(input("몇 단을 출력하시겠습니까? >>> "))     # multiply(dan)으로 실행하라고 조건이 주어졌기 때문에 main단계에서 dan을 받아와야 함.
# multiply(dan)




