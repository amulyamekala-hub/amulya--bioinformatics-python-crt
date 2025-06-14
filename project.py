Guest_List=[]
while(True):
    print("***********Menu****************")
    print("1.Add the Guest")
    print("2.Remove the Guest Who Can Cancels")
    print("3.Check if a Guest is Attending the party or not")
    print("4.View the Final Guest List")
    print("5.Exit")
    print("-----------------------------------")
    Choice=int(input("Enter Your choice :"))
    if(Choice>=1 and Choice<=5):
        if(Choice==1):
            GuestName=input("Enter the Guest Name :")
            Guest_List.append(GuestName)
            print(f"{GuestName} is Added te Guest List....!")
        elif(Choice==1):
            GuestName=input("Enter the Guest Name :")
            Guest_List.append(GuestName)
            print(F"{GuestName} is Added to Guest List....!")
        elif(Choice==2):
            CancelledGuest=input("Enter the Cancelled Guest Name :")
            if CancelledGuest in Guest_List:
                Guest_List.remove(CancelledGuest)
                print(f"{CancelledGuest} is removed to Guest List....!")
            else:
                print(f"{CancelledGuest} is not to Guest List....!")
        elif(Choice==3):
            CheckGuest=input("Enter the Guest Name to Check :")
            if CheckGuest in Guest_List:
                print(f"{CheckGuest} is Attending the Party.....!")
            else:
                print(f"{CheckGuest} is not Attending the Party.....!")
        elif(Choice==4):
            if (len(Guest_List)==0):
                print("Guest List is empty, enter the Guest Name.....!")
            else:
                Guest_List.sort()
                print("Here is your final Guest List....!")
                print(Guest_List)
        else:
            print("Enjoy the party.....!!")
            break
    else:
        print("Invalid-Input")




        
