num = input("Enter an integer number: ")
# Remove negative sign if present
num = num.lstrip('-')
zero_count = 0
for digit in num:
    if digit == '0':
        zero_count += 1
print("Number of 0s in the number:", zero_count)
