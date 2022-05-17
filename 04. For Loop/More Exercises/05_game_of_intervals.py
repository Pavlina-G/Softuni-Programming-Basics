number_of_moves =  int(input())
points = 0
total_points = 0
total_numbers =0
number_to9 = 0
number_to19 = 0
number_to29 = 0
number_to39 = 0
number_to50 = 0
invalid_number = 0

for num in range(number_of_moves):
    number = int(input())
    if number < 0 or number > 50:
        points /= 2
        invalid_number += 1
    elif 0 <= number < 10:
        points += (0.20 * number)
        number_to9 += 1
    elif 10 <= number < 20:
        points += (0.30 * number)
        number_to19 += 1
    elif 20 <= number < 30:
        points += (0.40 * number)
        number_to29 += 1
    elif 30 <= number < 40:
        points += 50
        number_to39 += 1
    elif 40 <= number <= 50:
        points += 100
        number_to50 += 1

total_points += points
total_numbers = invalid_number + number_to50 + number_to39 + \
                number_to29 + number_to19 + number_to9
print(f"{total_points:.2f}")
print(f"From 0 to 9: {number_to9 / total_numbers * 100:.2f}%")
print(f"From 10 to 19: {number_to19 / total_numbers * 100:.2f}%")
print(f"From 20 to 29: {number_to29 / total_numbers * 100:.2f}%")
print(f"From 30 to 39: {number_to39 / total_numbers * 100:.2f}%")
print(f"From 40 to 50: {number_to50 / total_numbers * 100:.2f}%")
print(f"Invalid numbers: {invalid_number / total_numbers * 100:.2f}%")