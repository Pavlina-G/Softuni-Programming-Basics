num1 =int(input())
num2 =int(input())
operator = input()
result = 0
type_of_result = ""

if operator == "+":
    result = num1 + num2
    if result % 2 == 0:
        type_of_result = 'even'
    else:
        type_of_result = 'odd'
    print(f"{num1} + {num2} = {result} - {type_of_result}")
elif operator == "-":
    result = num1 - num2
    if result % 2 == 0:
        type_of_result = 'even'
    else:
        type_of_result = 'odd'
    print(f"{num1} - {num2} = {result} - {type_of_result}")
elif operator == "*":
    result = num1 * num2
    if result % 2 == 0:
        type_of_result = "even"
    else:
        type_of_result = "odd"
    print(f"{num1} * {num2} = {result} - {type_of_result}")

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
    else:
        print(f"Cannot divide {num1} by zero")

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print(f"Cannot divide {num1} by zero")


