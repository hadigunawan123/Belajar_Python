for i, v in enumerate("belajar python"):
    if v == "a":
        print("Di posisi A")
        continue
    elif v == " ":
        print(f"index = {i} ###### value = 'spasi'")
        continue
    print(f"index = {i} ###### value = {v}")

print("="*30)
for i in range(1, 11):
    print(i, end=" ")
    if i % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")
