'''
python_lesson_12_class -> main.py

p 258

1. 클래스 도입의 필요성
'''
# 매개 변수가 6개인 함수 정의
# def student_info(name, department, professor, phone, address, grade):
#     print(name)
#     print(department)
#     print(professor)
#     print(phone)
#     print(address)
#     print(grade)

# 변수에 데이터 대입
# name1 = "안근수"
# department1 = "영어교육과"
# professor1 = "David"
# phone1 = "010-7445-7113"
# address1 = "부산광역시 연제구"
# grade1 = "A"
# 함수 호출
# student_info(name1, department1, professor1, phone1, address1, grade1)
'''
지금까지 배운 함수와 매개변수, 그리고 argument를 통해 여섯 개의 변수를 처리할 수 있습니다. 하지만 만들어야 할 변수의 개수가 많고,
학생 한 명당 변수가 6개라면 학생이 100명일 경우 600개의 변수를 처리할 필요가 있습니다.

즉, 학생 한 명이 증가할 때마다 변수가 6개씩 증가하는 상황이 생깁니다.
'''
# student_info("안근순", "컴퓨터공학과", "Aaron", "010-1111-2222", "서울특별시 종로구", "B")
# student_info(name="강근수", department="화학과", professor="남궁혁", phone="010-2222-3333", address="경상남도 양산시", grade="C")
'''
이상의 상황들(변수에 데이터들을 각각 대입, 혹은 함수에 argument를 직접 등록, 또는 keyword argument를 통한 등록)을 벗어나기 위해
클래스와 객체 개념을 사용할 수 있습니다.

p 260

클래스 개념 : 객체를 만드는 도구 -> 청사진 / 설계도 / 틀 등으로 비유됨.
    하나의 클래스를 통해 여러 가지 객체를 만들 수 있음.
    
    자동차 설계도 -> 클래스
    설계도를 통해 생성된 자동차들 -> 객체
    
    같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있습니다.
    마찬가지로 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질 수 있습니다.
    
    인스턴스(instance) 역시 클래스를 이용해서 생성한 객체를 가리키는 용어입니다.
    객체와 인스턴스는 그 둘을 바라 보는 관점의 차이로 볼 수 있습니다.
    
    1. 자동차 설계도로 만든 자동차는 객체(object)입니다.
    2. 자동차는 자동차 설계도 클래스의 인스턴스(instance)입니다.

p 261

클래스 정의

클래스를 작성하는 것을 클래스 정의라고 함 -> 함수 정의와 비슷하다고 볼 수 있음.

형식 :

class 클래스명(대문자로 시작):
    본문
----------------------------
객체생성형식 :

객체이름 = 클래스명()
'''
# 클래스 정의 형식 예시
# class WaffleMachine:        # 클래스명은 대문자로 시작하는 upper camel case / 변수는 snake case
#     pass                    # 나중에 코드를 작성하겠다는 의미로 이 경우 실행시켜도 오류가 나지 않음

