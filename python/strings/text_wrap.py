'''
You are given a string string and width max_width, Your task is to wrap the string into a paragraph of width max_width

example :
s = ABCDEFGHIJKLIMNOQRSTUVWXYZ
w = 4

answer should be:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

import textwrap

#without textwrap module
def wrap(string, max_width):
    wrapped_lines = [string[i:i+max_width] for i in range(0, len(string), max_width)]
    # print(type(wrapped_lines)) # <class 'list'>
    return '\n'.join(wrapped_lines)
    
#with textwrap module
# def wrap(string, max_width):
#     return '\n'.join(textwrap.wrap(string, max_width))

string, string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Hadi Gunawan"
max_width, max_width2 = 4, 2

print(wrap(string, max_width))
print(wrap(string2, max_width2))

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)