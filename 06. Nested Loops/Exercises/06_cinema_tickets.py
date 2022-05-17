student_tickets_counter = 0
standard_tickets_counter = 0
kid_tickets_counter = 0
total_tickets_counter = 0
total_tickets = 0

movie_name = input()

while movie_name != "Finish":
    free_space = int(input())
    total_space = free_space
    total_tickets_counter = 0
    while free_space > 0:
        type_of_ticket = input()
        if type_of_ticket == "student":
            student_tickets_counter += 1
        elif type_of_ticket == "standard":
            standard_tickets_counter +=1
        elif type_of_ticket == "kid":
            kid_tickets_counter += 1
        elif type_of_ticket == "End":
            break
        free_space -= 1
        total_tickets_counter += 1
        total_tickets += 1
    print(f"{movie_name} - {total_tickets_counter / total_space * 100:.2f}% full.")
    movie_name = input()
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_counter / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets_counter / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets_counter / total_tickets * 100:.2f}% kids tickets.")






