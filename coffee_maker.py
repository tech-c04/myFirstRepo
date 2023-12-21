import coffee_maker_details
machine_on = True
while machine_on == True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print(coffee_maker_details.resources)
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        ingr_names = list(coffee_maker_details.MENU[order]["ingredients"].keys())
        for ingr in ingr_names:
            if coffee_maker_details.resources[ingr] < coffee_maker_details.MENU[order]["ingredients"][ingr]:
                print(f"Oops! {ingr} is insufficient! Money refunded.")
                break
            continue
        for ingr in ingr_names:
            if coffee_maker_details.resources[ingr] >= coffee_maker_details.MENU[order]["ingredients"][ingr]:
                coffee_maker_details.resources[ingr] = coffee_maker_details.resources[ingr] - coffee_maker_details.MENU[order]["ingredients"][ingr]
        print("Please insert coins")
        quarters = int(input("How many Quarters?: "))
        dimes = int(input("How many Dimes?: "))
        nickles = int(input("How many Nickles?: "))
        pennies = int(input("How many Pennies?: "))
        inserted_dollar_amt = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
        # Accessing elements in nested dictionary
        price = coffee_maker_details.MENU[order]["cost"]
        change = inserted_dollar_amt - price
        if change > 0:
            print(f"Here is ${change} in change. Enjoy!")
        elif change < 0:
            print("Sorry that's not enough money. Money refunded!")
        if change == 0:
            print(f"Here's your {order}. Enjoy!")  




# Take input from user 
# If resources for input are not sufficient, give alert
# Else ask to insert coins in all denominations
# Conversion of denominations
# Subtract price from money given and return change
# Subtract resources used from resources left 