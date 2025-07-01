'''Problem:
You are given an array of integers representing student scores.
Your task is to sort the array in ascending order using a basic sorting algorithm (Bubble Sort/ Selection Sort/ Insertion Sort)
Input:
-----
An integer n (1<= n <=1000)- no.of.students
An array of n integers- the scores(0 <= score <=100)
Output:
------
Sorted array of scores in ascending order
---------------------
Input:5
Scores:[55,90,85,63,72] '''
def bubble_sort(scores):
    n = len(scores)
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
    return scores
n = 5
scores = [55, 90, 85, 63, 72]
sorted_scores = bubble_sort(scores)
print("Sorted Scores:", sorted_scores)

