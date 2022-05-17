number1_end = int(input()) #not working for 444
number2_end = int(input())
number3_end = int(input())
prime_number = True
for num1 in range(2, number1_end + 1, 2):
    for num2 in range(2, number2_end + 1):
        if num2 > 1:
            for i in range(2, num2):
                if(num2 % i) == 0:
                    prime_number = False
                    break
                else:
                    prime_number = True
        for num3 in range(2, number3_end + 1, 2):
            if prime_number:
                print(f"{num1} {num2} {num3}")


