import random
list = []
inputan = abs(int(input()))
for i in range(1, inputan+1):
    list.append(random.randint(1, 5))
print(list)
