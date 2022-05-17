percentage_fat = int(input())
percentage_protein = int(input())
percentage_carbohydrates = int(input())
total_calories = int(input())
percentage_water = int(input())

gram_fat_cal = 9
gram_protein_cal = 4
gram_carbohydrates_cal = 4

total_grams_fat = (percentage_fat / 100 * total_calories) / gram_fat_cal
total_grams_protein = (percentage_protein / 100 * total_calories) / gram_protein_cal
total_grams_carbohydrates = (percentage_carbohydrates / 100 * total_calories) / gram_carbohydrates_cal

total_food_grams = total_grams_protein + total_grams_carbohydrates + total_grams_fat
calories_per_gram = total_calories / total_food_grams
average_calories = calories_per_gram - calories_per_gram * percentage_water / 100

print(f"{average_calories:.4f}")
