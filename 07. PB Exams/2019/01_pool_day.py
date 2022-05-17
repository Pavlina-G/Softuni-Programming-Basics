from math import ceil

people = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())
total_price = 0

entrance_fee = entrance_fee * people
sunbed_price = ceil(0.75 * people) * sunbed_price
umbrella_price = ceil(people / 2) * umbrella_price
total_price = entrance_fee + sunbed_price + umbrella_price
print(f"{total_price:.2f} lv.")