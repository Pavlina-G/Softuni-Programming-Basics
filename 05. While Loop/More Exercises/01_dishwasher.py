dishwashing_detergent = int(input())
detergent_ml = dishwashing_detergent * 750
command = input()
counter_dishes = 0
plates_number =0
pots_number = 0
is_detergent_empty = False

while command != "End":
    number_of_dishes = int(command)
    counter_dishes += 1
    if counter_dishes % 3 == 0:
        detergent_ml -= number_of_dishes * 15
        pots_number += number_of_dishes
    else:
        detergent_ml -= number_of_dishes * 5
        plates_number += number_of_dishes
    if detergent_ml < 0:
        is_detergent_empty = True
        break
    command = input()

if is_detergent_empty:
    print(f"Not enough detergent, {abs(int(detergent_ml))} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{plates_number} dishes and {pots_number} pots were washed.")
    print(f"Leftover detergent {int(detergent_ml)} ml.")
    
