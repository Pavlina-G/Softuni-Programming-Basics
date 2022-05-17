command = input()
winner = ""
max_points = 0

while command != "Stop":
    name = command
    name_str = str(name)
    points = 0
    total_points = 0
    for digit in name_str:
        number = int(input())
        if number == ord(digit):
            points += 10
        else:
            points += 2
    total_points += points
    if total_points > max_points:
        max_points = total_points
        winner = name
    elif total_points == max_points:
        winner = name

    command = input()

print(f"The winner is {winner} with {max_points} points!")