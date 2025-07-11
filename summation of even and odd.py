num = int(input("Enter an integer number: "))

# Convert to absolute value to handle negative numbers
num = abs(num)

even_sum = 0
odd_sum = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    num = num // 10

print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)
