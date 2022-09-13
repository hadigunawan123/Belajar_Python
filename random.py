import random


def lottery():
    for i in range(7):  # create 7 random number
        # saving data when loop iterating another data, random number between (1-8)
        yield random.randint(1, 8)


list = []
for index, randnumber in enumerate(lottery()):
    print(f"Nomer ke {index+1} adalah = {randnumber}")
    list.append(randnumber)

print(f"Total keseluruhan angka adalah = {sum(list)}")
