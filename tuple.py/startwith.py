"""WAPP to take name as input from the user including prefix (Mr/Mrs)
print gender classification of name as male and female based on prefix"""
gender= input("Enter Your name along with prefix: ")
if gender.startswith('Mr'):
    print("Male")
else:
    print("Female")