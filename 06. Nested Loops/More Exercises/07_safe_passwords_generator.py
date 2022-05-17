a = int(input())
b = int(input())
counter = 0
max_combinations= int(input())
first_last_symbol = 35
second_before_last_symbol = 64

for middle_symbol_a in range(1, a + 1):
    for middle_symbol_b in range(1, b + 1):
        counter += 1
        if counter > max_combinations:
            break
        if first_last_symbol > 55:
            first_last_symbol = 35
        if second_before_last_symbol > 96:
            second_before_last_symbol = 64
        print(f"{chr(first_last_symbol)}{chr(second_before_last_symbol)}{middle_symbol_a}{middle_symbol_b}{chr(second_before_last_symbol)}{chr(first_last_symbol)}", end = "|")
        first_last_symbol += 1
        second_before_last_symbol += 1