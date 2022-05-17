football_team = input()
number_of_games = int(input())
total_score = 0
won_game = 0
equal_game = 0
lost_game = 0
winner = ""
total_games = 0

for game in range(number_of_games):
    game_result = input()
    if game_result == "W":
        total_score += 3
        won_game += 1
        winner = football_team
    elif game_result == "D":
        total_score += 1
        equal_game += 1
    elif game_result == "L":
        total_score += 0
        lost_game += 1
total_games += won_game + equal_game + lost_game
if number_of_games == 0:
    print(f"{football_team} hasn't played any games during this season.")
if total_games > 0:
    print(f"{football_team} has won {total_score} points during this season.")
    print(f"Total stats:")
    print(f"## W: {won_game}")
    print(f"## D: {equal_game}")
    print(f"## L: {lost_game}")
    print(f"Win rate: {won_game / total_games * 100:.2f}%")