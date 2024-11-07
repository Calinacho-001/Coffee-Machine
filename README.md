# Coffee Machine Project

## Description

This is a simple coffee machine program built in Python that allows users to select from three different types of coffee drinks (Espresso, Latte, and Cappuccino), insert coins for payment, and receive their coffee orders. The machine tracks its available resources (water, milk, and coffee) and ensures that the user is charged correctly based on the selected drink. The user can also view the available ingredients and check the current balance of money in the machine.

## Features

- **Coffee Menu**: Espresso, Latte, and Cappuccino.
- **Resource Management**: Keeps track of ingredients (water, milk, and coffee).
- **Payment System**: The user can insert coins (quarters, dimes, nickels, pennies) to pay for the selected drink.
- **Report**: Displays the current resources in the machine and the accumulated money.
- **Help**: Provides a guide on how to use the machine and how to make a payment.
- **Turn Off Machine**: Option to turn off the coffee machine.

## Requirements

- Python 3.x
- `simple_colors` library for colored text output (install via `pip install simple_colors`).

## How to Use

1. **Start the Coffee Machine**:
   - Run the script and the coffee machine will start.
   
2. **Select a Coffee**:
   - You can choose one of the following coffee options by typing the corresponding number or coffee name:
     - **Espresso** ($1.50)
     - **Latte** ($2.50)
     - **Cappuccino** ($3.00)

3. **Insert Coins**:
   - The machine will prompt you to insert coins (quarters, dimes, nickels, pennies). The machine will calculate the total amount based on the inserted coins.

4. **Receive Coffee**:
   - If the payment is sufficient and the required ingredients are available, you will receive your coffee.

5. **Report**:
   - Type "report" or press "4" to see the current state of ingredients and accumulated money.

6. **Help**:
   - Type "help" or press "5" for a guide on how to use the machine.

7. **Turn Off Machine**:
   - Type "off" or press "6" to turn off the machine.

## Code Structure

### Global Variables:
- `MENU`: Contains the coffee types, their ingredients, and costs.
- `resources`: Tracks the available ingredients (water, milk, coffee).
- `money`: Stores the accumulated money from sales.
- `_quarter`, `_dime`, `_nickle`, `_pennie`: Variables to keep track of coins inserted by the user.

### Functions:
- `resource_check(order_ingridients)`: Checks if there are enough ingredients to fulfill the order.
- `process_coins(quarter, dime, nickle, pennie)`: Processes the coins inserted by the user.
- `is_payment_complete(money_received, drink_cost)`: Verifies if the user has inserted enough money for the selected drink.
- `make_coffee(drink_name, drink_ingridients)`: Updates resources and serves the coffee.
- `coffee_machine()`: Main logic for interacting with the user (menu options and decisions).
- `clear_screen()`: Clears the console screen (works on both Windows and Unix systems).
- `main()`: Starts the coffee machine program.

## Error Handling

- If you try to select a drink when there aren't enough ingredients, the machine will notify you.
- If the inserted amount of coins is insufficient, the machine will notify you and refund the money.

## Credits

This project was created as part of a learning exercise in Python programming. It demonstrates basic concepts such as conditionals, loops, functions, and user input handling.

---

Happy brewing! ☕