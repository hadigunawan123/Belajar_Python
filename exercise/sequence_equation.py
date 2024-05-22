'''
Given a sequence of n integers, p(1), p(2),..., p(n) where each element is distinct and satisfies 1 ≤ p(x) ≤ n. For
each a where 1 ≤ x ≤ n, that is a increments from 1 to n, find any integer y such that p(p(y)) = x and keep a history of the values of y in a return array.
Example
p = [5, 2, 1, 3, 4]
Each value of x between 1 and 5, the length of the sequence, is analyzed as follows:
1. x = 1 = p[3], p[4] = 3, so p[p[4]]
= 1
2. x = 2 = p[2], p[2] = 2, so p[p[2]] = 2
3. x = 3 = p[4], p[5] = 4, so p[p[5]]
= 3
4. x = 4 = p[5], p[1] = 5, so p[p[1]] = 4
5. x = 5 = p[1], p[3] = 1, so p[p[3]] = 5
The values for y are [4, 2, 5, 1, 3].
Function Description
Complete the permutationEquation function in the editor below.
permutationEquation has the following parameter(s):
int p[n]: an array of integers
Returns
• int[n]: the values of y for all x in the arithmetic sequence 1 to n
'''
# n = int(input().strip())
def permutationEquation(p):
    # Write your code here
    peta = {v:i+1 for i,v in enumerate(p)}
    return [peta[peta[i]] for i in range(1, n+1)]

p1, p2 = [2, 3, 1], [4, 3, 5, 1, 2]
n = len(p1)
print(permutationEquation(p1))
print(permutationEquation(p2))