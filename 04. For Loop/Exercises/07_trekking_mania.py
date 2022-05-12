group_number = int(input())
all_people = 0
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest =0

for group in range(group_number):
    people_number = int(input())
    if people_number < 6:
        musala += people_number
    elif people_number < 13:
        montblanc += people_number
    elif people_number < 26:
        kilimanjaro += people_number
    elif people_number < 41:
        k2 += people_number
    elif people_number > 40:
        everest += people_number
all_people = musala + montblanc + kilimanjaro + k2 + everest
percent_musala = musala / all_people * 100
percent_montblanc = montblanc / all_people * 100
percent_kilimanjaro = kilimanjaro / all_people * 100
percent_k2 = k2 / all_people * 100
percent_everest = everest / all_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_montblanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")





