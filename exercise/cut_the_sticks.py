'''
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.
Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left.

Example
arr = [1, 2, 3]

The shortest stick length is 1, so cut that length from the longer two and discard the pieces of length 1. Now the lengths are arr = [1, 2]. Again, the shortest stick is of length 1, so cut that amount from the longer stick and discard those pieces. There is only one stick left, arr = [1], so discard that stick. The number of sticks at each iteration are answer = [3, 2, 1].
'''

def cutTheSticks(arr):
    # Write your code here
    answer = []
    
    while arr:
        answer.append(len(arr))
        shortest_stick = min(arr)
        arr = [stick-shortest_stick for stick in arr if stick != shortest_stick]
    return answer

arr_first = [5,4,4,2,2,8]
arr_scnd = [1,2,3,4,3,3,2,1]

print(cutTheSticks(arr_first))
print(cutTheSticks(arr_scnd))