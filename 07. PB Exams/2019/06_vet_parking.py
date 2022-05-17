days = int(input())
hours = int(input())
total_cost = 0

for day in range(1, days + 1):
    cost = 0
    for hour in range(1,hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        cost += price

    total_cost += cost
    print(f"Day: {day} - {cost:.2f} leva")

print(f"Total: {total_cost:.2f} leva")