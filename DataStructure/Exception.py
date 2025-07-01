''' 
try:
    '''

Num=100
print("Program Execution Begins")
print(Num)
try:
   print(Num/0)
except ZeroDivisionError:
   print("Dividing with zero Gives an Infinate value")
print("Program Execution Ends")



#finally
Num=100
print("Program Execution Begins")
print(Num)
try:
   print(Num/0)
finally:
   print("Dividing with zero Gives an Infinate value")
print("Program Execution Ends")