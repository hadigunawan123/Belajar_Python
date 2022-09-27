listmu = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(len(listmu))
lismureversed = []
for i in range(len(listmu)):
    reverse_i = len(listmu)-1-i
    lismureversed.append(listmu[reverse_i])

print(lismureversed)

# pythonic way
reverse_pythonic = listmu[::-1]
stringku = "Hai semua nama gue Ewing dan terima kasih telah memberikan gue kesempatan untuk menemani malam jum'at loe"
reverse_pythonic_string = stringku[::-1]
print(reverse_pythonic_string)
print(stringku[::-1])
