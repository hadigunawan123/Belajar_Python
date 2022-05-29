# get index in loop by for loop and while loop
kumpulannama = [123, 324, 1231, 32423, 12321]  # angka btw, males ganti bjir
lengthh = len(kumpulannama)

for nama in range(lengthh):  # looping for list dengan range (sama aja padahalmah hehe)
    print(f"nama ke : {kumpulannama[nama]}")

for nama2 in kumpulannama:  # looping for list biasa
    print(f"nama ke : {nama2}")


i = 0
while i < lengthh:  # looping list dengan while
    print(f"nama ke : {kumpulannama[i]}")
    i += 1


# list comprehension
listcampur = ["stringcuy", 1, 2, 3, 4, "oyeee"]
for data in listcampur:
    print(data)


[print(i) for i in listcampur]


# enumerate
print("\nEnumerate")
for index, data in enumerate(listcampur):
    print(f"indexnya = {index}, valuenya = {data}")
