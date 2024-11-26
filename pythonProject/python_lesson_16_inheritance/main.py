'''
python_lesson_16_inheritance

p 283

1. 상속이란?
    어떤 클래스가 가지고 있는 기능을 그대로 물려 받아서 사용할 수 있는 클래스를 생성할 수 있는데,
    클래스의 기능을 물려 받을 때 상속 받는다는 표현을 사용함.
    상속 관계에 있는 클래스들을 표현할 때 부모 클래스 / 자식 클래스 라는 용어를 사용.

    기능을 물려 주는 클래스 = 부모 클래스 = 슈퍼 클래스 = 기반 클래스
    기능을 물려 받는 클래스 = 자식 클래스 = 서브 클래스 = 파생 클래스


2. 상속 관계 구현
    두 클래스가 상속 관계에 놓이려면 IS-A 관계를 성립해야 함. IS-A 관계란 "~은 ~이다"로 해석될 수 있는 관계를 의미
    ex) "학생은 사람이다." 주어(자식 클래스)는 보어(부모 클래스)이다.

    *IS-A 원문 : is a kind of -> Dog is a kind of animal. -> '개'는 '동물'의 한 종류이다.

    형식 :
class 슈퍼_클래스:
    본문

class 서브_클래스(슈퍼_클래스):
    본문
'''
# class Person:   # 클래스 정의(슈퍼 클래스)
#     # 생성자 정의
#     def __init__(self, name):
#         self.name = name
#     # 인스턴스 메서드 정의
#     def eat(self, food):
#         print(f"{self.name}이(가) {food}을(를) 먹습니다.")
#
#
# class Student(Person):      # 서브 클래스
#     # 생성자 정의
#     def __init__(self, name, school):
#         super().__init__(name)  # name이라는 인스턴스 변수는 슈퍼 클래스로부터 상속 받겠다는 의미 -> 그래서 self.name = name이 아님
#         self.school = school
#
#     # 메서드 정의
#     def study(self):
#         print(f"{self.name}은(는) {self.school}에서 공부를 합니다.")

# 객체 생성
# potter = Student(name="해리포터", school="호그와트")
# potter.eat("감자")    # 슈퍼 클래스의 메서드를 서브 클래스의 객체가 그대로 사용 가능
# potter.study()
'''
3. 서브 클래스의 __init__()

서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없습니다. 그래서 서브 클래스의 생성자를 구현할 때는 '반드시' 슈퍼 클래스의 생성자를 먼저
호출하는 코드를 작성해야만 합니다.

super -> 슈퍼 클래스를 의미. 즉, Student의 생성자를 호출하려면 super().__init__(name)에 의해서
슈퍼 클래스인 Person의 생성자가 먼저 호출됨. -> 즉 슈퍼 클래스가 '생성'된다.
이후 슈퍼 클래스에서 생성된 인스턴스 변수인 name이 서브 클래스로 전달되고, 이후에 서브 클래스에서 school 인스턴스 변수에 값을 저장하면서
생성됩니다.

4. 서브 클래스의 인스턴스 자료형

슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
하지만 서브 클래스의 객체는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스
즉, Student의 객체는 Student의 인스턴스이면서 동시에 Person의 인스턴스

형식 :

isinstance(객체명, 클래스명)
'''
# 4 부분을 증명 -> potter는 Student의 인스턴스이면서 동시에 Person의 인스턴스
# print(isinstance(potter, Student))          # True
# print(isinstance(potter, Person))           # True

# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def speak(self):
#         print(f"{self.species}은(는) 소리를 냅니다.")
#
# class Dog(Animal):
#     def __init__(self, name, species="개"):
#         super().__init__(species)           # 슈퍼 클래스의 species매개변수를 그대로 받아와 서브 클래스에 적용
#         self.name = name
#
#     def bark(self):
#         print(f"{self.name}이(가) 짖습니다. 멍멍!")
#
# # Cat 클래스를 정의하고 생성자까지 만들어보세요.
# class Cat(Animal):
#     def __init__(self, name, species="고양이"):
#         super().__init__(species)
#         self.name = name
#
#     # meow() 메서드를 정의하고, cat이라는 객체명을 지니는 객체를 생성한 뒤, cat.meow()를 실행했을 때 콘솔에 "야옹이이(가) 웁니다. 야옹!"
#     # 이 출력되도록 작성하시오.
#     def meow(self):
#         print(f"{self.name}이(가) 웁니다. 야옹!")
#
# # dog = Animal("개")       # 슈퍼 클래스의 객체 생성
# dog = Dog("멍멍이")
# dog.bark()
# cat = Cat("야옹이")
# print(cat.species)      # 권장되지 않는 데이터를 직접 참조하는 사례
# cat.meow()

'''
상속 예제 1

다음 지시 사항을 읽고 Hybrid 클래스를 구현하세요.

지시 사항

1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스를 구현하세요. -> 강사가 표기할 예정
2. 서브 클래스 Hybrid는 다음과 같은 특징을 가지고 있습니다.
    최대 배터리 충전량은 30입니다.
    배터리를 충전하는 charge() 메서드가 있습니다. 최대 충전량을 초과하도록 충전할 수 없고,
    0보다 작은 값으로 충전할 수 없습니다.
    현재 '주유량'과 '충전량'을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.
    
3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil=0, amount=0)       # 객체 생성 방식에 주목할 필요가 있음 -> 생성자의 매개변수명 확인이 가능합니다.
car.add_oil(100)
car.charge(50)
car.hybrid_info()                   # 현재 주유 상태 : 50\n현재 충전 상태 : 30
'''
class Car:
    max_oil = 50            # 클래스 변수

    def __init__(self, oil):        # 생성자
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:
            return          # 메서드 정의 후 return 후 아무 값도 쓰지 않는다면 메서드를 종료하겠다는 의미
        self.oil += oil
        if self.oil > Car.max_oil:  # 인스턴스 메서드인데 클래스 변수를 참조해야한다면 cls.max_oil이 아니라 Car.max_oil로 작성해야 함.
                                    # 주유 후 최대 주유량 초과 상태라면
             self.oil = Car.max_oil # 현재 주유량을 최대 주유량으로 설정

    def car_info(self):
        print(f"현재 주유 상태 : {self.oil}")

# 서브 클래스 Hybrid를 정의하시오.
class Hybrid(Car):
    max_amount = 30

    def __init__(self, oil, amount):
        super().__init__(oil)       # 슈퍼 클래스의 생성자의 매개변수인 oil을 받아오고
        self.amount = amount        # 슈퍼 클래스에는 없는 자식 클래스의 고유 매개변수인 amount는 직접 작성함.

    def charge(self, amount):
        if amount <= 0:             # 충전량이 0이하라면 충전이 일어날 수 없도록 작성
            return
        self.amount += amount       # amount를 더한 후에 그 값이 max_amount를 초과한다면 max_amount값으로 고정시켜야 함.
        if self.amount > Hybrid.max_amount:
            self.amount = Hybrid.max_amount

    def hybrid_info(self):
        super().car_info()              # super() 키워드를 이용하여 슈퍼 클래스의 메서드를 그대로 불러올 수 있음.
        print(f"현재 충전 상태 : {self.amount}")


car = Hybrid(oil=0, amount=0)       # 객체 생성 방식에 주목할 필요가 있음 -> 생성자의 매개변수명 확인이 가능합니다.
car.add_oil(100)
car.charge(50)
car.hybrid_info()                   # 현재 주유 상태 : 50\n현재 충전 상태 : 30

car2 = Car(30)                      # Car 클래스의 객체 car2 생성
# car2.charge(10)                     # 슈퍼 클래스의 객체는 서브 클래스의 메서드를 사용할 수 없음. -> 해당 라인은 오류 발생






