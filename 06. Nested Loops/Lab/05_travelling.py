destination = input()
total_amount = 0

while destination != "End":
    min_budget = float(input())
    while total_amount <= min_budget:
        amount = float(input())
        total_amount += amount
        if total_amount >= min_budget:
            print(f"Going to {destination}!")
            break
    destination = input()
    total_amount = 0

