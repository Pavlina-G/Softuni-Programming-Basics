first_letter = input()
last_letter = input()
skipped_letter = input()
counter = 0

chars = range(ord(first_letter), ord(last_letter) + 1)
for i in chars:
    if chr(i) == skipped_letter:
        continue
    for j in chars:
        if chr(j) == skipped_letter:
            continue
        for k in chars:
            if chr(k) == skipped_letter:
                continue
            counter += 1
            print(chr(i) + chr(j) + chr(k), end = " ")
print(counter)
