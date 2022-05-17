failed_threshold = int(input())
count_bad_grades = 0
has_failed = False
average_score = 0
count_task = 0
last_task = ""

task_name = input()


while task_name != "Enough":
    score = int(input())
    if score <= 4:
        count_bad_grades += 1
        if failed_threshold <= count_bad_grades:
            has_failed = True
            break
    average_score += score
    count_task += 1
    last_task = task_name
    task_name = input()
average_score /= count_task
if has_failed:
    print(f"You need a break, {failed_threshold} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {count_task}")
    print(f"Last problem: {last_task}")
