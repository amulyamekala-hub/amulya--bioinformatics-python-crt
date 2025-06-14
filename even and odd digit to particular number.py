num = int(input("Enter an integer number: "))
# Convert to absolute value to handle negative numbers
num = abs(num)
even_count = 0
odd_count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num = num // 10
print("Number of even digits:", even_count)
print("Number of odd digits:", odd_count)
