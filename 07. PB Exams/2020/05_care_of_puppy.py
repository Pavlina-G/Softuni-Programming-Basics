total_food_kg = int(input())
total_food_gr = int(total_food_kg * 1000)
command = input()
food_is_enough = True

while command != "Adopted":
    dog_food_gr = int(command)
    total_food_gr -= dog_food_gr
    if total_food_gr < 0:
        food_is_enough = False
    command = input()

if not food_is_enough:
    print(f"Food is not enough. You need {abs(total_food_gr)} grams more.")
else:
    print(f"Food is enough! Leftovers: {total_food_gr} grams.")



