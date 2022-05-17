group_numbers = int(input())
musala = 0
montblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
all_people = 0
for g in range(group_numbers):
    number_of_people = int(input())
    if number_of_people < 6:
        musala += number_of_people
    elif 6 <= number_of_people < 13:
        montblan += number_of_people
    elif 13 <= number_of_people < 26:
        kilimanjaro += number_of_people
    elif 26 <= number_of_people < 41:
        k2 += number_of_people
    elif 41 <= number_of_people:
        everest += number_of_people

all_people += musala + montblan + kilimanjaro + k2 + everest
percent_musala = musala / all_people * 100
percent_montblan = montblan / all_people * 100
percent_kilimanjaro = kilimanjaro / all_people * 100
percent_k2 = k2 / all_people * 100
percent_everest = everest / all_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_montblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")