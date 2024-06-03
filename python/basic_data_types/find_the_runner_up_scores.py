# n = int(input())
# arr = map(int, input().split())

arr = [2,3,6,6,5]

my_arr = list(set(arr)) #in case the input (arr) is not a list (lets say map)
print(max([i for i in list(my_arr) if i < max(my_arr)]))

#just use code below if the array is list already
# print(max([i for i in arr if i < max(arr)])) 