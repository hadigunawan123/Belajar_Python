'''
﻿

You have two strings of lowercase English letters. You can perform two types of operations on the first string: 1. Append a lowercase English letter to the end of the string.
2. Delete the last character of the string. Performing this operation on an empty string results in an empty string.
Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s. If it's possible, print Yes. Otherwise, print No.
Example. s = = [a,b,c]
t = [d, e, f]
k = 6
To convert s to t, we first delete all of the characters in 3 moves. Next we add each of the characters of t in order. On
the 6th move, you will have the matching string. Return Yes.
If there were more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than 6 moves, we would not have succeeded in creating the new string.
Function Description
Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.
appendAndDelete has the following parameter(s):
• string s: the initial string
string t: the desired string
int k: the exact number of operations that must be performed

ex:
s=hackerhappy
t=hackerrank
k=9

then return yes, because we made <= 9 operation (k) (5 for deleting "happy" and then 4 for adding/appending a "rank")
'''

def appendAndDelete(s, t, k):
    # Write your code here
    stop = 0
    for i, j in zip(s, t):
        if i != j:
            break
        stop += 1
        
    delete_operation = len(s) - stop
    append_operation = len(t) - (len(s)-delete_operation)
    
    if append_operation == 0 and delete_operation <= k:
        return "Yes"
    elif delete_operation == 0 and (k-append_operation)%2 != 0:
        return "No"
    number_of_operation = delete_operation + append_operation
    
    return "Yes" if number_of_operation <= k else "No"

print(appendAndDelete(s= "hackerhappy", t= "hackerrank", k= 9))
print(appendAndDelete(s= "ashley", t= "ash", k= 2))