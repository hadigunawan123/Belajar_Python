'''
John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

Example:
a = [3, 4, 5]
k = 2
queries = [1, 2]

Here k is the number of rotations on a, and queries holds the list of indices to report. First we perform the two rotations: [3, 4, 5] -> [5, 3, 4] -> [4, 5, 3]

Now return the values from the zero-based indices  and  as indicated in the  array.
a[1] = 5
a[2] = 3

Function Description

Complete the circularArrayRotation function in the editor below.

circularArrayRotation has the following parameter(s):

int a[n]: the array to rotate
int k: the rotation count
int queries[1]: the indices to report
Returns

int[q]: the values in the rotated a as requested in m
'''

def circularArrayRotation(a, k, queries):
    # Write your code here
    result = []

    k = k % len(a)
    a = a[-k:] + a[:-k]
    for i in queries:
        result.append(a[i]) #bisa juga pake list compre: return [a[i] for i in queries]
    return result

a1, a2 = [3,4,5,6], [1,2,3]
k1, k2 = 2, 3
queries1, queries2 = [0, 2], [1, 2]
print(circularArrayRotation(a1, k1, queries1))
print(circularArrayRotation(a2, k2, queries2))