# for segitiga
# sisi = 4

# count = 0

# for i in range(sisi):
#     count += 1
#     print("*"*count)

# while segitiga
# berapasegitiga = int(input("Mau bentuk segitiga sampai mana?: "))
# count = 0

# while True:
#     if count >= berapasegitiga:
#         break
#     count += 1
#     print("*"*count)

# while True:
#     if count >= berapasegitiga:
#         break
#     elif count % 2 != 0:
#         count += 1
#         print("ganjil")
#         continue
#     count += 1
#     print("*"*count)


# while True:
#     if count >= berapasegitiga:
#         break
#     elif count % 2 != 0:
#         count += 1
#         continue
#     count += 1
#     print("*"*count)

# segitiga sama kaki
berapasegitiga = int(input("Mau bentuk segitiga sampai mana?: "))
count = 1
spasi = int(berapasegitiga/2)
while True:
    if count % 2 != 0:
        print(" "*spasi, "*"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue

    if count > berapasegitiga:
        break
