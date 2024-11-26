'''
python_lesson_03 패키지 생성 -> main.py

조건문 if -> 특정 조건을 만족했을 때만 이하의 코드가 실행됨.
elif -> 위의 if 문의 조건을 충족시키지 못했으나 elif에 해당되는 조건을 만족시켰을 때 이하의 코드가 실행됨.
else -> if / elif의 조건들을 충족시키지 못했을 때 이하의 코드가 실행됨

형식 :

if 조건문1:
    실행문1
elif 조건문2:
    실행문2
else:
    실행문3

조건문 -> True / False으로 결정이 날 수 있는 것만 사용 가능
'''
# 조건문 if - elif - else 세트
# if 3 > 0:                           # True
#     print("3은 0보다 큽니다.")
# elif 3 > 1:                         # True
#     print("3은 1보다 큽니다.")
# else:
#     print("3은 0과 1보다 작나 봅니다.")
# if 3 > 0:                           # True / 조건문 1번 세트
#     print("3은 0보다 큽니다.")
# if 3 > 1:                         # True    / 조건문 2번 세트 시작
#     print("3은 1보다 큽니다.")
# else:
#     print("3은 0과 1보다 작나 봅니다.")
'''
나이를 입력 받고,
나이가 10살 이하라면, "당신은 아기입니다."를 출력하세요.
나이가 19살 이하라면, "당신은 중등교육과정에 해당합니다."를 출력하세요.
나이가 35살 이하라면, "당신은 청년입니다."를 출력하세요.
나이가 65살 이하라면, "당신은 경제활동인구입니다."를 출력하세요.
나이가 65살 초과라면, "당신은 노년입니다."를 출력하는 프로그램을 작성하시오.
'''
# age = int(input("당신의 나이를 입력하세요. >>> "))
#
# if age < 11:
#     print("당신은 아기입니다.")
# elif 11 <= age < 20:                        # 이렇게 작성할 경우 잉여적이다 -> if 문이 실행되지 않았다는 것은
#     print("당신은 중등교육과정에 해당합니다.")   # age >= 11이라는 의미이기 때문
# elif age < 36:
#     print("당신은 청년입니다.")
# elif age < 66:
#     print("당신은 경제활동인구입니다.")
# else:
#     print("당신은 노년입니다.")
'''
점수를 입력 받아서 학점을 출력하는 프로그램을 구현하세요. 학점은, 점수가 100 ~ 90이면 "A",
89 ~ 80이면 "B", 79 ~ 70이면 "C", 69 ~ 60이면 "D", 59 ~ 0이면 "F"에 해당합니다.

실행 예

점수를 입력하세요 >>> 95
점수는 95점이고, 학점은 A학점입니다.

점수를 입력하세요 >>> 150
잘못된 점수를 입력하셨습니다.

점수를 입력하세요 >>> -30
잘못된 점수를 입력하셨습니다.
'''
# score = int(input("점수를 입력하세요 >>> "))

# 변수가 한 개인 풀이
# if score > 89:
#     print(f"당신의 점수는 {score}점이고, 학점은 A학점입니다.")
# elif score > 79:
#     print(f"당신의 점수는 {score}점이고, 학점은 B학점입니다.")
# elif score > 69:
#     print(f"당신의 점수는 {score}점이고, 학점은 C학점입니다.")
# elif score > 59:
#     print(f"당신의 점수는 {score}점이고, 학점은 D학점입니다.")
# elif score > 0:
#     print(f"당신의 점수는 {score}점이고, 학점은 F학점입니다.")
# elif score < 0:
#     print("잘못된 점수를 입력하셨습니다.")
# elif score > 101:
#     print("잘못된 점수를 입력하셨습니다.")

