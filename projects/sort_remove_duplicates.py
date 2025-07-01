'''Problem:
Given a list of integers that may contain duplicates.
sort the list in ascending order and remove all duplicates.

Input:
A List of integers arr with length n (1 _< n <1000)
Output:
Sorted list with unique elements only
-------------------------------------
Input: [4,2,2,8,4,6]
Output: [2,4,6,8]'''
def sort_unique(arr):
    return sorted(set(arr))
arr = [4, 2, 2, 8, 4, 6]
result = sort_unique(arr)
print("Output:", result)