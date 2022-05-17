from math import floor
number_balls = int(input())
points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0
total_points = 0

for ball in range(number_balls):
    colour = input()
    if colour == "red":
        red += 1
        points += 5
    elif colour == "orange":
        points += 10
        orange += 1
    elif colour == "yellow":
        yellow += 1
        points += 15
    elif colour == "white":
        white += 1
        points += 20
    elif colour == "black":
        black += 1
        points /= 2
    else:
        other += 1
        pass
total_points += points
print(f"Total points: {floor(total_points)}")
print(f"Points from red balls: {red}")
print(f"Points from orange balls: {orange}")
print(f"Points from yellow balls: {yellow}")
print(f"Points from white balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")
