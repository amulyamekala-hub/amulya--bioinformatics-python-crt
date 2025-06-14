num = int(input("Enter the value of num: "))

for i in range(1, num + 1):
    print(f"\nReversed multiplication table of {i}:")
    for j in range(10, 0, -1):
        print(f"{i} x {j} = {i * j}")
