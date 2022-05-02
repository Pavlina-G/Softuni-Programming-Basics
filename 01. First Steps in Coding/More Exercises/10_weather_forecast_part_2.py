degrees = float(input())
if 5 <= degrees < 12:
    print("Cold")
elif 12 <= degrees < 15:
    print("Cool")
elif 15 <= degrees <= 20 :
    print("Mild")
elif 20.1 <= degrees <= 25.9:
    print("Warm")
elif 26.00 <= degrees < 35.00:
    print("Hot")
elif degrees < 5 or degrees > 35:
    print("unknown")