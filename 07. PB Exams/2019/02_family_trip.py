budget = float(input())
nights= int(input())
price_per_night= float(input())
total_nights = 0
other_expenses = int(input())
total_cost = 0
other_expenses = other_expenses / 100 * budget
if nights > 7:
    price_per_night *= 0.95
total_nights = price_per_night * nights
total_cost = total_nights + other_expenses
difference = abs(total_cost - budget)
if total_cost <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")