'''
python_lesson_15_class_and_static

p 278

1. 클래스 변수

    인스턴스 변수 : 인스턴스마다 서로 다른 값을 가지는 경우
    클래스 변수 : 모든 인스턴스가 동일한 값을 가지는 경우

    인스턴스 변수 :
        목적 - 인스턴스 마다 다른 값을 저장
        접근 방식 - 인스턴스 접근(o)
                 - 클래스  접근(x)

    클래스 변수 :
        목적 : 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                 - 클래스 접근(o)
클래스 변수
'''
# class Korean:
#
#     country = "한국"      # 클래스 변수
#
#     def __init__(self, name, age, address): #생성자 -> name, age, address : 인스턴스 변수
#         self.name = name
#         self.age = age
#         self.address = address

# man = Korean("안근수", 37, "부산광역시 연제구")        # man 객체를 생성
# 인스턴스 변수들을 확인
# print(man.name)
# print(man.age)
# print(man.address)
# print()
# 인스턴스인 man을 통해 클래스 변수에 접근 -> 해당 방식의 경우 클래스 변수인지 인스턴스 변수인지 확인하기가 어려움.
# print(man.country)
# 클래스 Korean을 통한 클래스 변수 접근 -> 클래스 변수인 경우 클래스명.변수명 으로 접근함.
# print(Korean.country)
'''
클래스 메서드
'''
# class Korean2:
#     country = "대한민국"    # 클래스 변수 선언 및 초기화
#
#     @classmethod        # 이하의 메서드가 클래스 메서드임을 명시 -> 클래스 메서드 : 클래스 변수를 사용하는 메서드
#     def trip(cls, travelling_site): # 클래스 메서드에서 클래스 변수를 참조할 때는 cls를 명시함.
#         if cls.country == travelling_site:
#             print("국내 여행입니다.")
#         else:
#             print("해외 여행입니다.")

# 클래스 메서드 호출    -> 클래스 메서드의 호출이기 때문에 인스턴스 메서드 호출 때 처럼 객체 생성을 선행할 필요가 없다.
# Korean2.trip("대한민국")
# Korean2.trip("미국")
'''
p 279

2. 클래스 메서드

클래스 메서드(class method) : 클래스 변수를 사용하는 메서드

특징 :

1. 인스턴스 또는 클래스로 호출 -> 하지만 클래스 변수와 마찬가지로 클래스로 호출하는 것이 권장됨.
2. 생성된 인스턴스가 없어도 호출 가능
3. @classmethod 데코레이터(decorator)를 표시하고 작성 -> 그러면 자동으로 첫번째 매개변수로 cls가 적용됨. 
    명시하지 않으면 인스턴스 메서드로 간주되어 self가 첫번째 매개변수로 적용됨.
4. 매개변수 self를 사용하지 않고 cls를 사용

호출 방식 :

클래스명.메서드명() -> self를 사용하지 않기 때문에 '인스턴스 변수에 접근이 불가능. cls를 통해 class 변수에만 접근 가능'

Korean2 클래스에서 정의된 trip() 메서드는 클래스 메서드임을 알리는 @classmethod로 시작.
첫번째 매개변수인 cls는 class의 축약형. 여기서는 클래스 Korean2를 의미함.
따라서 내부의 cls.country는 Korean2.country와 동일한 의미. 이를 클래스 내부에서는 cls.country로 표기함.
클래스 메서드는 인스턴스를 생성하지 않아도 클래스만으로 호출이 가능, 즉 Korean2.trip(인수)로 호출 가능함.

p 280

정적 메서드(static method)

정적 메서드 또한 self를 사용하지 않음 -> 이 의미는 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미 : class method와의 공통점
인스턴스를 생성하지 않아도 사용할 수 있다는 점 때문에 클래스 메서드와 유사함.

특징 :

1. 인스턴스 또는 클래스로 호출 가능 -> 클래스 메서드와 같음
2. 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와 같음
3. @staticmethod 데코레이터를 표시하고 작성 -> 클래스 메서드와 다름
4. 반드시 작성해야 할 매개변수가 없음 -> 클래스 메서드와 다름

정적 메서드는 self, cls를 다 사용하지 않기 땜누에 인스턴스 변수와 클래스 변수를 모두 사용하지 않는 메서드를 정의하는 경우에 적절함.
정적 메서드는 클래스에 소속돼 있지만 인스턴스에는 영향을 주지도 않고 또 영향을 받지도 않음.
'''
class Korean3:
    country = "한국"      # 클래스 변수

    @staticmethod        # 정적 메서드 선언
    def slogan():        # self, cls 둘 다 적용되지 않음 -> 데코레이터를 달거나 메서드를 작성해도 자동 생성이 되지 않음으로 확인 가능
        print("Imagine your Korea")

    # @classmethod
    # def trip(cls):
    #     pass
    #
    # def __init__(self, name):
    #     self.name = name
    #
    # def introduce(self):
    #     pass

