#Quick Sort
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
print(quick_sort([5, 3, 8, 6, 2]))
'''
arr=[50,80,30,20,15,10]
pivort=Arr[6//2] ---->
'''