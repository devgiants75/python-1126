'''
python_lesson_18_turtle

'''
# turtle이라는 모듈을 사용하고, Turtle, Screen이라는 클래스를 사용한다는 의미
from turtle import Turtle, Screen
import random

t = Turtle()        # Turtle 클래스의 객체 t 생성
screen = Screen()   # Screen 클래스의 객체 screen 생성

t.shape("turtle")   # Turtle 클래스의 객체인 t에서 shape 메서드의 경우 argument로 str을 받으며, 특정
                    # str인 경우 모양을 바꿀 수 있음
t.color("red")
screen.bgcolor("black")

colors = [
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
]


# 거북이 이동 방법
# t.penup()
# t.forward(200)
# t.pendown()
# t.forward(200)

# 점선으로 이동 방법
# t.forward(10)
# t.penup()
# t.forward(10)
# t.pendown()
#
# t.forward(10)
# t.penup()
# t.forward(10)
# t.pendown()
#
# t.forward(10)
# t.penup()
# t.forward(10)
# t.pendown()
#
# t.forward(10)
# t.penup()
# t.forward(10)
# t.pendown()
#
# t.forward(10)
# t.penup()
# t.forward(10)
# t.pendown()

def draw_dotted_line():
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

# draw_dotted_line()

# draw_dotted_line을 수정하여 반복 횟수를 고정시키지 않고 그때그때 지정할 수 있도록 수정하시오
# def draw_dotted_line2(repeated_num):
#     for _ in range(repeated_num):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()

# draw_dotted_line2(30)

# draw_dotted_line3을 정의해서 argument를 입력 받아 그 횟수만큼 반복이 실행될 수 있도록 수정하시오.

# def draw_dotted_line3(repeated_num):
#     for _ in range(repeated_num):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()

# times = int(input("몇 번 반복하시겠습니까? >>> "))
# draw_dotted_line2(times)
# draw_dotted_line2(10)

# 한 변의 길이가 100짜리인 정사각형을 그리시오.
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# 한 변의 길이가 100인 정삼각형을 그리시오
#
# for _ in range(3):
#     t.forward(100)
#     t.left(120)
#
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
# # 한 변의 길이가 100인 정오각형을 그리시오
# for _ in range(5):
#     t.forward(100)
#     t.left(72)
# # 한 변의 길이가 100인 정육각형을 그리시오.
# for _ in range(6):
#     t.forward(100)
#     t.left(60)


def draw_shapes(num_sides):
    for _ in range(num_sides):
        # t.forward(100)
        draw_dotted_line()
        t.left(360 / num_sides)

# draw_shapes(3)
# draw_shapes(4)
# draw_shapes(5)
# draw_shapes(6)
# draw_shapes(7)
# draw_shapes(8)
# draw_shapes(9)
# draw_shapes(10)

# 반복문 적용
# for i in range(3, 11):
#     draw_shapes(i)  # 시작값 3부터 11미만까지 반복
#     t.color(random.choice(colors))


# .setheading() -> 특정 각도로 거북이를 회전시키는 메서드
# .heading() -> 거북이가 바라보는 방향을 나타내는 속성, degree(도) 단위로 표현됨. 시계 방향으로 측정
# 0도 : 오른쪽
# 90도 : 위쪽
# 180도 : 왼쪽
# 270도 : 아래쪽
# t.heading()의 return 값은 float 형태로 콘솔에 찍힘 -> 연산이 가능
# print(t.heading())
# t.forward(100)
# t.left(30)
# print(t.heading())
# for i in range(3, 11):
#     draw_shapes(i)  # 시작값 3부터 11미만까지 반복
#     t.color(random.choice(colors))
#     current_heading = t.heading()
#     t.setheading(current_heading + 10)

# for i in range(3, 11):
#     draw_shapes(i)  # 시작값 3부터 11미만까지 반복
#     t.color(random.choice(colors))
#     t.setheading(10)

# t.circle(50)

# 함수 정의
def draw_spriograph(size_of_gap):
    for _ in range(360 // size_of_gap): # range()의 매개변수는 int이고, a / b의 결과값은 float이기 때문에
                                        # a // b 형태로 작성해야 함.
        t.color(random.choice(colors))
        t.circle(80)
        t.setheading(t.heading() + size_of_gap)

# 함수 호출
t.speed(0)         # 거북이 속도 조절하는 메서드 -> 0이 가장 빠릅니다.
draw_spriograph(1)



screen.exitonclick()    # 클릭해야 screen이 종료되고 이후 main.py 파일이 전체 종료됨