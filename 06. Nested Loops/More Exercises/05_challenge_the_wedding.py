man_number = int(input())
woman_number = int(input())
max_table = int(input())

for man in range(1, man_number + 1):
    for woman in range(1, woman_number + 1):
        max_table -= 1
        if max_table < 0:
            break
        else:
            print(f"({man} <-> {woman})", end = " ")
