'''
python_lesson_07_collections -> main.py

p 39

컬렉션(Collection) : 여러 값을 하나의 이름으로 묶어서 관리하는 자료형

string의 경우 문자 하나 하나를 줄(string)로 묶어서 문자열로 출력 하는데, 예를 들어
'다수의 다른 string을 관리하는 방법은 무엇일까?'에 관한 대답

여러 명의 프로필을 관리한다고 가정했을 때,
'''
# ahn_geunsu = "이름 : 안근수\n나이 : 37\n직업 : 파이썬 강사"
# print(ahn_geunsu)
# kim_donggyu = "이름 : 김동규\n나이 : 미상\n직업 : 학생"
# print(kim_donggyu)
'''
한 명 저장 하는데에는 문제가 없을 수 있지만 매번 변수 하나에 이름, 나이, 직업 등을 한 명 추가할 때마다
정리하는 것은 비효율적이고, 예를 들어 ahn_geunsu에서 직업만 조회하고 싶어도 전체 정보를 다 확인해야만 합니다.
이를 한꺼번에 관리하기 위한 방식으로 모음(Collection)을 사용합니다.

종류
    1. list()리스트 - 추가, 수정, 삭제가 언제나 가능 / a = [1, 2, 3] # 대괄호 사용
    2. tuple()튜플 - 추가, 수정, 삭제가 불가능 / a = (1, 2, 3) # 소괄호 사용
    3. set()세트 - 중복된 값의 저장이 불가능 / a = {1, 2, 3} # 중괄호 사용
    4. dict()딕트 - 키 + 값으로 관리 / a = {"name": "안근수", "age": 37} # 중괄호 사용
    
이 중 1, 2번인 list와 tuple은 저장된 값의 순서가 있으며 이를 시퀀스(Sequence)라고 부릅니다.
즉, list는 저장 순서가 있고, 추가/수정/삭제가 자유로우며, tuple의 경우 저장된 순서가 있으나 추가/수정/삭제가 불가능합니다.

1. list
    여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능
    하나의 배열(파이썬 리스트와 비슷한 개념의 자료 구조)에 동일한 자료형만을 저장할 수 있는 C와 Java에 비해 python이 가지는
    장점이라고 할 수 있음.
'''
# li = [4, 5, 6]
# print(li)
'''
    1-1. list의 index와 slice/리스트의 인덱스와 슬라이스
        list는 str과 동일한 방식의 index와 slice를 지원함.
        1) 인덱스 및 마이너스 인덱스
'''
# print(li[0])
# print(li[1])
# print(li[2])
# print(li[-1])
# print(li[-2])
# print(li[-3])
'''
        2) slice
        str의 슬라이싱과 같이 '시작점:종료점:증감값'으로 이루어져 있음
'''
# list_num1 = [100, 3.14, "hello"]        # list 생성 방법 1
# list_num2 = list([4, 5, 6, 7, 8, 9])    # list 생성 방법 2
# print(list_num1)
# print("hello")
# print(list_num2[0:5:2])             # 슬라이싱 -> 시작값 : 처음부터 / 종료값 : 5번지 '앞까지' / 증감값 2씩
'''
        3) list 요소의 추가와 삭제
        
        list에 새로운 요소를 추가할 때는 append()와 insert() '메서드'를 사용할 수 있습니다.
        기존 요소를 삭제할 때는 pop() 메서드를 사용합니다.
        
        .append() - 항상 마지막 인덱스에 요소를 추가하는 메서드
        .insert(위치, 값) - 정해진 위치(인덱스)에 해당 값을 추가하는 메서드
'''
# scores = [30, 40, 50]
# print(scores)
# scores.append(100)          # 함수와 달리 리스트이름.메서드명(데이터)의 형태로 사용함. 함수는 함수명(데이터)로 사용
# print(scores)
#
# scores.insert(0, 90)    # scores라는 list의 0번지(인덱스0)에 90이라는 데이터를 추가하겠다는 의미
# print(scores)
'''
        .pop()의 경우 빈 괄호로 사용하게 되면 맨 마지막 요소가 삭제됨.
        .pop(인덱스)로 작성하면 해당 인덱스의 요소를 삭제함.
'''
# scores.pop()
# print(scores)
# scores.pop(0)
# print(scores)