# 정적 메서드 호출
# Korean3.slogan()

'''
기본 예제

다음은 가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스입니다.
'''

# class Bag:
#
#     count = 0       # 클래스 변수 선언 및 초기화
#
#     def __init__(self):     # 생성자 -> 인스턴스 변수들을 선언하고 초기화하겠다는 의미
#         Bag.count += 1      # 객체를 하나 생성할 때마다 count가 1씩 증가됨. -> 인스턴스 메서드를 통해서 클래스 변수를 참조
#         print("가방이 생산되었습니다.")
#
#     @classmethod
#     def sell(cls):
#         print("가방이 팔렸습니다.")
#         cls.count -= 1      # 클래스 메서드에서 클래스 변수를 참조하는 사례 // 129번 라인과 135번 라인의 차이를 확인할 것
#
#     @classmethod            # 클래스 변수를 참조하는 것이기 때문에 클래스 메서드를 생성
#     def remain_bag(cls):    # 직접 참조하는 것이 별로 좋지 않기 때문에 클래스 변수를 참조하는 getter 메서드 생성
#         return cls.count
#
# print(f"현재 가방 개수 : {Bag.remain_bag()}")   # Bag.count가 아닌 것에 주목
# # 객체 생성
# bag1 = Bag()
# bag2 = Bag()
# bag3 = Bag()
# print(f"현재 가방 개수 : {Bag.remain_bag()}")
# # print(f"현재 가방 개수 : {Bag.count}")        # 보안상 좋지 않기 때문에 주석 처리해둡니다.
# bag1.sell()                                   # 클래스 메서드를 사용하는 것인데 Bag.sell()을 사용한 것이 아니라
# bag2.sell()                                   # 인스턴스를 통해 메서드를 호출했다는 단점이 있음.
# bag3.sell()
# bag1.sell()                                   # 소멸자를 정의하지 않은 상태이기 때문에 bag1.sell()을 사용하더라도 적용되는 문제가 있음
# print(f"현재 가방 개수 : {Bag.remain_bag()}")

'''
응용 예제

1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 생성하세요.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하세요.      -> 생성자와 관련있는 부분
man = Person("james")                                     -> Person("james")를 봤을 때, __init__(self, name): 임을 확인 가능
woman = Person("emily")

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하세요.       -> 생성될 때 콘솔에서 출력돼야 함. : contructor_and_destructor에서 학습함
james is born.
emily is born.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하세요.              -> 클래스 메서드를 정의하라는 의미
print(f"전체 인구수 : {Person.get_population()}")                        -> 대문자 P인 점, 그리고 . 뒤를 확인하면 메서드 명 확인 가능

4. 다음과 같은 방법으로 man 인스턴스를 삭제하세요.                           -> 소멸자 정의하세요 : constructor_and_destructor 확인하세요
del man                                                                 -> Bag 클래스 확인하세요

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하세요.
james is dead.
'''
# class Person:
#
#     # 지시사항 3번
#     population = 0          # 클래스 변수를 선언 및 초기화 -> Bag 클래스에서 힌트가 있음
#
#     # 지시사항 1, 2번
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is born.")
#         # 객체가 생성되었을 때 클래스 변수인 population을 1 증가 시켜야 함.
#         Person.population += 1      # cls 아닙니다.
#
#     # 지시사항 3번
#     @classmethod
#     def get_population(cls):
#         return cls.population       # 여기는 cls입니다.
#
#     # 지시사항 4번
#     def __del__(self):
#         Person.population -= 1      # cls 아닙니다.
#         # 지시사항 5번
#         print(f"{self.name} is dead")

