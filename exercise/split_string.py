teks = 'belajar python dasar'
split = []
kata = ''
for huruf in teks:
    if huruf != ' ':
        kata += huruf
    else:
        split.append(kata)
        kata = ''

split.append(kata)
print(split)

# pythonic way
split2 = teks.split(' ')
print(split2)
