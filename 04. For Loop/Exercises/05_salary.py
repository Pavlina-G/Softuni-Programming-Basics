tabs_numbers = int(input())
salary = float(input())
fine = 0

for tab in range(tabs_numbers):
    open_tab = input()
    if open_tab == "Facebook":
        fine = 150
    elif open_tab == "Instagram":
        fine = 100
    elif open_tab == "Reddit":
        fine = 50
    else:
        fine = 0
    salary -= fine
    if salary <= 0:
        print(f"You have lost your salary.")
        break
if salary > 0:
    print(int(salary))





