command = input()
sum_prime_numbers = 0
sum_composite_numbers = 0

while command != "stop":
    current_num = int(command)
    if current_num < 0:
        print("Number is negative.")
        # command = input()
        # continue
    else:
        prime_number = True
        for number in range(2, current_num):
            if current_num % number == 0:
                prime_number = False
                break
        if prime_number:
            sum_prime_numbers += current_num
        else:
            sum_composite_numbers += current_num

    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_composite_numbers}")