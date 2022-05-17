days = int(input())
total_rakia = 0
total_degree = 0

for day in range(1, days + 1):

    liter_rakia = float(input())
    degree = float(input())

    total_rakia += liter_rakia
    total_degree += degree * liter_rakia

average_degree = total_degree / total_rakia

print(f"Liter: {total_rakia:.2f}")
print(f"Degrees: {average_degree:.2f}")

if average_degree < 38:
    print(f"Not good, you should baking!")
elif average_degree <= 42:
    print(f"Super!")
else:
    print(f"Dilution with distilled water!")

