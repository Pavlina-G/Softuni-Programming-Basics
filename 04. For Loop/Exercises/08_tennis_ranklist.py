tennis_tournament_number = int(input())
start_points = int(input())
total_points = 0
current_points = 0
won_tournament = 0

for i in range (tennis_tournament_number):
    tournament_stage = input()
    if tournament_stage == "W":
        current_points += 2000
        won_tournament += 1
    elif tournament_stage == "F":
        current_points += 1200
    elif tournament_stage == "SF":
        current_points += 720
total_points = current_points + start_points
average_points = current_points / tennis_tournament_number
percent_won = won_tournament / tennis_tournament_number * 100
print(f"Final points: {total_points}")
print(f"Average points: {int(average_points)}")
print(f"{percent_won:.2f}%")
