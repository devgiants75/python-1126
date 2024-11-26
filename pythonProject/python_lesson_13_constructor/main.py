'''
python_lesson_13_constructor -> main.py

p 276

1. 생성자?(Constructor)
'''
# 클래스 정의
# class Candy:
#
#     def set_info(self, shape, color):       # 생성자가 아닌 set_info 메서드를 통해 속성에 값 대입
#         self.shape = shape
#         self.color = color
#
#     def get_info(self):
#         return f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다."

# 객체 생성
# satang = Candy()        # satang 객체 생성 -> 생성자가 없기 때문에 빈값으로만 생성 가능
# satang.set_info("구형", "갈색")
# print(satang.get_info())
'''
satang 인스턴스는 생성된 후에 set_info() 메서드를 호출하여 "구형" 모양의, "갈색" 사탕이라는 값을 지니게 됨.(값 = 속성)

satang 인스턴스의 생성 과정 :
1. 값이 없는 인스턴스를 생성
2. 값을 저장할 수 있는 메서드를 호출

그렇다면 처음부터 값이 있는 인스턴스를 생성하기 위한 방법은 무엇인가? -> __init__() 메서드

__init__() 메서드(생성자)는 인스턴스가 생성될 때 '자동으로 호출'되기 때문에 인스턴스 변수의 초기화 용도로 사용,
값이 있는 인스턴스를 생성할 수 있다는 의미 -> init 자체가 initialization의 축약어입니다.

'객체 생성과 동시에' 생성자가 호출됨 -> 초기값을 작성할 때 사용 

형식 :

class 클래스명:
    
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
'''
# 클래스 생성
# class Candy2:
#
#     # 생성자 정의 -> 그렇다면 set_info(self, shape, color) 메서드는 필요 없음.
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def get_info(self):
#         return f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다."

# 객체 생성
# satang2 = Candy2("정육면체", "흰색")
# print(satang2.get_info())
'''
이상에서 주목해야 할 점은 satang 인스턴스와 satang2 인스턴스의 생성 방식 차이입니다. -> 한 줄 줄였다
satang = Candy()
satang.set_info("구형", "갈색)
print(satang.get_info())

satang2 = Candy2("정육면체", "흰색")
print(satang2.get_info())

2. 소멸자(Desctructor)

인스턴스가 생성될 때 자동으로 생성되는 생성자와 마찬가지로 인스턴스가 소멸될 때 호출되는 메서드가 있음.
이를 소멸자라고 하며, 소멸자를 정의하는 메서드는 __del__()
'''
# 클래스 정의
# class Sample:
#
#     # 생성자 정의
#     def __init__(self):
#         print("인스턴스가 생성되었습니다.")
#     # 소멸자 정의
#     def __del__(self):
#         print("인스턴스가 소멸됩니다.")

# 객체 생성
# sample = Sample()
# # del sample          # del 객체명을 작성하면 자동으로 소멸됨. -> 소멸되는 시점을 개발자가 통제할 수 있음.
# print("이 line 밑으로 프로그램이 종료됩니다.")
'''
기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 구현하시오.

1. 클래스 USB를 만드시오
2. 생성자를 정의하여 매개변수로 capacity를 받고, get_info() 메서드를 정의하시오.

main 단계의 코드 라인
usb = USB(64)
usb.get_info()

실행 예
64GB USB
'''
# 지시사항 1번
# class USB:
#     # 지시사항 2-1
#     def __init__(self, capacity):
#         # 지시사항 2-2
#         self.capacity = capacity
#
#     #지시사항 2-3
#     def get_info(self):
#         print(f"{self.capacity}GB USB")

# main 단계
# usb = USB(64)
# usb.get_info()

'''
생성자와 소멸자를 이용하여 서비스 안내 메시지를 출력하는 프로그램을 작성하시오.

class Service를 정의하고, 생성자를 통해 매개변수로 service를 받고, print()문을 쓰시오.
소멸자를 정의하여 Service가 종료되었음을 안내하시오.

s = Service("길 안내")
del s

실행 예
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.
'''
# 클래스 정의
# class Service:
#     # 생성자 정의
#     def __init__(self, service):
#         self.service = service
#         print(f"{self.service} Service가 시작되었습니다.")
#     # 소멸자 정의
#     def __del__(self):
#         print(f"{self.service} Service가 종료되었습니다.")
#
# # 객체 생성
# s = Service("길 안내")
# del s
# print("이 line 밑으로 프로그램이 종료됩니다.")



