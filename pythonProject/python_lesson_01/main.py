'''
python_lesson_01 패키지 만들고
python_lesson_01 우클릭 -> New -> python file -> main.py
'''
# print("Hello Python!")
# print("안근수")
# print(37)               # 숫자의 경우는 ""를 사용하지 않아도 됨.

# 주석(comment) : 컴퓨터가 처리하지 않고 사람들이 읽어서 해당 코드에 대한 정보를 습득할 수 있도록 하는 기능

# 샵을 입력하면 그 뒷부분은 전부 주석 처리가 됨.
# 미리 작성한 후에 해당 부분을 주석 처리하고 싶다면 ctrl + /를 누르면 됨.

# : 한 줄 주석 처리
'''
이 사이에 작성하게 되면 여러 줄이 주석 처리가 됩니다.


'''
# print("안근수")
# print('안근수')
"""
마찬가지로 다중 주석이 됩니다. -> Docstring이라는 개념 -> 추후 수업 예정
"""
'''
변수(variable) : 어떤 데이터를 저장하고자 할 때 사용하는 메모리 저장소
등호(=) 왼쪽에 변수 이름 작성, 등호 오른쪽에 저장할 값을 작성합니다.
ex) 예를 들어 점수가 100점 이라는 것을 표현하고 싶다면
'''
# score = 100
'''
와 같은 방식으로 저장된 값을 언제나 불러낼 수 있습니다.
'''
# print(100)
# print(score)
#
# name = "안근수"
# print(name)
'''
name, age, address, major라는 변수에 여러분들의 이름, 나이, 주소, 전공을 대입하여
print(name) 
print(age) 
print(address) 
print(major)
를 입력하여 콘솔창에 해당 정보들을 뜰 수 있도록 작성하시오. 
'''
# name = "안근수"
# age = "37"
# address = "부산광역시 연제구"
# major = "영어교육과"
# mbti = "ESTJ"
#
# print(name)
# print(age)
# print(address)
# print(major)
#
# print(name + "\n" + age + "\n" + address + "\n" + major)

introduction = '''
이름 : 안근수
나이 : 37
주소 : 부산광역시 연제구
MBTI : ESTJ
'''
# print(introduction)
# score = 100
# print(score)
# score = 90
# print(score)

print("안녕하세요." +" 제 이름은 안근수입니다.")
# print("그리고 제 나이는 " + 37 + "살입니다.")        # 오류 발생 -> 서로 다른 자료형을 동시에 print할 수 없음
'''
이상과 같은 오류를 파이썬 상에서 해결하기 위해 나온 출력 방식 : f-string(formatted string)이라고 하고,
한국에서는 그냥 에프스트링이라고 표현하는 편

형식 :
f"쓸 내용 {변수명}과 같은 방식으로 사용합니다."
'''
# age = 37
# print(f"제 나이는 {age}살입니다.")          #f-string 사용 예시
# name = "안근수"
# age = 37
# address = "부산광역시 연제구"
# major = "영어 교육과"
# mbti = "ESTJ"
# job = "코리아it아카데미 파이썬 강사"

'''
위의 변수에 적당한 데이터를 입력하고,
콘솔 창에
안녕하세요, 제 이름은 안근수이고, 나이는 37살입니다. 저는 영어교육과고, 부산광역시 연제구에 삽니다.
제 mbti는 ESTJ이며, 직업은 코리아it아카데미 파이썬 강사입니다.
와 같은 방식으로 출력할 수 있게끔 f-string을 이용하시오.
'''
# print(f"안녕하세요, 제 이름은 {name}이고, 나이는 {age}살입니다. 저는 {major}고, {address}에 삽니다.")
# print(f"제 mbti는 {mbti}이며, 직업은 {job}입니다.")

