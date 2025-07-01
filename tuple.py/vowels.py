#write apython program to read a string as input from the suer and print the count of 
    #1.uppercase vowels
    #2.lower case vowels
   # 3.upper consonents
   #4.lower case consonents
str=input("enter the string :")
U_Vowels,L_Vowels,U_consonants,L_consonants=0,0,0,0
for ch in str:
    if(ch.isalpha()and ch.isupper()):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_consonants+=1
    if(ch.isalpha() and ch.islower()):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_consonants+=1
print(f"Lower case Vowel count: {L_Vowels}")
print(f"Lower case Vowel count: {U_Vowels}")
print(f"Lower case Vowel count: {L_consonants}")
print(f"Lower case Vowel count: {U_consonants}")


#PROGRAM

str=input("enter the string :")
U_Vowels,L_Vowels,U_consonants,L_consonants=0,0,0,0
for ch in str:
    if(ch>='A'and ch<='Z'):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_consonants+=1
    if(ch>='a' and ch<='z'):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_consonants+=1
print(f"Lower case Vowel count: {L_Vowels}")
print(f"Lower case Vowel count: {U_Vowels}")
print(f"Lower case Vowel count: {L_consonants}")
print(f"Lower case Vowel count: {U_consonants}")




