logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""





def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div (a, b):
    return a / b

def remainder (a, b):
    remainder = a % b
    return remainder

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": div,
    "%": remainder
}

# if operation == "+":
#     print(add(first_num, last_num))
# elif operation == "-":
#     print(sub(first_num, last_num))
# elif operation == "*":
#     print(multiply(first_num, last_num))
# elif operation == "/":
#     print(div(first_num, last_num))
# elif operation == "%":
#     print(remainder(first_num, last_num))

def calculator():
    print(logo)
    should_accumulate = True
    first_num = float(input("What's your first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an Operation: ")
        last_num = float(input("What's the next number?: "))
        ans = operations[operation_symbol](first_num, last_num)
        print(f"{first_num} {operation_symbol} {last_num} = {ans}")

        choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_num = ans
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
