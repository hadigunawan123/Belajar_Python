'''
The factorial of the integer n, written n!, is defined as:
n! = n x (n - 1) x (n - 2) x ...
Calculate and print the factorial of a given integer.
.. x 3 x 2 x 1
For example, if n = 30, we calculate 30 x 29 x 28 x -- x 2 x 1 and get 265252859812191058636308480000000.
Function Description
Complete the extraLong Factorials function in the editor below. It should print the result and return.
extraLongFactorials has the following parameter(s):
n: an integer
'''

def extraLongFactorials(n):
    # Write your code here
    answer = 1
    while n!=1:
        answer *= n
        n -= 1
    return answer #or just print

print(extraLongFactorials(20))
print(extraLongFactorials(30))