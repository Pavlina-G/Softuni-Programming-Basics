command = input()
desi_win = False
win_game_counter = 0
lost_game_counter = 0
all_game_counter = 0

while command != "End of tournaments":
    game_number = int(input())
    all_game_counter += game_number

    total_desi_score = 0
    total_other_score = 0
    difference = 0

    for game in range(1, game_number + 1):
        desi_score = int(input())
        other_score = int(input())
        difference = 0

        difference = abs(desi_score - other_score)

        if other_score < desi_score:
            win_game_counter += 1
            print(f"Game {game} of tournament {command}: win with {difference} points.")
        else:
            lost_game_counter += 1
            print(f"Game {game} of tournament {command}: lost with {difference} points.")

    command = input()
print(f"{win_game_counter / all_game_counter * 100:.2f}% matches win")
print(f"{lost_game_counter / all_game_counter * 100:.2f}% matches lost")