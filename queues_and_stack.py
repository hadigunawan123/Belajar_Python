# there's no queues built-in function in python, so we need to use this library below
from collections import deque
antrian = deque(list(range(1, 11)))

print(antrian)

antrian.append(11)
print(antrian)

# bisa pake pop left untuk operasi queue, example:
out = antrian.popleft()  # <-this one is queues, (LILO) Last In Last Out
print(f"data yang keluar adalah: {out}")
print(antrian)

# nama.pop() #<-this one is stack, (LIFO) Last In First Out
