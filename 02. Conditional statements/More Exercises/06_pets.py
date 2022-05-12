from math import floor, ceil

days = int(input())
food_kg = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

total_food = 0
total_food = (dog_food_per_day + cat_food_per_day + turtle_food_per_day) * days
difference = abs (food_kg - total_food)

if total_food <= food_kg:
    print(f'{floor(difference)} kilos of food left.')
else:
    print(f'{ceil(difference)} more kilos of food are needed.')