a = "Saya suka buah apel"

a = a.split(' ')
print(a)
hasil = []
for i in a:
    print(i[0], end=' ')
    # or
    hasil.append(i[0])

print(hasil)
