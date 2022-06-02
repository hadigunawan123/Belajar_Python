# ======================Looping for and while with continue and break
for i in range(100):
    if i % 2 == 1:
        continue  # continue funsinya utk skip kode dibawahnya jika kondisi terpenuhi
    print(i)

for i in range(100):
    if i % 50 == 0:
        continue
    print(i)

while True:
    data = input("Data: ")
    if data == "Hadi Gunawan":
        break  # fungsi break yaitu utk menghentikan looping jika kondisi terpenuhi
    print(data)


# loop range angka dibuat jd segitiga
print("="*40)
listkesini1 = []
for i in range(1, 11):
    listkesini1.append(i)
    print(listkesini1)

# append hasil loop ke list kosong
print("="*40)
listkesini2 = []
for i in range(1, 21):
    listkesini2.append(i)

print(listkesini2)

# LIST COMPREHENSION
print("="*40)
listkesini3 = [i for i in range(1, 16)]
print(listkesini3)

print("="*40)
# enaknya pake cara ini, hasil loop bisa di operasikan dgn math
listkesini4 = [i**2 for i in range(1, 16)]
print(listkesini4)

print("="*40)
# enaknya pake cara ini, hasil loop bisa di operasikan dgn math
listkesini5 = [(i**2/2) for i in range(1, 16)]
print(listkesini5)

print("="*40)
loop1 = [x for x in range(5) if x > 0]
print(loop1)

print("="*40)
loop2 = [x+1 for x in range(5) if x > 0]
print(loop2)

print("="*40)
loop3 = [x for x in range(5) if x % 2 == 0]
print(loop3)

print("="*40)
loop4 = [x for x in range(5) if x % 2 == 0 and x != 0]
print(loop4)

print("="*40)
loop5 = [x if x % 2 == 0 else "Ganjil" for x in range(1, 6)]
print(loop5)
