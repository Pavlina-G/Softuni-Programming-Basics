state = input()
device = input()
max_score = 20

if state == "Russia":
    if device == "ribbon":
        difficulty = 9.1
        performance = 9.4
    elif device == "hoop":
        difficulty = 9.3
        performance = 9.8
    elif device == "rope":
        difficulty = 9.6
        performance = 9.0
elif state == "Bulgaria":
    if device == "ribbon":
        difficulty = 9.6
        performance = 9.4
    elif device == "hoop":
        difficulty = 9.55
        performance = 9.75
    elif device == "rope":
        difficulty = 9.5
        performance = 9.4

elif state == "Italy":
    if device == "ribbon":
        difficulty = 9.2
        performance = 9.5
    elif device == "hoop":
        difficulty = 9.45
        performance = 9.35
    elif device == "rope":
        difficulty = 9.7
        performance = 9.15

total_score = difficulty + performance
if total_score < max_score:
    percent = (max_score - total_score) / max_score * 100

print(f"The team of {state} get {total_score:.3f} on {device}.")
print(f"{percent:.2f}%")