# 객체 생성 예시
# waffle = WaffleMachine()    # 객체 생성
# print(waffle)
'''
print(waffle)을 실행했을 때 <__main__.WaffleMachine object at 0x000002255B18DCA0>에서 object라고 표기된 점을 미루어
waffle은 WaffleMachine의 객체임을 확인할 수 있음

p 264

클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지니고 있습니다.
    객체를 생성하기 위해 클래스는 객체가 가져야 할 '값'과, '기능'을 가지고 있어야 합니다.
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 변수는 두 가지로 분리됩니다. 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수인 '클래스 변수'와
    모든 인스턴스들이 개별적으로 가지는 변수인 '인스턴스 변수'입니다.
    
    메서드는 특징에 따라서,
    클래스 메서드, 정적 메서드, 인스턴스 메서드로 분리됩니다.
    
    인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미
        모든 인스턴스 변수는 self라는 키워드를 앞에 붙여준다.
    인스턴스 메서드 : 인스턴스 변수를 사용하는 메서드
        인스턴스 변수값에 따라서 각 인스턴스(객체)마다 다르게 동작합니다.
        인스턴스 메서드는 첫번째 매개변수로 self를 추가해야 합니다.
        
    인스턴스 변수와 인스턴스 메서드는 객체지향프로그래밍(object-oriented programming)에서 중요한 개념입니다.
    이 두 가지를 클래스와 객체의 상태(인스턴스 변수)와 동작(인스턴스 메서드)을 정의하는 데 사용합니다.
    
    # 인스턴스 변수
    각 인스턴스(객체)마다 개별적으로 유지되는 변수. 객체가 생성될 때마다 새로 할당, 각 객체는 고유한 인스턴스의 변수 값을 가짐.
        인스턴스 변수의 정의 :
            인스턴스 변수는 일반적으로 클래스의 '생성자' 메서드(__init__) 내에서 self 키워드를 사용하여 정의됩니다.
'''
# 클래스 정의
# class Pokemon:
#     # 생성자 정의
#     def __init__(self, number, name, type):     # self는 항상 있어야 하는 것. number, name, type을 매개변수로 함.
#         self.number = number                    # 인스턴스 변수 1
#         self.name = name                        # 인스턴스 변수 2
#         self.type = type                        # 인스턴스 변수 3
#
#     # 메서드 예시 정의
#     def display_info(self):                     # self는 항상 있어야 하는 것. 해당 클래스의 객체임을 나타냄.
#         return f"번호 : {self.number}\n이름 : {self.name}\n타입 : {self.type}"
#
#     # 메서드 예시 정의 2
#     def display_info2(self):
#         print(f"번호 : {self.number}\n이름 : {self.name}\n타입 : {self.type}")

# 객체(인스턴스) 생성
# pokemon1 = Pokemon(1, "이상해씨", "풀/독")
# pokemon2 = Pokemon(type="불꽃", number=4, name="파이리")     # keyword argument의 사용 -> 순서가 바뀌어도 상관없음.
# pokemon3 = Pokemon()        # 이 경우 생성자할 때 argument 세 개를 입력하도록 클래스 정의를 했기 때문에 오류가 발생함.

# print(pokemon1)     # 객체임을 표시
# print(pokemon2)     # 객체임을 표시
#
# print(pokemon1.display_info())  # 속성을 확인하기 위해서는 속성을 표시하는 메서드를 정의하고, 이를 print()해야함.
# print()
# print(pokemon2.display_info())  # 속성을 확인하기 위해서는 속성을 표시하는 메서드를 정의하고, 이를 print()해야함.
'''
print() -> 함수
pokemon1.display_info() -> pokemon1이라는 객체에 종속된(인스턴스 변수를 사용하게 되는) display_info()는 인스턴스 메서드
'''
# print()
# pokemon1.display_info()
# pokemon2.display_info()

# pokemon2.name = "리자드"           # 객체의 name 속성에 직접 접근하여 그 값을 새로 대입한 사례 1
# pokemon2.number = 5               # 객체의 number 속성에 직접 접근하여 그 값을 새로 대입한 사례 2
# print()
# print(pokemon2.display_info())

# 한 객체의 속성을 직접 조회하는 방식
# print()
# print(pokemon1.number)
# print(pokemon1.name)
# print(pokemon1.type)

