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
