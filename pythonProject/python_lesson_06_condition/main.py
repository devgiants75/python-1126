'''
python_lesson_06_condition -> main.py

1. 윤년 계산기(leap year)

주어진 해가 윤년 인지 아닌지를 계산하는 프로그램을 작성하시오. 일반적으로 1년은 365일이고,
윤년은 366일로 2월에 하루가 더 있습니다.

다음은 특정 년도가 윤년인지 확인하는 방법입니다.

1. 4로 나누어 떨어지는 해는 윤년입니다.
2. 그러나, 100으로 나누어 떨어지는 해는 윤년이 아닙니다.
3. 그런데, 400으로 나누어 떨어지는 해는 윤년입니다.

ex)

2000 / 4 = 500(윤년)
2000 / 100 = 20(윤년 아님)
2000 / 400 = 5(윤년)

따라서 2000년은 윤년입니다.

2100 / 4 = 525(윤년)
2100 / 100 = 21(윤년 아님)
2100 / 400 = 5.25(윤년 아님)

따라서 2100년은 윤년이 아닙니다.
'''
# year = int(input("년도를 입력하세요 >>> "))
# if year % 100 != 0:                         # ! -> not의 의미
# 이렇게 쓰면 오류납니다 -> 왜 그런지 생각해보세요
# 수정한 버전 -> 중첩 if문을 사용하지 않은 풀이
# if year % 400 == 0:
#     print("윤년입니다.")
# elif year % 100 == 0:
#     print("윤년이 아닙니다.")
# elif year % 4 == 0:
#     print("윤년입니다.")
# else:
#     print("윤년이 아닙니다.")

# 중첩 if문을 사용하지 않은 사례 -> elif도 사용하지 않은 사례
# if (year % 100 != 0 and year % 4 == 0) and (year % 4 == 0):
#     print(f"{year}년은 윤년입니다.")
# else:
#     print(f"{year}년은 윤년이 아닙니다.")

# 중첩 if문을 사용한 사례 -> 400과 100으로 나뉘어지는 것은 4로도 나누어지기 때문에 사용할 수 있는 방식
# if year % 4 == 0:
#     if year % 400 == 0:
#         print(f"{year}년은 윤년입니다.")
#     elif year % 100 == 0:
#         print(f"{year}년은 윤년이 아닙니다.")
#     else:
#         print(f"{year}년은 윤년입니다.") # 4로는 나누어지지만 100과 400으로 나누어지지 않는 년도를 처리하기 위함
# else:
#     print(f"{year}년은 윤년이 아닙니다.")
'''
fizzbuzz 게임

1. 프로그램은 1부터 100까지의 숫자를 차례대로 출력합니다.
2. 숫자가 3으로 나누어 떨어지면 숫자 대신 "Fizz"를 출력합니다.
3. 숫자가 5로 나누어 떨어지면 숫자 대신 "Buzz"를 출력합니다.
4. 숫자가 3과 5 둘 다로 나누어 떨어지면 숫자 대신 "FizzBuzz"를 출력합니다.

1
2
Fizz        3 대신
4
Buzz        5 대신
...
Fizz        12 대신
13
14
FizzBuzz    15 대신
'''
# 1부터 100까지 출력하기 위한 for문
# for i in range(1, 101):
#     # 내부에 if문을 작성해서 지시 사항을 만족시키세요
#     if i % 3 ==0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

# 1부터 100까지 출력하기 위한 while문
# i = 1
# while i < 101:
#     if i % 3 ==0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)
#     i += 1
'''
응용 문제

마지막 숫자를 입력 받아서 그 숫자까지 출력하면서 FizzBuzz 게임을 할 수 있도록 프로그램을 작성하세요.
'''
last_num = int(input("마지막 번호를 입력하세요 >>> "))

# while 문으로 작성
i = 1
while i <= last_num:
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i += 1

# for문으로 작성
for i in range(last_num + 1):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)