# 교재에 없는 삭제 메서드 : .remove(값)을 하면 list내의 해당 값을 찾아 삭제함.
# scores.remove(50)
# print(scores)

# list의 요소를 하나씩 뽑아 쓰는 반복문 -> 향상된 for문을 사용한 사례
# for score in scores:
#     print(score)

# 요소를 하나씩 뽑는 반복문 -> 고전 for문을 사용한 사례
# for i in range(len(scores)):                    # len() -> length의 줄임말로 반복가능객체의 크기를 int형태로 산출함.
#     print(scores[i])
#
# print(len(scores))
# print(len("abcd"))
'''
    2. tuple() : 저장된 값을 변경할 수 없는 list라고 생각하면 됩니다. 인덱스와 슬라이스를 사용하지만 저장된 값 이외에는
    추가 / 수정 / 삭제가 불가능.
    
    튜플은 소괄호를 통해 생성함
'''
# tuple_num1 = (1, 2, 3)          # 튜플 생성 방법 1
# tuple_num2 = tuple((4, 5, 6))   # 튜플 생성 방법 2
# tuple_num3 = 7, 8, 9            # 튜플 생성 방법 3
# print(tuple_num1)
# print(tuple_num2)
# print(tuple_num3)
# a, b, c = 7, 8, 9               # 복수의 변수를 동시에 선언하고 초기화하는 방법
# print(a)
# print(b)
# print(c)
'''
        튜플 생성 방법 3을 이용한다고 가정할 때, 값이 하나 뿐인 튜플을 생성한다면
        tuple_num4  = 7이라고 입력할 경우 생기는 문제점은 무엇인가?
'''
# tuple_num4  = 7
# print(tuple_num4)
# print(type(tuple_num4))
#
# tuple_num5 = 7,             # ,를 추가하면 tuple로 인식됨
# print(tuple_num5)
# print(type(tuple_num5))

'''
    튜플에서의 인덱스 / 마이너스 인덱스
'''
# tuple_num6 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(type(tuple_num6))
#
# print(type(tuple_num6[1]))          # 인덱스를 먹이게 되면 각 요소의 자료형이 추출됨
# tuple_num7 = "hello. ", "nice to meet you. ", "I'm Ahn Geunsu. ", "my age is ", 37
# print(type(tuple_num7[0]))
# print(type(tuple_num7[4]))
# print(tuple_num7[-1])
# # 슬라이싱 적용 사례
# print(tuple_num7[:-1:2])        # 시작값 -> 처음부터 / 종료값 -> -1번지 : -1번지 앞에서 끝이남 / 증감값 -> 1로 고정
'''
    3. set : 수학의 집합 개념을 구현한 자료형입니다. list와의 차이점은 순서가 없기 때문에(비시퀀스) 인덱스 및 슬라이싱 사용이 불가능
    중복된 값의 저장이 불가능.
    이를 활용하여 중복 제거용으로 사용하는 경우와, 교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우 사용함.
    
    set을 생성하기 위해서는 중괄호({})를 사용합니다.
'''
# set_num1 = { 1, 2, 3 }      # 세트 생성 방법 1
# set_num2 = set({4, 5, 6})   # 세트 생성 방법 2
# print(set_num1)
# print(set_num2)
#
# li = []
# tu = ()             # 비어있는 튜플은 잘 생성하지 않는다 -> 추가 / 수정 / 삭제가 불가능 하기 때문
# se = {}
#
# print(type(li))
# print(type(tu))
# print(type(se))
'''
        se = {} 형태로 비어있는 set를 만들게 됐을 경우 se는 사실 class dict이기 때문에, 비어있는 set을 만들기 위해서는
        세트 생성 방법 2를 사용해야만 함
'''
# se2 = set({})               # 비어있는 세트를 생성하는 방법 1
# print(type(se2))
# set_empty = set()           # 비어있는 세트를 생성하는 방법 2
# print(type(set_empty))

