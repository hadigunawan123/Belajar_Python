import types  # for the generators version fib


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b),
        a, b = b, a+b
    print(f"angka sudah melebihi {n}")


fib(100000)

# Can you use only two variables in the generator function? Remember that assignments can be done simultaneously. The code will simultaneously switch the values of a and b.
# fill in this function


def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


# testing code
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