# 1. 점수가 0 ~ 100인지를 확인하는 조건문
# if (score < 0) or (score > 100):
#     print("잘못된 점수를 입력하셨습니다.")
# # 이상의 if문을 통과했다면 score > 0 and score < 101이기 때문에 점수 환산이 가능
# elif score > 89:
#     print(f"당신의 점수는 {score}점이고, 학점은 A학점입니다.")
# elif score > 79:
#     print(f"당신의 점수는 {score}점이고, 학점은 B학점입니다.")
# elif score > 69:
#     print(f"당신의 점수는 {score}점이고, 학점은 C학점입니다.")
# elif score > 59:
#     print(f"당신의 점수는 {score}점이고, 학점은 D학점입니다.")
# else:
#     print(f"당신의 점수는 {score}점이고, 학점은 F학점입니다.")

# 변수가 2 개인 풀이
# if (score < 0) or (score > 100):
#     print("잘못된 점수를 입력하셨습니다.")
#     grade = ""      # ""는 빈값을 의미
# elif score > 89:
#     grade = "A"
# elif score > 79:
#     grade = "B"
# elif score > 69:
#     grade = "C"
# elif score > 59:
#     grade = "D"
# else:
#     grade = "F"
#
# print(f"당신의 점수는 {score}점이고, 학점은 {grade}학점입니다.")
# 이 부분을 지시 사항대로 풀이하기 위해서는 파이썬2 과목에서의 예외처리 개념을 익혀야 함. -> 추후 수업 예정

# print("롤러 코스터에 오신 것을 환영합니다.")
# height = float(input("당신의 키는 몇 cm인가요? >>> "))
# age = int(input("당신의 나이는 몇 살인가요? >>> "))

# 키와 나이를 둘 다 만족시키는 조건문의 작성 -> 중첩 if문(multiple if sentence)의 사용
# if height >= 120:
#     if age > 7:
#         print("당신은 롤러코스터에 탑승할 수 있습니다.")
#     else:                                       # 나이가 7 이하인 경우에 실행됨
#         print(f"당신은 롤러코스터에 탑승할 수 없습니다. {8-age}년 후에 다시 오세요.")
# else:                                           # 키가 120cm 미만인 경우에 실행됨
#     print(f"당신은 롤러코스터에 탑승할 수 없습니다. {120-height}cm 더 크고 오세요.")

# 축약한 버전
# if (height >= 120) and (age > 7):       # and 연산자 : and의 왼쪽 조건식과 오른쪽 조건식이 모두 True여야지만
#                                         # 이하의 실행문이 실행됨. C와 Java에서는 &&로 작성
#     print("당신은 롤러코스터에 탑승할 수 있습니다.")
# else:                                   # 키가 120 미만에 해당, 나이가 7세 이하에 해당
#     print("당신은 롤러코스터에 탑승할 수 없습니다.")

'''
bmi 계산기 업그레이드 버전을 작성하시오

옆의 bmi 지수에 맞게 조건문을 포함하여 bmi지수에 따라
저체중 / 정상 / 과체중 / 비만을 출력할 수 있도록 작성하시오.

실행 예

키를 입력하세요(cm) >>> 172
몸무게를 입력하세요(kg) >>> 68

당신의 bmi 지수는 22.00이고, 정상 체중입니다.
'''
# height = float(input("키를 입력하세요(cm) >>> ")) * 0.01
# print(height)     # 1.xx / 2.xx로 나오는지 확인하기 위한 test code
# weight = float(input("몸무게를 입력하세요(kg) >>> "))
# bmi 지수 계산 = 몸무게(kg) / (키(m)의 제곱)
# bmi = round((weight/height**2), 2)
# print(bmi)        # bmi 지수가 제대로 출력되는지 확인하기 위한 test code

# if bmi < 18.5:
#     grade = "저체중"
# elif bmi < 23:
#     grade = "정상 체중"
# elif bmi < 25:
#     grade = "과체중"
# else:
#     grade = "비만"
#
# print(f"당신의 bmi 지수는 {bmi}이고, {grade}입니다.")

