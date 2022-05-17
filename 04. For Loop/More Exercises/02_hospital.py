period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period + 1):
    number_of_patients = int(input())
    if day % 3 == 0: #Wednesday
        if untreated_patients > treated_patients:
            doctors += 1
    if doctors >= number_of_patients:
        treated_patients += number_of_patients
    else:
        treated_patients += doctors
        untreated_patients += (number_of_patients - doctors)

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
