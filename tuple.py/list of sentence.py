#write a python program to read a sentence as input from the user and print the list of words from the sentence
sentence="We are learning python"
List=sentence.split()
print(List)
#write a python program to read the string as input from the user
#reverse the string
#convert the string into lowecase
#conver the string into uppercase
#Convert the characters of string to lower case if it is in upper case & convert to uppercase if it is in l.c
#check if the string  is starting with the letter A
#print the count of the character A from the give string and replace all P to J
str=input("Enter the string : ")
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.startswith('p'))
print(str.count('p'))
str=str.lower()
print(str.replace('p','j'))
