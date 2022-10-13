import random


def migratoryBirds(arr):
    highest_count = 0
    highest_bird_type = 0
    for i in range(1, 6):
        count = len([bird for bird in arr if bird == i])
        if highest_count < count:
            highest_count = count
            highest_bird_type = i
    return highest_bird_type


list = []
for i in range(1, 15):
    list.append(random.randint(1, 6))

print(list)
print(migratoryBirds(list))
