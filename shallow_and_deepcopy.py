from copy import deepcopy
data1 = [1, 2, 3]
data2 = [4, 5, 6]

datacampur = [data1, data2, 7, 8]
datacampurcopyshallow = datacampur.copy()

datacampur[0][1] = 100
print(f"address datacampur = {hex(id(datacampur))}")
print(f"address datacampurcopyshallow = {hex(id(datacampurcopyshallow))}")

print(f"address datacampur index-1 = {hex(id(datacampur[0][1]))}")
print(
    f"address datacampurcopyshallow index-1 = {hex(id(datacampurcopyshallow[0][1]))}")

print(datacampur)
print(datacampurcopyshallow)


print("#############################################")
datacampurcopydeep = deepcopy(datacampur)
datacampur[0][0] = 10000
print(f"address datacampur = {hex(id(datacampur))}")
print(f"address datacampurcopydeep = {hex(id(datacampurcopydeep))}")

print(f"address datacampur index-0 = {hex(id(datacampur[0][0]))}")
print(
    f"address datacampurcopydeep index -0 = {hex(id(datacampurcopydeep[0][0]))}")

print(datacampur)
print(datacampurcopydeep)


print("#############################################")
print(datacampur)
print(datacampurcopyshallow)
print(datacampurcopydeep)
