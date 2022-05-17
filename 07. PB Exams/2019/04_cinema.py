capacity = int(input())
command = input()
price = 5
total_income = 0
cinema_is_full = False

while command != "Movie time!":
    people = int(command)
    capacity -= people
    income = 0
    if capacity < 0:
        cinema_is_full= True
        break
    income = people * price
    if people % 3 == 0:
        income -= 5

    total_income += income

    command = input()

if cinema_is_full:
    print(f"The cinema is full.")
else:
    print(f"There are {abs(capacity)} seats left in the cinema.")
print(f"Cinema income - {total_income} lv.")





