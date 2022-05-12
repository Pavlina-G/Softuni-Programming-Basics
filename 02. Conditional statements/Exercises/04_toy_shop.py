trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60
doll_price= 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

toys_num = puzzles + dolls + bears + minions + trucks
profit = (puzzles * puzzle_price) + (dolls * doll_price) + \
          (bears * bear_price) + (minion_price * minions) + (truck_price * trucks)

if toys_num >= 50:
    profit *= 0.75
    profit *= 0.9
else:
    profit *= 0.9
needed_money = abs(trip_price - profit)

if profit >= trip_price:
    print(f"Yes! {needed_money:.2f} lv left.")
else:
    print(f"Not enough money! {needed_money:.2f} lv needed.")