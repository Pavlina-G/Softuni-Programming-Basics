command = input()
total_tickets_counter = 0
student_tickets_counter = 0
standard_tickets_counter = 0
kid_tickets_counter = 0


while command != "Finish":
    movie_name = command
    free_space = int(input())
    total_space = free_space
    sold_tickets = 0
    while free_space > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter += 1
        elif ticket_type == "standard":
            standard_tickets_counter += 1
        elif ticket_type == "kid": #else:
            kid_tickets_counter += 1
        free_space -= 1
        sold_tickets += 1
        total_tickets_counter += 1
    print(f"{movie_name} - {sold_tickets / total_space * 100:.2f}% full.")
    command = input()

print(f"Total tickets: {total_tickets_counter}")
print(f"{student_tickets_counter / total_tickets_counter * 100:.2f}% student tickets.")
print(f"{standard_tickets_counter / total_tickets_counter * 100:.2f}% standard tickets.")
print(f"{kid_tickets_counter / total_tickets_counter* 100:.2f}% kids tickets.")