'''
        비어 있는 set를 생성할 때는 중괄호 사용 불가, s = {}와 같이 작성할 경우 세트 대신 비어있는 딕셔너리가 생성됨.
        그래서 빈 set를 생성할 경우 set() 함수를 사용해야만 함.
        
        2) 특징
            1. 저장되는 순서가 없다 -> 인덱싱 / 슬라이싱 불가능
            2. 중복되는 값을 저장할 수 없다.
            3. 특히 2.의 특징으로 인해 set를 단독으로 쓰이기 보다는 list와 연계하여 많이 사용됨. 
'''
# list_num4 = [ 1, 1, 2, 2, 3, 3, 3 ]
# print(list_num4)
# set_num4 = set(list_num4)           # 형변환 함수인 set()을 사용하고 그 안에 list_num4를 입력해 list를 set으로 형변환
# print(set_num4)                     # 중복이 제거된 것을 확인할 수 있음
# list_num5 = list(set_num4)          # set로 형변환하여 중복을 제거하고, 다시 list() 함수를 활용하여 list로 다시 변환
'''
        set에는 인덱싱 / 마이너스 인덱싱 / 슬라이싱을 지원하지 않기 때문에 특정 요소만 추출하기 위해서는 형변환하는 과정이 필요함
        
        .add() - set에 새로운 요소를 추가할 때
        .remove() - 기존 요소를 삭제할 때
        .discard() - 기존 요소를 삭제할 때
'''
# set_num5 = {10, 20, 30}
# set_num5.add(50)
# print(set_num5)     # 순서가 없기 때문에 출력 결과가 순서대로 나오지 않을 수 있음
# set_num5.remove(50) # 순서가 없기 때문에 '값'을 정확히 입력해야 함
# print(set_num5)
# # set_num5.remove(40)   # .remove()를 사용하면서 정확하지 않은 값을 넣을 경우 오류 발생 -> KeyError 발생 : 예외처리에서 수업예정
# set_num5.discard(40)    # .discard()는 set을 탐색하면서 해당 값이 없어도 오류가 발생하지 않음
# print(set_num5)
'''
    4. 딕셔너리 - 말 그대로 사전의 의미를 생각하시면 됩니다. 종이 사전을 펴보게 되면,
    flower : 꽃
    dictionary : 사전
    등으로 기재돼있습니다. 즉 ':'을 기준으로 좌측과 우측이 나누어진 형태를 지니고 있는데, 딕셔너리는 이전의 리스트, 튜플, 세트와 달리
    key: value의 구성으로 이루어져 있습니다.
'''
# dict_num1 = {
#     "이름":"안근수",
#     "나이":37,
#     "주소":"부산광역시 연제구",
# }
'''
와 같은 방식으로 작성합니다.
'''
# print(dict_num1)
# print(dict_num1["이름"])
'''
    딕셔너리는 인덱스는 존재하지 않지만 위와 같이 key를 인덱스와 비슷하게 사용함.
    즉, 키값(key)을 알면 저장된 값(value)을 확인할 수 있는 구조
'''
# list의 각 요소를 추출하기 위한 반복문
# li2 = [10, 20, 30, 40]
# for num in li2:
#     print(num)
# # dictionary에서 같은 방식의 반복문을 활용하게 되면,
# for key in dict_num1:           # dictionary에서 반복문을 돌리게 되면 각 key가 추출됨.
#     print(key)
#     print(dict_num1[key])       # dictionary에서 반복문을 이용하여 value를 추출하는 방법.
#
# print(dict_num1.keys())         # 딕셔너리.keys() 메서드 -> key 목록을 추출하는 메서드
# print(type(dict_num1.keys()))   # class 'dict_keys'로 출력됨.
# list_keys = list(dict_num1.keys())  # key 목록을 list 형태로 보기 위해 list() 함수를 사용하는 편
# print(list_keys)
# print(dict_num1.values())       # 딕셔너리.values() 메서드 -> value 목록을 추출하는 메서드
# print(type(dict_num1.values())) # class 'dict_values'로 출력됨.
# list_values = list(dict_num1.values())  # value 목록을 list 형태로 보기 위해 list() 함수를 사용하는 편ㅍ
# print(list_values)
# print(list_keys[1])             # 왜 list로 바꾸느냐? -> index를 활용하기 위해
# print(list_values[1])
'''
    4-1. 딕셔너리 요소의 추가와 삭제
'''
# dict_num1["직업"] = "코리아it아카데미 파이썬 강사"    # 기존에 없는 key를 입력하고 = value를 입력하게 되면,
# print(dict_num1)
# # 하나의 key에 서로 다른 value를 저장할 수 없음 -> key 하나당 value 하나
# dict_num1["직업"] = "영어 과외 강사"                # 딕셔너리 내의 특정 key의 value를 수정하는 방법
# print(dict_num1)
# # 삭제 방법
# dict_num1.pop("직업")             # 딕셔너리명.pop(key)를 입력하면 key - value 전체 삭제
# print(dict_num1)

