days = int(input())
total_money = 0
win_days = 0
lost_days = 0

for day in range(1, days + 1):
    money = 0
    win_game_counter = 0
    lost_game_counter = 0
    sport = input()

    while sport != "Finish":
        end_game = input()
        if end_game == "win":
            win_game_counter += 1
            money += 20
        elif end_game == "lose":
            lost_game_counter += 1
        sport = input()

        if sport == "Finish":
            if win_game_counter > lost_game_counter:
                win_days += 1
                money *= 1.10
                total_money += money
            else:
                lost_days += 1
                total_money += money

if win_days > lost_days:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")

