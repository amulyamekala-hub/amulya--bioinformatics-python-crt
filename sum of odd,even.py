numbers = [3,-2,-5,6,7,0,8,-1]
neg_sum = 0
pos_even_sum = 0
pos_odd_sum = 0
i = 0
while i < len(numbers):
    n = numbers[i]
    if n < 0:
        neg_sum += n
    elif n > 0 and n % 2 == 0:
        pos_even_sum += n
    elif n > 0 and n % 2 != 0:
        pos_odd_sum += n
    i +=1
print("sum of negative numbers:",neg_sum)
print("sum of positive even numbers:",pos_even_sum)
print("sum of positive odd numbers:",pos_odd_sum)