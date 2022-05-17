number = input()

first_number = number[2]
second_number = number[1]
third_number = number[0]
result = 0

for num1 in range(1,int(first_number) + 1):
    for num2 in range(1,int(second_number) + 1):
        for num3 in range(1,int(third_number) + 1):
            result = num1 * num2 * num3
            print(f"{num1} * {num2} * {num3} = {result};")