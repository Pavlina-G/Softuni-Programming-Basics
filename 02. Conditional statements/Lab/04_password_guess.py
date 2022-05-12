password = str(input())
if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print('Wrong password!')

# Second way
user_password = "s3cr3t!P@ssw0rd"
input_password = input()

if user_password == input_password:
    print("Welcome")
else:
    print('Wrong password!')