'''
간단한 계산기 프로그램

두 개의 숫자와 하나의 연산자를 입력 받아, 간단한 사칙 연산을 수행하는 계산기 프로그램을 작성합니다.
사용자가 입력한 연산자에 따라 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하고, 그 겨로가물을 출력하세요.
만약 사용자가 0으로 나누기를 시도할 경우, "0으로 나눌 수 없습니다."라는 메시지를 출력하세요.

지시 사항

1. 사용자는 첫번째 숫자와, 두번째 숫자를 입력해야 합니다.
2. 사용자는 연산자로 +, -, *, / 중 하나를 입력해야 합니다.
3. 나눗셈을 수행할 때, 두번째 숫자가 0이면 "0으로 나눌 수 없습니다."라는 메시지를 출력하세요.
4. 입력된 연산자가 잘못된 경우, "잘못된 연산입니다, +, - , *, / 중에서 선택하세요."라는 메시지를 출력합니다. 
'''
# num1 = float(input("첫번째 숫자를 입력하세요 >>> "))
#
# operator = input("부호를 입력하세요 (+, -, *, /) >>> ")         # 이 부분의 결과값은 무조건 문자열이기 때문-> 198번째 라인과 연관
#
# num2 = float(input("두번째 숫자를 입력하세요 >>> "))
#
# # = 와 ==의 차이 / = : 대입 연산자 / == : == 왼쪽과 오른쪽이 같다는 의미
# if operator == "+":
#     print(f"결과 : {num1} + {num2} = {num1+num2}")
# elif operator == "-":
#     print(f"결과 : {num1} - {num2} = {num1-num2}")
# elif operator == "*":
#     print(f"결과 : {num1} * {num2} = {num1*num2}")
# elif operator == "/":                               # num2 = 0인 경우 연산을 하지 않아야 함. -> 중첩 if문 작성
#     if num2 == 0:
#         print("0으로 나눌 수 없습니다.")
#     else:                                           # num2 != 0이라는 의미(! -> not)
#         print(f"결과 : {num1} / {num2} = {num1/num2}")
# else:                                               # +, -, *, /가 아닌 문자열이 들어왔을 때
#     print("잘못된 연산자입니다. +, -, *, / 중에서 선택하세요.")

# operator2가 "/"이고, num4 = 0인 경우, 0으로 나눌 수 없습니다를 출력하는 if문 작성
# 해당되지 않는다면 정상적인 연산 결과가 나올 수 있도록 작성

num3 = float(input("첫번째 숫자를 입력하세요 >>> "))

operator2 = input("부호를 입력하세요 (+, -, *, /) >>> ")
# 이하에 operator2가 +, -, * /에 해당되지 않는다면 잘못된 연산입니다를 출력하는 if문 작성
# if operator2 == "+" or operator2 == "-" or operator2 == "*" or operator2 == "/":
    # operator2가 +, -, *, /에 해당한다면
# if not operator2 == "+" or operator2 == "-" or operator2 == "*" or operator2 == "/":
    # operator2가 +, -, *, /에 해당하지 않는다면
# operator2 ==을 반복하지 않는 방법
if operator2 not in ("+", "-", "*", "/"):   #in - ~ 안에서 / not in (내용) : 내용에 해당하는 것이 없다면
    print("잘못된 연산자입니다. +, -, *, / 중에서 선택하세요.")
else:
    num4 = float(input("두번째 숫자를 입력하세요 >>> "))
    if operator2 == "+":
        print(f"결과 : {num3} + {num4} = {num3+num4}")
    elif operator2 == "-":
        print(f"결과 : {num3} - {num4} = {num3-num4}")
    elif operator2 == "*":
        print(f"결과 : {num3} * {num4} = {num3*num4}")
    elif operator2 == "/":                               # num2 = 0인 경우 연산을 하지 않아야 함. -> 중첩 if문 작성
        if num4 == 0:
            print("0으로 나눌 수 없습니다.")
        else:                                           # num2 != 0이라는 의미(! -> not)
            print(f"결과 : {num3} / {num4} = {num3/num4}")










