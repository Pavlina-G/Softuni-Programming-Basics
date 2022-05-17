coin_1 = int(input())
coin_2 = int(input())
coin_5 = int(input())
amount = int(input())

for lv1 in range(coin_1 + 1):
    for lv2 in range(coin_2 + 1):
        for lv5 in range(coin_5 + 1):
            if (lv1 * 1 + lv2 * 2 + lv5 * 5) == amount:
                print(f"{lv1} * 1 lv. + {lv2} * 2 lv. + {lv5} * 5 lv. = {amount} lv.")


