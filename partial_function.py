from functools import partial


def multiply(x, y):
    return x * y


# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))

print("="*15)


def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x


# Enter your code here to create and print with your partial function
prtl = partial(func, 10, 5, 2)
print(prtl(1))