'''
인스턴스 변수와 인스턴스 메서드의 관계
- 인스턴스 변수는 객체의 데이터(값)를 저장합니다. 예를 들어 pokemon1 객체의 인스턴스 변수는 "이상해씨"라는 값을 가짐.
- 인스턴스 메서드는 이 데이터를 사용하여 동작을 수행합니다. 예를 들어 display_info() 메서드는 각 객체의 인스턴스 변수를 사용하여
    해당 객체의 번호 / 이름 / 타입을 출력함.
- 인스턴스 메서드는 self 키워드를 사용하여 객체의 인스턴스 변수에 접근할 수 있음. 이를 통해 객체 내부의 데이터에 접근 가능함.
'''
# 클래스 정의
# class Person:
#
#     def set_info(self, name, age, tel, address):        # init(생성자)를 사용하지 않는 예시
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.address = address
#
#     # 속성 하나씩 바꾸고, 조회하는 메서드 생성
#     # 속성 하나를 바꾸는 메서드
#     def set_name(self, name):
#         self.name = name
#
#     # 나이, 전화번호, 주소를 바꾸는 메서드들을 각각 정의하시오.
#     def set_age(self, age):
#         self.age = age
#
#     def set_tel(self, tel):
#         self.tel = tel
#
#     def set_address(self, address):
#         self.address = address
#
#     # 속성 하나만 조회하는 메서드
#     def get_name(self):
#         return self.name
#     # 나이, 전화번호, 주소를 각각 확인할 수 있는 get_age, get_tel, get_address를 각각 정의하시오.
#     def get_age(self):
#         return self.age
#
#     def get_tel(self):
#         return self.tel
#
#     def get_address(self):
#         return self.address

    # display_info()를 정의하시고, 전체 속성을 다 조회할 수 있도록 작성하시오 -> Pokemon 확인하시오.
    # def display_info(self):
        # return f"이름 : {self.name}\n나이 : {self.age}\n연락처 : {self.tel}\n주소 : {self.address}"
        # self.get_name() -> 메서드 내부에서 다시 메서드를 참조하는 형태
# 객체 생성
# boy = Person()      # 생성자를 클래스에 정의하지 않았기 때문에 pokemon1과 달리 소괄호 내에 아무런 값이 없어도 가능
# boy.set_info("안근수", 37, "010-7445-7113", "부산광역시 연제구")

# boy 객체의 이름, 나이, 전화번호, 주소를 수강생님 본인의 것으로 '각각' 바꾸시오. 그 후 '각각' 출력하시오.
# boy.set_name("Brian")
# boy.set_age(17)
# boy.set_tel("010-3333-4444")
# boy.set_address("뉴욕주 뉴욕시")
# print(boy.get_name())
# print(boy.get_age())
# print(boy.get_tel())
# print(boy.get_address())

# display_info()를 통해 콘솔창에 정보를 확인할 수 있도록 작성하시오.
# print(boy.display_info())
'''
응용 예제

다음 지시 사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book 클래스를 생성하세요.

지시 사항


1. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요.
책 제목 = title
책 저자 = author

book1 = Book()          # book1 = Book("파이썬", "민경태")가 아니라!!!!
book2 = Book()
2. set_title / set_author / set_info / get_title / get_author / print_info 메서드들을 정의하시오.
    단, print_info 메서드는 책 제목과 책 저자가 전부 나와야만 함.
    단, set_info 메서드는 책 제목과 책 저자를 전부 집어넣을 수 있어야 함.

실행 예
책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생텍쥐페리
'''
class Book:
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_info(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def print_info(self):
        return f"책 제목 : {self.title}\n책 저자 : {self.author}"

book1 = Book()
book2 = Book()

book1.set_title("파이썬")      # setter를 이용하여 각 속성마다 메서드를 활용해 값을 대입한 사례
book1.set_author("민경태")
book2.set_info(title="어린왕자", author="생택쥐페리")    # set_info 메서드를 활용하여 복수의 속성에 값을 대입한 사례

print(f"책 제목 : {book1.get_title()}")        # main 단계에서 f-string을 활용하여 함수형프로그래밍을 할 수 있도록 작성
print(f"책 저자 : {book1.get_author()}")
print()
print(book2.print_info())                     # 복수의 속성을 가져오기 때문에 굳이 f-string 활용할 필요없이
                                              # 메서드 내에 f-string을 사용한 사례



