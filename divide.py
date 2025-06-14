num=[10,20,30,40,50]
divisor=5
if divisor == 0:
    print("cannot divide by zero.")
else:
    result = []
    i=0
    while i<len(num):
        result.append(num[i]/divisor)
        i += 1
print("resulting list:",result)
