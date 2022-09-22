arr = [1, 3, 5, 6, 11, 23]
sum = 9


def twoSum(a, s):
    for num1 in arr:
        if num1 <= 9:
            print(f"num1 = {num1}")
            for num2 in arr:
                if num1 <= 9:
                    if num1+num2 == sum:
                        print(f"num2 = {num2}")
                        print(
                            f"Found it! num1 = {num1}, num2 = {num2} sooo, num1+num2 = {num1+num2})")
                    else:
                        continue


twoSum(arr, sum)
