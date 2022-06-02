ganjil = list(range(1, 10, 2))
genap = list(range(2, 11, 2))

gabungan = ganjil + genap
print(gabungan)

nestedlist = [ganjil+genap]
print(nestedlist)

nestedlist2 = [ganjil, genap]
print(nestedlist2)

for luar in nestedlist2:
    print(luar)

    for dalam in luar:
        print(dalam)
