"""WAPP to take name as input from the user including prefix (Mr/Mrs)
print gender classification of name as male and female based on prefix"""
gender=input("Enter name with prefix (ms/mr):")
if str.startswith('ms'):
    print('female')
else:
    print('male')

    