fruit = input()
day_of_week = input()
quantity = float(input())
cost = 0
condition = True

if day_of_week in "Monday" "Tuesday" "Wednesday" "Thursday" "Friday":
    if fruit == "banana":
        cost = quantity * 2.50
    elif fruit == "apple":
        cost = quantity * 1.20
    elif fruit == "orange":
        cost = quantity * 0.85
    elif fruit == "grapefruit":
        cost = quantity * 1.45
    elif fruit == "kiwi":
        cost = quantity * 2.70
    elif fruit == "pineapple":
        cost = quantity * 5.50
    elif fruit == "grapes":
        cost = quantity * 3.85
    else:
        condition = False
elif day_of_week in "Saturday" "Sunday":
    if fruit == "banana":
        cost = quantity * 2.70
    elif fruit == "apple":
        cost = quantity * 1.25
    elif fruit == "orange":
        cost = quantity * 0.90
    elif fruit == "grapefruit":
        cost = quantity * 1.60
    elif fruit == "kiwi":
        cost = quantity * 3.00
    elif fruit == "pineapple":
        cost = quantity * 5.60
    elif fruit == "grapes":
        cost = quantity * 4.20
    else:
        condition = False
else:
    condition = False

if condition:
    print(f'{cost:.2f}')
else:
    print('error')


