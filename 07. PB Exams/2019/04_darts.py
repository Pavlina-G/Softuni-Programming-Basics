name = input()
points = 301
good_shot = 0
bad_shot = 0
game_won = True

while points != 0:
    command = input()
    if command == "Retire":
        game_won = False
        break

    current_points = int(input())

    if command == "Single":
        if current_points <= points and points > 0:
            points -= current_points
            good_shot += 1
        else:
            bad_shot += 1

    elif command == "Double":
        current_points *= 2
        if current_points <= points and points > 0:
            points -= current_points
            good_shot += 1
        else:
            bad_shot += 1

    elif command == "Triple":
        current_points *= 3
        if current_points <= points and points > 0:
            points -= current_points
            good_shot += 1
        else:
            bad_shot += 1

if not game_won:
    print(f"{name} retired after {bad_shot} unsuccessful shots.")
else:
    print(f"{name} won the leg with {good_shot} shots.")
