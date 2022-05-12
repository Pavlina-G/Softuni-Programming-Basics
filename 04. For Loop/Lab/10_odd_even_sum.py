number = int(input())
odd_sum = 0 
even_sum = 0

for i in range(number):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
difference = abs(odd_sum - even_sum)
if odd_sum == even_sum:
    print(f"Yes")
    print(f"Sum = {odd_sum}")
else:
    print(f"No")
    print(f"Diff = {difference}")
    