# man = Person("james")
# print(f"전체 인구수 : {Person.get_population()}")
# woman = Person("emily")
# print(f"전체 인구수 : {Person.get_population()}")
# # 지시사항 4번
# del man
# print(f"전체 인구수 : {Person.get_population()}")
'''
예제 1:

학생들의 성적을 관리하는 Student 클래스를 작성하세요. 이 클래스는 학생의 이름, 학번, 성적을 인스턴스 변수로 갖습니다.

지시 사항 :

1. Student 클래스를 정의하고 생성자를 통해 이름(name), 학번(student_id), 성적(grade)을 초기화하세요.
2. 학생의 프로필을 출력하는 인스턴스 메서드 print_grade()를 작성하세요.
3. 학생의 성적을 변경할 수 있는 인스턴스 메서드 set_grade()를 작성하세요.
4. 세 명의 학생 인스턴스를 생성하고, 각 학생의 정보를 출력한 다음 성적을 변경하고 다시 출력하세요.

student1 = Student("김철수", 2023001, "A")

실행 예

학생 이름: 김철수
학번: 2023001
성적: A

학생 이름: 이영희
학번: 2023002
성적: B

학생 이름: 박민수
학번: 2023003
성적: C

성적 변경 후 :
학생 이름: 김철수
학번: 2023001
성적: A+

학생 이름: 이영희
학번: 2023002
성적: B+

학생 이름: 박민수
학번: 2023003
성적: B
'''
# class Student:
#     # 생성자
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade
#     # setters
#     def set_name(self, new_name):
#         # 새로 입력하는 이름이 기존의 이름과 동일한 경우에 메서드를 정지시키고 싶은 경우
#         if self.name == new_name:
#             print("기존의 이름과 동일합니다.")
#             return                  # 함수 / 메서드에서 비어있는 return을 입력할 경우 함수/메서드 정지
#         else:
#             self.name = new_name
#
#     def set_student_id(self, new_student_id):
#         self.student_id = new_student_id
#
#     def set_grade(self, new_grade):
#         self.grade = new_grade
#
#     # getters
#     def get_name(self):
#         return self.name
#
#     def get_student_id(self):
#         return self.student_id
#
#     def get_grade(self):
#         return self.grade
#
#     def print_grade(self):
#         return f"학생 이름 : {self.name}\n학번 : {self.student_id}\n성적 : {self.grade}\n"
#
#
#
#
# student1 = Student("김철수", 2023001, "A")
# student2 = Student(name="이영희", student_id=2023002, grade="B")   # keyword argument
# student3 = Student("박민수", 2023003, "C")
# print(student1.print_grade())
# print(student2.print_grade())
# print(student3.print_grade())
# print("성적 변경 후")
# student1.set_grade("A+")
# student2.set_grade("B+")
# student3.set_grade("B")
# print(student1.print_grade())
# print(student2.print_grade())
# print(student3.print_grade())
# student1.set_name("안근수")
# print(student1.print_grade())
# student1.set_name("안근수")
#
# student1.name = "안근수"
# print(student1.name)

