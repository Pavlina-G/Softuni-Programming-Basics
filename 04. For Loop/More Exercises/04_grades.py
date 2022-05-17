students = int(input())
excellent = 0
very_good = 0
good = 0
fail = 0
current_grade = 0
total_grade = 0
average_grade = 0

for i in range(1, students + 1):
    grade = float(input())
    if 2 <= grade < 3:
        fail += 1
        current_grade += grade
    elif 3 <= grade < 4:
        good += 1
        current_grade += grade
    elif 4 <= grade < 5:
        very_good += 1
        current_grade += grade
    elif 5 <= grade:
        excellent += 1
        current_grade += grade
total_grade += current_grade

percent_fail = fail / students * 100
percent_good = good / students * 100
percent_very_good = very_good / students * 100
percent_excellent = excellent / students * 100

average_grade = total_grade / students

print(f"Top students: {percent_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percent_very_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_good:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {average_grade:.2f}")