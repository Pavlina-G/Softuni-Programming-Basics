walk_minutes = int(input())
walk_number = int(input())
cat_calories = int(input())

total_minutes = walk_minutes * walk_number
burned_calories = total_minutes * 5

if burned_calories >= (0.50 * cat_calories):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")