command = input()

secret_word = ""
counter_n = 0
counter_o = 0
counter_c = 0
word = ""

while command != "End":
    if command >= "a" and command <= "z" or command >= "A" and command <= "Z":
        if command == "n" and counter_n == 0:
            counter_n += 1
        elif command == "o" and counter_o == 0:
            counter_o += 1
        elif command == "c" and counter_c == 0:
            counter_c += 1
        else:
            word += command
        if counter_c == 1 and counter_o == 1 and counter_n == 1:
            secret_word += word + " "
            counter_c = 0
            counter_n = 0
            counter_o = 0
            word = ""

    command = input()
print(secret_word)


