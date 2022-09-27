# NORMAL FUNCTION
print("Normal Function Example")


def sum(a, b):
    return a + b


a = 1
b = 2
c = sum(a, b)
print(c)

# LAMBDA FUNCTION
# your_function_name = lambda inputs : output
print("Lambda Function Example")
a = 1
b = 2
def sum(x, y): return x + y


c = sum(a, b)
print(c)


# lambda functions to check if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element.
l = [2, 4, 7, 3, 14, 19]
for i in l:
    # your code here
    def my_lambda(x): return (x % 2) != 0
    print(my_lambda(i))

# another example
l2 = list(map(lambda x: x*2, l))
print(l2)
