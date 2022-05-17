first_number = int(input())
second_number = int(input())

for number in range(first_number,second_number + 1):
    odd_sum = 0
    even_sum = 0
    number_str = str(number)
    for index, digit in enumerate(number_str): # index = 0,1,2,3...,digit = value of number's numeral
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=" ")