# print("제 이름은 '안근수'입니다.")
# print('제 이름은 "안근수"입니다.')
# print("제 이름은 \"안근수\"입니다.")
'''
응용 예제

어떤 중국 음식점의 이번 주말 할인 메뉴는 금요일은 탕수육, 토요일은 유산슬, 일요일은 팔보채입니다.
요일별 할인 메뉴를 딕셔너리(dict) 구조로 저장하고 다음과 같이 출력하는 프로그램을 구현하세요.

실행 예
금요일 : 탕수육
토요일 : 유산슬
일요일 : 팔보채
'''
# 요일이 key, 할인 메뉴가 value가 되는 dictionary를 작성할 것
# dict_menu = {
#     "금요일":"탕수육",
#     "토요일":"유산슬",
#     "일요일":"팔보채", # 해당 collection의 뒤에 데이터가 추가될 수 있음을 개발자들끼리 표시하기 위해 맨 마지막 요소 뒤에 ','를
#                      # 삽입하는 버릇이 있음
# }
# 반복문 혹은 list로의 변환 등 다양한 방법을 활용하여 key 및 value를 추출하여 위의 실행 예와 같이 콘솔에 출력할 것

# for key in dict_menu:       # 반복문으로 dictionary를 돌리게 되면 key가 출력됨.
#     print(f"{key} : {dict_menu[key]}")


# list로 바꿔서 하나하나 작성하는 방법
# list_keys = list(dict_menu.keys())
# list_values = list(dict_menu.values())
# print(f"{list_keys[0]} : {list_values[0]}")
# print(f"{list_keys[1]} : {list_values[1]}")
# print(f"{list_keys[2]} : {list_values[2]}")
# list로 바꾼 다음 for문을 통해 작성하는 방법
# for i in range(len(list_keys)):         # key의 개수 = value의 개수는 동일하기 때문에 관계 없음
#     print(f"{list_keys[i]} : {list_values[i]}")

