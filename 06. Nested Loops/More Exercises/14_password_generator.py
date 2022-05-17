n = int(input())
l = int(input())
start3 = ord("a")
end3 = start3 + l

for symbol1 in range(1, n + 1):
    for symbol2 in range(1, n + 1):
        for symbol3 in range(start3, end3):
            for symbol4 in range(start3, end3):
                for symbol5 in range(1, n + 1):
                    if symbol1 < symbol5 and symbol2 < symbol5:
                        print(f"{symbol1}{symbol2}{chr(symbol3)}{chr(symbol4)}{symbol5}", end =" ")