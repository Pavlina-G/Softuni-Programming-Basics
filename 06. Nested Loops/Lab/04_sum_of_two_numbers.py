start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination = 0
condition = False

for num1 in range(start_number, end_number + 1):
    for num2 in range(start_number, end_number + 1):
        combination += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{combination} ({num1} + {num2} = {magic_number})")
            condition = True
            break
    if condition:
        break
if not condition:
    print(f"{combination} combinations - neither equals {magic_number}")

