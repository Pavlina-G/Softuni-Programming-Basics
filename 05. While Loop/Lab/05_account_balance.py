balance = 0

while True:
    amount = input()
    if amount == "NoMoreMoney":
        break
    # string --> in float()
    elif float(amount) < 0:
        print("Invalid operation!")
        break

    balance += float(amount)
    print(f"Increase: {float(amount):.2f}")
print(f"Total: {balance:.2f}")