# print(f"안녕하세요, 제 이름은 {name}이고, 나이는 {age}살입니다. 저는 {major}고, {address}에 삽니다.\n제 mbti는 {mbti}이며, 직업은 {job}입니다.")
# print("안녕하세요 제 이름은 " + name + f"이고, 나이는 {age}살입니다. 저는 " + major + "고,")
'''
input() 함수 -> () 내에 있는 내용을 콘솔창에 띄우고, 입력받을 수 있도록 하는 함수
'''
# input("당신의 이름은 무엇입니까? >>> ")
'''
함수의 결과값을 변수에 대입할 수 있음.
'''
# name = input("당신의 이름은 무엇입니까? >>> ")
'''
input 함수의 결과값은 문자열로 나오게 되며 이를 name이라는 변수에 대입하는 과정을 거침
'''
# print(name)
'''
이후 print(name)을 하게 되면 '당신의 이름은 무엇입니까? >>> '가 뜨게 되는 게 아니라,
콘솔창에 입력한 내용이 출력됨.

함수의 결과값을 변수에 담을 수 있다.
  ex) name = input("당신의 이름을 입력하세요 >>> ")를 실행시켜서 콘솔창에 '안근수'라고 입력했다면,
  1) input("당신의 이름을 입력하세요 >>> ") = "안근수"라는 문자열로 변환된다.
  2) name = "안근수"
  3) name에 "안근수"라는 문자열이 저장된다(데이터를 변수에 저장)
  4) 이후 print(name)을 실행시키면 콘솔에 안근수 가 출력됨을 확인할 수 있음.
  
지시 사항
input() 함수를 이용해서 이름, 나이, 주소, 직업을 입력받고, print() 함수를 이용하여 출력하시오.
실행 예시
이름이 무엇입니까? >>> 안근수
몇 살입니까? >>> 37
어디에 삽니까? >>> 부산광역시 연제구
직업이 무엇입니까? >>> 코리아it아카데미 파이썬 강사
'''
# name = input("이름이 무엇입니까? >>> ")
# age = input("몇 살입니까? >>> ")
# address = input("어디에 삽니까? >>> ")
# job = input("직업이 무엇입니까? >>> ")
'''
안근수
37
부산광역시 연제구
코리아it아카데미 파이썬 강사
'''
# print(name)
# print(age)
# print(address)
# print(job)
'''
지시 사항
1. 지금 입고 있는 하의 색깔을 '입력 받고' pants_color라는 변수에 대입하시오.
2. 마지막으로 먹은 음식을 입력 받고 last_food라는 변수에 대입하시오.
3. f-string을 이용하여 "당신의 밴드 이름은 블랙 스테이크덮밥입니다."와 같은 방식으로 출력하시오.
'''
logo = '''
d8888b.  .d8b.  d8b   db d8888b. d8b   db  .d8b.  .88b  d88. d88888b 
88  `8D d8' `8b 888o  88 88  `8D 888o  88 d8' `8b 88'YbdP`88 88'     
88oooY' 88ooo88 88V8o 88 88   88 88V8o 88 88ooo88 88  88  88 88ooooo 
88~~~b. 88~~~88 88 V8o88 88   88 88 V8o88 88~~~88 88  88  88 88~~~~~ 
88   8D 88   88 88  V888 88  .8D 88  V888 88   88 88  88  88 88.     
Y8888P' YP   YP VP   V8P Y8888D' VP   V8P YP   YP YP  YP  YP Y88888P 
'''
# print(logo)
# pants_color = input("지금 입고 있는 하의 색깔은 무엇입니까? >>> ")
# last_food = input("마지막으로 먹은 음식은 무엇입니까? >>> ")
# band_name = pants_color + last_food # pants_color의 데이터와 last_food의 데이터를 합쳐 band_name 변수에 대입
# # 155라인에 작성한 방식대로하면 띄어쓰기가 적용되지 않음
# band_name = pants_color + " " + last_food
# # print(f"당신의 밴드 이름은 {pants_color} {last_food}입니다. ")
# print(f"당신의 밴드 이름은 {band_name}입니다. ")