'''
클래스 변수 / 클래스 메서드 활용 예제

1. 다음 지시 사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 작성하세요.

지시 사항

1. Shop 클래스는 다음과 같은 변수를 가지고 있다.
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 딕셔너리 요소를 지니는 리스트
    menu_list = [ {메뉴명1:가격1}, {메뉴명2:가격2} ]
    
    menu_list = [ {"떡볶이": 3000}, {"순대": 4000}, {"튀김": 500}, {"김밥": 2000} ]
    
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
Shop.sales("떡볶이", 1)        # 떡볶이을(를) 1개 판매     
Shop.sales("김밥", 2)        # 김밥을(를) 2개 판매     
Shop.sales("튀김", 5)        # 튀김을(를) 5개 판매     

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f"매출 : {Shop.show_total_sales()}원")
'''
# class Shop:
#     #클래스 변수 선언
#     total = 0       # 전체 매출액을 나타내는 클래스 변수
#     menu_list = [{"떡볶이": 3000}, {"순대": 4000}, {"튀김": 500}, {"김밥": 2000}]    # 메뉴를 나타내는 list도 클래스 변수로 도입
#
#     # 클래스 메서드를 정의
#     @classmethod
#     def sales(cls, item, quantity):
#         # cls.menu_list를 참조해야 함.
#         for menu in cls.menu_list:  #반복문의 결과값은 list의 element이므로 menu = dictionary가 됨.
#             if item in menu:    # menu에서 item 조건문을 작성하게 되면 key가 나옴.
#                 price = menu[item]  # menu[item]은 dictionary'들'의 value가 됨.
#                 total_price = price * quantity  # 전체 가격 = 메뉴의 가격 * 수량
#                 print(f"{item}을(를) {quantity}개 판매")
#                 cls.total += total_price
#
#     @classmethod
#     def show_total_sales(cls):
#         return cls.total
#
#
# Shop.sales("떡볶이", 1)
# Shop.sales("김밥", 2)
# Shop.sales("튀김", 5)
# # print(Shop.total)
# print(f"매출 : {Shop.show_total_sales()}원")
'''
2. 은행 계좌를 관리하는 BankAccount 클래스를 작성하세요. 이 클래스는 계좌 소유자 이름, 계좌 번호, 잔액을 인스턴스 변수로 갖습니다.

지시 사항

1. BankAccount 클래스를 정의하고, 생성자를 통해 소유자 이름(owner), 계좌 번호(account_num), 잔액(balance)을 초기화하세요.
2. 입금 기능을 하는 인스턴스 메서드(deposit())을 구현하세요. -> 입금 잔액을 받아 잔액을 증가시킵니다.
3. 출금 기능을 하는 인스턴스 메서드(withdraw())를 구현하세요. -> 출금 금액을 받아 잔액을 감소시킵니다. -> 잔액이 부족하면 출금이 불가능하도록 작성
4. 계좌 정보를 출력하는 인스턴스 메서드 print_account_info()를 구현하세요 -> 소유자 이름 / 계좌 번호 / 잔액 전체 print 할 것
5. 두 개의 계좌를 생성하고, 입금과 출금을 수행한 후 계좌 정보를 출력하세요.

실행 예
계좌 소유자 : 홍길동
계좌 번호 : 123-456-789
현재 잔액 : 100000원                             (십만원)

계좌 소유자 : 신사임당
계좌 번호 : 987-654-321
현재 잔액 : 500000원                             (오십만원)

50000원이 입금되었습니다. 현재 잔액 : 150000원        # -> account1에 대한 입금 (오만원 입금)
잔액이 부족하여 출금할 수 없습니다.                    # -> account1에서 200000 출금 시도 실패 사례 (이십만원 출금 실패)
100000원이 출금되었습니다. 현재 잔액 : 50000원        # -> account1에 대한 출금 (십만원 출금 성공)

100000원이 출금되었습니다. 현재 잔액 : 400000원       # -> account2에 대한 출금 (십만원 출금)
200000원이 입금되었습니다. 현재 잔액 : 600000원       # -> account2에 대한 입금 (이십만원 입금)

최종 계좌 정보
계좌 소유자 : 홍길동
계좌 번호 : 123-456-789
현재 잔액 : 50000원                             (오만원)

계좌 소유자 : 신사임당
계좌 번호 : 987-654-321
현재 잔액 : 600000원                             (육십만원)

'''

class BankAccount:
    # 지시 사항 1번
    def __init__(self, owner, account_num, balance):
        self.owner = owner
        self.account_num = account_num
        self.balance = balance

    # 지시 사항 2번  -> setter 개념을 응용
    def deposit(self, income):
        """입금액을 받아 잔액을 증가시킴"""
        self.balance += income
        print(f"{income}원이 입금되었습니다. 현재 잔액 : {self.balance}원")

    # 지시 사항 3번 -> setter 개념을 응용
    def withdraw(self, outcome):
        """출금 액을 받아 잔액을 감소 시킴. 출금 액이 잔액 보다 큰 경우 출금 불가 관련 메시지를 출력함 -> 실행 예 확인할 것"""
        if outcome > self.balance:
            print("잔액이 부족하여 출금할 수 없습니다.")
        else: # self.balance가 outcome 이상일 때
            self.balance -= outcome     # self.balance = self.balance - outcome
            print(f"{outcome}원이 출금되었습니다. 현재 잔액 {self.balance}")

    # 지시 사항 4번 -> getter 개념 응용 return / print 쓰셔도 됩니다.  / 가공된 데이터이기 때문에 print()문을 쓰도록 하겠습니다.
    def print_account_info(self):
        print(f"계좌 소유자 : {self.owner}\n계좌 번호 : {self.account_num}\n현재 잔액 : {self.balance}")

# 지시 사항 1번을 완료했을 때 객체 생성 가능
account1 = BankAccount(owner="홍길동", account_num="123-456-789", balance=100000)
account2 = BankAccount(owner="신사임당", account_num="987-654-321", balance=500000)

# deposit, withdraw, print_account_info의 경우 인스턴스 메서드이기 때문에 호출 방식은
# income = int(input("입금 액은 얼마 입니까? >>> "))
account1.print_account_info()
print()
account2.print_account_info()
print()
account1.deposit(50000)
account1.withdraw(200000)
account1.withdraw(100000)
print()
account2.withdraw(100000)
account2.deposit(200000)
print()
print("최종 계좌 정보 : ")
account1.print_account_info()
print()
account2.print_account_info()










