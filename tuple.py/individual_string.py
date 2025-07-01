# Read string input from the user
input_string = input("Enter a string: ")
# Convert string to list of characters
char_list = [ch for ch in input_string]
print("List of characters:", char_list)
# 1. Find the length of the string without using built-in functions
length = 0
for _ in char_list:
    length += 1
print("Length of string:", length)
# 2. Find the minimum element in the list (ASCII comparison), without using min()
min_char = char_list[0]
for ch in char_list[1:]:
    if ch < min_char:
        min_char = ch
print("Minimum character in list:", min_char)
# 3. Count the number of spaces in the string without using built-in methods
space_count = 0
for ch in char_list:
    if ch == ' ':
        space_count += 1
print("Number of spaces in the string:", space_count)
  