sea_trip_number = int(input())
mountain_trip_number = int(input())

sea_price = 680
mountain_price = 499
profit = 0
all_sold = False

while True:
    command = input()
    if command == "Stop":
        break

    elif command == "sea":
        sea_trip_number -= 1
        if sea_trip_number >= 0:
            profit += sea_price

    elif command == "mountain":
        mountain_trip_number -= 1
        if mountain_trip_number >= 0:
            profit += mountain_price

    if sea_trip_number <= 0 and mountain_trip_number <= 0:
        all_sold = True
        break

if all_sold:
    print(f"Good job! Everything is sold.")
print(f"Profit: {profit} leva.")