n = int(input("Enter the no.of.words that you would like to find :"))
List=['Marker','Water','Hair','Blue','Free','Sun','Wheel']
Tuple=('Pen','Bottle','Band','color','Fire','day','chair')
for i in range(n):
    word=input("Enter the word:")
    index=List.index(word)
    print(f"{word}-{Tuple[index]}")