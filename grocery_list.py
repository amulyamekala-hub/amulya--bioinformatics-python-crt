print("*************** MENU ***************")
List=['rice','salt','green gram','jaggery','mustard','maize']
price= (1400,120,140,100,150,110)
print(List)
Requried_items=int(input("Enter the number of groceries requries: "))
i=1
total_bill=0
while(i<=Requried_items):
    item= input(" Enter the item requried: ")
    if item in List:
        quantity=int(input("number of items: "))
        index= List.index(item)
        bill=price[index]*quantity
        print("CONFRIM ORDER")
        if (bill>0):
            bill+bill*(25/100)
            print(bill)
            total_bill+=bill
    else:
        print("order somethind else")
    i+=1
phone=int(input("Enter phone number : "))
count=0
while(phone!=0):
    phone=phone//10
    count+=1
if(count==10):
    print("THANK YOU")
else:
    print("wrong number")
feedback=input("Give feedback :")
tip= int(input("Enter the timp amount : "))
total_bill+=tip
print("the total bill is :",total_bill)