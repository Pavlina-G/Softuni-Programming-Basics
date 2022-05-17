command = input()
max_num = -99999999999999

while command != "Stop":
    number = int(command)
    if number > max_num:
        max_num = number
    command = input()
print(max_num)
