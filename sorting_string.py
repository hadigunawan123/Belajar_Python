string = "hadigunawan"  # string yang mau disortir
# akan mengembalikan list dari semua huruf diatas sudah diurut
sorted_string = sorted(string)
print(type(sorted_string))
print(sorted_string)
for i in sorted_string:

    # print stringnya dengan for loop, end="" itu biar ga ada spasinya
    print(i, end="")
    # print(i)
