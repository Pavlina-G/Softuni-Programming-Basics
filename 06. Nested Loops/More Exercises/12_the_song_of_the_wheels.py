number = int(input())
condition = False
counter = 0
password1 = ""
password = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a * b + c * d == number:
                    counter += 1
                    condition = True
                    print(f"{a}{b}{c}{d}", end=" ")

                    if counter == 4:
                        password = True
                        password1 = f"{a}{b}{c}{d}"
print()
if password:
    print(f"Password: {password1}")
if not condition or not password:
    print("No!")









