number = int(input())
for current_number in range(1111,10000):
    special_number = True
    current_number_str = str(current_number)

    for current_digit in current_number_str:
    #     print(current_digit)
    # exit()
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            special_number = False
            break
    if special_number:
        print(current_number_str, end =" ")






