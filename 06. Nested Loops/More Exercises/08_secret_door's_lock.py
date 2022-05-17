first_end = int(input())
second_end = int(input())
third_end= int(input())

for hundreds in range(2, first_end + 1, 2):
    for tens in range(2, second_end + 1):
        for units in range(2, third_end + 1, 2):
            if tens == 2 or tens == 3 or tens == 5 or tens == 7:
                print(f"{hundreds} {tens} {units}")