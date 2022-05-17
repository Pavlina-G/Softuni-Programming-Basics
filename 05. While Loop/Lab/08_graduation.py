name = input()
grades = 1
sum_grade = 0.00
excluded = 0


while grades <= 12:
    grade = float(input())

    if grade < 4.00:
        excluded += 1
        if excluded > 1:
            print(f"{name} has been excluded at {grades} grade")
            break
            continue
    else:
        sum_grade += grade
        grades += 1
average = sum_grade / 12
if grades >= 12:
    print(f"{name} graduated. Average grade: {average:.2f}")