'''
리스트 [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소부터 7번째 요소만 추출한 결과, 그리고 그 리스트에서
2번째 요소를 출력하는 프로그램을 구현하세요.

실행 예
3번째 요소로부터 7번째 요소 = [30, 40, 50, 60, 70]
3번째 요소로부터 7번째 요소 중 2번째 요소 = 40
'''
# list_original = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list_extracted = list_original[2:7:]        # 2번지부터 시작해서 7번지 앞까지 추출 / 증감값 1
# print(f"3번째 요소로부터 7번째 요소 = {list_extracted}")
# print(f"3번째 요소로부터 7번째 요소 중 2번째 요소 = {list_extracted[1]}")
'''
사용자로부터 1에서 12사이의 월을 입력 받아, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하시오.

실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일까지 있습니다.
'''
# question = int(input("1 ~ 12 사이의 월을 입력하세요 >>> "))
# 쉬운 버전
# month_list1 = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# print(f"{question}월은 {month_list1[question-1]}일까지 있습니다.")

# 어려운 버전
# month_list2 = [ 28, 30, 31 ]
# 조건문을 필요로 함.
# last_date = "오류"
# if question == 2:
#     last_date = month_list2[0]
# elif question == 4 or question == 6 or question == 9 or question == 11:
#     last_date = month_list2[1]
# elif question in (1, 3, 5, 7, 8, 10, 12):           # not in 예시는 수업했지만 in 예시는 처음이기 때문에 필기해둘 것
#     last_date = month_list2[2]
#
# print(f"{question}월은 {last_date}일까지 있습니다.")
'''
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3 명으로 가정하고 실행 예와 같이 동작하는 프로그램을 구현하세요.

실행 예
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.
'''
# 비어있는 list 생성
# field_trip = []
# 학생 3명에 대한 입력값을 student 변수에 저장
# student1 = input("희망하는 수학여행지를 입력하세요 >>> ")
# student2 = input("희망하는 수학여행지를 입력하세요 >>> ")
# student3 = input("희망하는 수학여행지를 입력하세요 >>> ")
# 비어있는 list에 student 변수의 값들을 추가 -> student1,2,3은 field_trip의 요소(elements)가 됨.
# field_trip.append(student1)
# field_trip.append(student2)
# field_trip.append(student3)
# list를 set로 변환 -> 중복 제거를 위해서
# field_trip_set = set(field_trip)
# field_trip_list = list(field_trip_set)
# print(f"조사된 수학여행지는 {field_trip_set}입니다.")
# print(f"조사된 수학여행지는 {field_trip_list}입니다.")

# 반복문을 통한 간결한 코드
# 비어있는 list 생성
# field_trip2 = []
# for _ in range(3):      # 학생이 3명이라고 했기 때문에 in range(3) 작성 // 반복횟수만 명시하기 때문에 _ 사용함
#     student = input("희망하는 수학여행지를 입력하세요 >>> ")
#     field_trip2.append(student)
# field_trip2_set = set(field_trip2)
# field_trip2_list = list(field_trip2_set)
# print(f"조사된 수학여행지는 {field_trip2_set}입니다.")
# print(f"조사된 수학여행지는 {field_trip2_list}입니다.")
'''
사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤 그 숫자만큼 '과일 이름'을 입력 받아
'basket' 리스트에 저장하는 프로그램을 구현하세요.

실행 예
몇 개의 과일을 보관할까요? >>> 5
1번째 과일을 입력하세요 >>> 사과
2번째 과일을 입력하세요 >>> 바나나
3번째 과일을 입력하세요 >>> 체리
4번째 과일을 입력하세요 >>> 오렌지
5번째 과일을 입력하세요 >>> 망고
입력받은 과일들은 ["사과", "바나나", "체리", "오렌지", "망고"]입니다.
'''
count = int(input("몇 개의 과일을 보관할까요? >>> "))
basket = []
for i in range(count):
    fruit = input(f"{i+1}번째 과일을 입력하세요 >>> ")
    basket.append(fruit)
print(f"입력받은 과일들은 {basket}입니다.")

for i in range(1, count+1):                         # 시작값, 종료값 이용한 사례
    fruit = input(f"{i}번째 과일을 입력하세요 >>> ")
    basket.append(fruit)
print(f"입력받은 과일들은 {basket}입니다.")

