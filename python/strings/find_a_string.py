'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
occurs in the given string. String traversal will take place from left to right, not from right to left.
Note: String letters are case-sensitive.
Input Format
The first line of input contains the original string. The next line contains the substring.


example:
string = "ABCDCDC"
sub_string = "CDC"

return 2, because there are 2 times 'CDC' occur in the string
'''
string = "ABCDCDC"
sub_string = "CDC"

string2 = "asdsdasdxddasasd"
sub_string2 = "asd"


def count_substring(string, sub_string):
    answer = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            answer += 1
    return answer

print(count_substring(string, sub_string))
print(count_substring(string2, sub_string2))

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)
