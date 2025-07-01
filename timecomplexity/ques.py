"""write a python program to print alpabets from a to z"""
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch+1)
ch = 65
Alphabets(ch)
print("-------------------------")
#revrse
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch-1)
ch = 90
Alphabets(ch)
  