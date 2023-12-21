from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#drink = MenuItem(, 200, 150, 24, 2.5)
main_menu = Menu()
# menu_item = MenuItem('name','water','')
coffee_maker_obj = CoffeeMaker()
machine = MoneyMachine()
# for item in main_menu.menu:
#     print(item.name, item.cost, item.ingredients)

# drink_choice = input(f"What would you like to have? ({order.get_items()}): ")
# if drink_choice == "report":
#     CoffeeMaker.report()

# print(drink.cost)
working = True
while working is True:
    print("Welcome! We have the following options: ")
    print(main_menu.get_items())
    choice = input("What would you like to have?: ")
    if choice == "report":
        machine.report()
    else:
        drink_menu = main_menu.find_drink(choice)
        check_sufficient = coffee_maker_obj.is_resource_sufficient(drink_menu)
        if check_sufficient:
            coffee_maker_obj.make_coffee(drink_menu)
            print(f"Cost of your drink is $ {drink_menu.cost}")
            # inp_amt = float(input("Enter amount: "))
            payment_success = machine.make_payment(drink_menu.cost)
            # if(payment_success):
            #     print(f"Here's your {drink_menu.name}! Enjoy!")
            # else:
            #     print("Insufficient amount paid..")
        else:
            print("Sorry! Not enough ingredients.")

