game_number = int(input())
starting_points = int(input())
win_game_counter = 0
final_points = 0
current_points = 0

for game in range(1,game_number + 1):
    game_stage = input()
    if game_stage == "W":
        win_game_counter += 1
        current_points += 2000
    elif game_stage == "F":
        current_points += 1200
    elif game_stage == "SF":
        current_points += 720
final_points += starting_points + current_points
average_points = current_points / game_number

print(f"Final points: {final_points}")
print(f"Average points: {int(average_points)}")
print(f"{win_game_counter / game_number * 100:.2f}%")
