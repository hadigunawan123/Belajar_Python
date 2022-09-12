def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b),
        a, b = b, a+b
    print(f"angka sudah melebihi {n}")


fib(100000)
