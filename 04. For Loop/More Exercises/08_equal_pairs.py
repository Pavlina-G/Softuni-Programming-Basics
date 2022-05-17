import sys
number_of_pairs = int(input())
first_sum = int(input()) + int(input())
max_difference = 0

for pair in range(2, number_of_pairs + 1):
    second_sum = int(input()) + int(input())

    if abs(first_sum - second_sum) > max_difference:
        max_difference = abs(first_sum - second_sum)
    else:
        first_sum = second_sum
if max_difference == 0:
    print(f"Yes, value={first_sum}")
else:
    print(f"No, maxdiff={max_difference}")