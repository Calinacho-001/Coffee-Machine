import os
from simple_colors import red, cyan, yellow, green, blue  # type: ignore


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 5000,
    "milk": 5000,
    "coffee": 5000,
}

money = {
    "value": 0,
}

_quarter = 0
_dime = 0
_nickle = 0
_pennie = 0

def resource_check(order_ingridients):
    is_enough = True
    for item in order_ingridients:
        if order_ingridients[item] >= resources[item]:
            print(red("Not enough ingridients."))
            is_enough = False
    return is_enough


def process_coins(quarter, dime, nickle, pennie):
    print(cyan("~~ Please insert coins ~~"))
    try:
        inserted_quarters = int(input("How many quarters?: "))
        inserted_dimes = int(input("How many dimes?: "))
        inserted_nickles = int(input("How many nickles?: "))
        inserted_pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Not a coin, please enter the number ammount of coins used.")
    
    total_quarters = inserted_quarters + quarter
    total_dimes = inserted_dimes + dime
    total_nickles = inserted_nickles + nickle
    total_pennies = inserted_pennies + pennie
    total = (total_quarters * 0.25) + (total_dimes * 0.10) + (total_nickles * 0.05) + (total_pennies * 0.01)
    return total


def is_payment_complete(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(yellow(f"Change left is ${change}. Please pick up you change."))
        money["value"] += drink_cost
        return True
    else:
        print(red("Sorry that's not enough money. Money refunded."))
        return False


def make_coffee(drink_name, drink_ingridients):
    for item in drink_ingridients:
        resources[item] -= drink_ingridients[item]
    print(blue(f"Here is your order. ☕"))


def coffee_machine():
    machine_is_on = True
    while machine_is_on:
        choice = input("\nWhat would you like?\n"
                        "1. Espresso ($1.5):\n"
                        "2. Latte ($2.5):\n"
                        "3. Cappuccino ($3.0):\n"
                        "4. Report:\n"
                        "5. Help:\n"
                        "6. Turn Off Machine:\n"
                        ">>> ").lower()
        clear_screen()
        if choice in ["6", "off"]:
            machine_is_on = False
            print(red("Coffee machine powerd off."))

        elif choice in ["5", "help"]:
            print(cyan("~~~ Guide on how to use the coffee machine ~~~\n"))
            print(yellow("- The accepted currency is only coins(e.g. quarters, dimes, nickles and pennies).\n"
                         "              ---Quarters = 0.25$\n"
                         "              ---Dimes = 0.10$\n"
                         "              ---Nickles = 0.05$\n"
                         "              ---Pennies = 0.01$\n"
                  "- To select the desired coffee, type the number of the option or the name of the coffee type.\n"
                  "- If the machine is out of ingridients, please contact the administrator.\n"
                  "- To print a report of the avaialble ingridients inside the machine, press 4 or type report.\n"
                  "- To add ingridients to the machine, contact the administrator for instructions."))

        elif choice in ["4", "report"]:
            print(f"Water: {resources['water']}ml.")
            print(f"Milk: {resources['milk']}ml.")
            print(f"Coffee: {resources['coffee']}g.")
            print(f"Money: ${money['value']}.")

        elif choice in ["1", "espresso"]:
            drink = MENU["espresso"]
            if resource_check(drink["ingredients"]):
                payment = process_coins(_quarter, _dime, _nickle, _pennie )
                if is_payment_complete(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])

        elif choice in ["2", "latte"]:
            drink = MENU["latte"]
            if resource_check(drink["ingredients"]):
                payment = process_coins(_quarter, _dime, _nickle, _pennie )
                if is_payment_complete(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])

        elif choice in ["3", "cappuccino"]:
            drink = MENU["cappuccino"]
            if resource_check(drink["ingredients"]):
                payment = process_coins(_quarter, _dime, _nickle, _pennie )
                if is_payment_complete(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print(red("Not a valid option. Please choose from the options available."))
            
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear_screen()
    coffee_machine()
    

if __name__ == "__main__":
    main()