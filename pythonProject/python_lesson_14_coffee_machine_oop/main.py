from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 외부 모듈에서 import 해온 것을 토대로 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()  # menu.get_items()의 return 값을 options라는 변수에 담음
    choice = input(f"어떤 음료를 드시겠습니까? {options} >>> ")
    # choice == "off" 일 때 / choice == "report"일 때 어떻게 해야하는지 작성하시오.
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink == None:       # input 함수에서 입력한 철자가 맞는지 틀린지 확인
            continue            # 만약에 메뉴에 없는 철자라면 while 반복문의 맨 처음으로 돌아가고 이 밑의 코드는 실행시키지 않음
        # 4. 자원이 충분한지 확인 -> coffee_maker 확인하셔야 함.
        if coffee_maker.is_resource_sufficient(drink):
            # coffee_maker.is_resource_sufficient() 메서드를 확인해보면, drink.ingredients를 반복문을 돌리는 것을 확인할 수 있음
            # argument에 drink만 넣어도 괜찮다 / drink.ingredients를 argument로 넣으면 오류가 남.

                # 5. 결제를 하는 코드 -> money_machine 확인하셔야 함.
                # 동전을 집어넣는 메서드인 process_coins()의 경우, make_payment() 메서드를 확인해본 결과, make_payment()를
                # 호출하면 맨 처음에 process_coins()가 호출되는 것을 확인할 수 있음
                # -> 그렇기 때문에 main 단계에서 money_machine.process_coins()를 호출해서는 안됨.
                if money_machine.make_payment(drink.cost):
                    # 이하의 코드가 실행이 된다면 위의 make_payment() 메서드가 True라는 의미이므로 다음 단계로 넘어가야 함.
                    # 6. 커피를 만드는 코드 -> coffee_maker를 확인하셔야 함.
                    coffee_maker.make_coffee(drink)





