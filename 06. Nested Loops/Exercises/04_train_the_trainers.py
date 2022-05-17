average_score = 0
score_counter = 0
all_scores = 0

people_in_jury = int(input())
presentation_name = input()

while presentation_name != "Finish":
    total_score = 0
    for people in range(1,people_in_jury+1):
        current_score = float(input())
        score_counter += 1
        total_score += current_score
    average_score = total_score / people_in_jury
    all_scores += total_score
    print(f"{presentation_name} - {average_score:.2f}.")
    presentation_name = input()
print(f"Student's final assessment is {all_scores / score_counter:.2f}.")
