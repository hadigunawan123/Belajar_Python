'''
Task
Given an integer, n, and n space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported
'''

if __name__ == '__main__':
    n = int(input()) # 1 2
    integer_list = map(int, input().split()) #resulting a map object, split funtion returning an int into string, thats why we need to map it into int again
    
    t = tuple(integer_list)
    print(hash(t))
    
    