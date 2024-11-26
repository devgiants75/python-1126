'''
python_lesson_10_coffee_machine_pop
procedural-oriented programming -> 절차지향 프로그래밍
'''
MENU = {
    "에스프레소": {
        "재료": {
            "물": 50,
            "커피": 18,
        },
        "가격": 1.5,
    },
    "라떼": {
        "재료": {
            "물": 200,
            "우유": 150,
            "커피": 24,
        },
        "가격": 2.5,
    },
    "카푸치노": {
        "재료": {
            "물": 250,
            "우유": 100,
            "커피": 24,
        },
        "가격": 3.0,
    }
}
# 다중 딕셔너리에서의 value를 조회하는 방법 예시
# print(MENU["라떼"]["가격"])
# # 카푸치노의 우유의 양
# print(MENU["카푸치노"]["재료"]["우유"])
# # 에스프레소의 커피의 양
# print(MENU["에스프레소"]["재료"]["커피"])

profit = 0              # 현재 자판기 내에 들어 있는 금액
resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,
}
# 함수 정의 부분
# 4번 과정과 관련된 함수 작성
def is_resource_sufficient(order_ingredients):      # order_ingredients를 dict로 가정
    """DocString : 함수/클래스가 어떤 작동을 하는지 '사람들에게' 설명해주는 기능
    True / False를 반환 -> 주문 받은 음료를 resources에서 재료 차감을 하고 난 후
    음료 만들기가 가능하면 True 아니면 False를 반환
    """
    # 어떻게 하면 resources의 value들과 drink = MENU[choice]의 물, 우유, 커피들과 연산을 할 수 있을지 고민해야 함.
    for item in order_ingredients:      # item은 order_ingredients의 key들이 됨.
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다, 현재 {item}이(가) 부족합니다.")
            return False
        return True     # else를 쓰지 않은 이유 : 위의 if문이 실행되지 않았다면 어차피 True가 되기 때문

# 동전을 처리하는 함수 정의
def process_coins():
    """동전들을 입력 받아 전체 금액을 반환하는 함수"""
    print("동전을 넣으세요.")
    # 쿼터, 다임, 니켈, 페니 네 종류의 동전이 있음. 쿼터 = 0.25 달러 / 다임 = 0.1 달러 / 니켈 = 0.05 달러 / 페니 = 0.01 달러
    # 각각 input 함수를 통해 동전의 개수를 입력 받고 총합을 계산하는 함수를 작성하시오.
    # total = 0.0
    # 일부러 복잡한 예시
    # quarters = input("쿼터 동전을 몇개 넣으시겠습니까? >> ")                             # 지역 변수들을 선언
    # dimes =  input("다임 동전을 몇개 넣으시겠습니까? >> ")
    # nickels = input("니켈 동전을 몇개 넣으시겠습니까? >> ")
    # pennies = input("페니 동전을 몇개 넣으시겠습니까? >> ")
    # total = (int(quarters) * 0.25) + (int(dimes) * 0.1) + (int(nickels) * 0.05) + (int(pennies) * 0.01)
    total = int(input("쿼터 동전을 몇개 넣으시겠습니까? >> ")) * 0.25
    total += int(input("다임 동전을 몇개 넣으시겠습니까? >> ")) * 0.1
    total += int(input("니켈 동전을 몇개 넣으시겠습니까? >> ")) * 0.05
    total += int(input("페니 동전을 몇개 넣으시겠습니까? >> ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):  # money_received는 process_coins()의 리턴값
    """거래가 수락되면 True, 실패하면(동전의 총합 음료 가격보다 적다면) False를 반환"""
    charge = money_received - drink_cost
    # 이하에 작성할 부분은 money_received가 drink_cost보다 많거나 같다면 -> profit에 drink_cost만큼 추가해주고,
    # 커피를 만드는 과정으로 넘어가기 위헤 True를 리턴
    # 아니라면, "죄송합니다. 돈이 충분하지 않습니다. 동전을 반환합니다."를 출력하고 False를 반환
    # 이상의 지시사항을 만족하는 조건문을 작성하시오.
    if charge >= 0:
        # 지역 변수 / 전역 변수 개념 -> 함수 내의 변수가 main단계에 있는 변수를 조작하는 것이 권장되지 않음
        global profit   # 함수 내에서 전역 변수의 값을 변환시키는 키워드 -> global // 권장되지는 않습니다.
        profit += drink_cost
        print(f"잔돈 $ {charge}를 반환합니다.")
        return True
    else:
        print("죄송합니다. 돈이 충분하지 않습니다. 동전을 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """resources에 있는 재료에서 MENU["음료이름"]["재료"]들을 차감함 -> 차감은 무조건 이루어짐
    -> is_resource_sufficient를 통과했기 때문에."""
    # 어떻게 하면 resources의 재료들에서 해당 음료의 재료들을 차감할 수 있나요? -> 아까 전에 했습니다
    # drink_name과 order_ingredients를 이용해서 차감해야 함.
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"{drink_name}☕이(가) 나왔습니다. 맛있게 드세요😊")


# main 및 함수 호출 부분
is_on = True
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 : ")
    # 만약에 choice가 off라면 반복문 종료하는 코드를 작성하시오.
    if choice == "off":
        is_on = False
        # break
    # 만약 choice가 report라면 현재의 물, 우유, 커피, 그리고 돈을 조회할 수 있도록 하는 조건문 작성
    elif choice == "report":
        print(f"물의 양은 {resources['물']}ml,\n우유의 양은 {resources['우유']}ml,\n커피의 양은 {resources['커피']}g,\n현재 자판기 내의 돈은 $ {profit}입니다.")
    elif choice in ("에스프레소", "라떼", "카푸치노"):
        drink = MENU[choice]
        # 메뉴명을 올바르게 입력했을 때 이루어지는 자판기의 처리 과정
        # 1. 해당 음료에서 소모되는 원재료의 양이 자판기 내에 충분히 있는지를 확인 True / False ->
        # 2. 동전을 넣는 process를 확인 -> 동전의 총합 -> 음료 가격보다 높다면 다음 과정으로 ->
        # 3. 자판기 내의 원재료에서 음료가 요구하는 원재료만큼 차감, 자판기에 수익을 더해야 함(음료 가격만큼), 음료 추출
        if is_resource_sufficient(drink["재료"]): # resources의 key는 물, 우유, 커피이기 때문에 "재료"키를 추출 불가능
                                                 # 따라서, argument로 drink["재료"]까지 명시해야 함. drink는 불가능
            # 여기가 실행이 되었다면 is_resource_sufficient()가 True라는 의미 -> 2번 단계로 넘어가야 함. -> 동전 넣고, 동전 합 계산
            if is_transaction_successful(money_received=process_coins(), drink_cost=drink["가격"]):
                # 여기가 실행이 되었다면 is_transaction_successful의 결과값이 True -> charge >= 0일거고, coffee가 나와야 함.
                make_coffee(drink_name=choice, order_ingredients=drink["재료"])
    else:           # 오타가 났을 경우
        print("잘못 입력 하셨습니다, 다시 입력해주세요.")












