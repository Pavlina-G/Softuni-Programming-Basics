number_of_days = int(input())
total_food = float(input())
biscuits = 0
total_biscuits =0
total_eaten_food = 0
total_eaten_dog_food = 0
total_eaten_cat_food = 0
days_count = 0

for days in range(number_of_days):
    eaten_dog_food = int(input())
    eaten_cat_food = int(input())
    total_eaten_dog_food += eaten_dog_food
    total_eaten_cat_food += eaten_cat_food
    days += 1 #count days
    if days % 3 == 0:
        biscuits += 0.10 * (eaten_dog_food + eaten_cat_food)

total_biscuits += round(biscuits)
total_eaten_food += total_eaten_cat_food + total_eaten_dog_food

percent_eaten_food = total_eaten_food / total_food * 100
percent_eaten_dog_food = total_eaten_dog_food / total_eaten_food * 100
percent_eaten_cat_food =  total_eaten_cat_food / total_eaten_food * 100

print(f"Total eaten biscuits: {total_biscuits}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_dog_food:.2f}% eaten from the dog.")
print(f"{percent_eaten_cat_food:.2f}% eaten from the cat.")
