# make a list consist of integer between last int of list "a" and first int of list "b" if the integer is modulo by another value in all value in list a+b == 0
def getTotalX(a, b):
    # Write your code here
    c = []
    for bil in range(a[-1], b[0]+1):
        for i in (a+b):
            if i < bil and bil % i != 0:
                print(f"ini break 1, nilai i = {i} dan nilai bil = {bil}")
                break
            if i > bil and i % bil != 0:
                print(f"ini break 2, nilai i = {i} dan nilai bil = {bil}")
                break
        else:
            print(bil)
            c.append(bil)

    print(c)
    print(len(c))


a = [2, 4]
b = [16, 32, 96]
getTotalX(a, b)
