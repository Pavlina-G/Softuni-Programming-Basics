number = int(input())
counter = 1
number_printed = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end = " ")
        counter += 1 # counter = 1, after first for loop counter 1+1
        if counter > number:
            number_printed = True
            break
    if number_printed:
        break
    print()
