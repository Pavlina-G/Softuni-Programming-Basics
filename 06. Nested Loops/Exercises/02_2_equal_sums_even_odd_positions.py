first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    number_str = str(number)
    odd_sum = 0
    even_sum = 0
    for index in range(len(number_str)):
        digit = int(number_str[index])
        if index % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit
    if odd_sum == even_sum:
        print(number, end = " ")