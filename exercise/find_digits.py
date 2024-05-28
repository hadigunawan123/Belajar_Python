'''
An integer n is a divisor of an integer  if the remainder of n%d=0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

Example
n=123

Check whether 1, 2 and 4 are divisors of 124. All 3 numbers divide evenly into 124 so return 3.

example again:
n=10

Check whether 1 and 0 are divisors of 10. 1 is but 0 is not (error), so return 1
'''

def findDigits(n):
    # Write your code here
    result = 0
    for i in str(n):
        if i != "0":
            if n % int(i) == 0:
                result+=1
            
    return result

print(findDigits(125))
print(findDigits(124))
print(findDigits(13))