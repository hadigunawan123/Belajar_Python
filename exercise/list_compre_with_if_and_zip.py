# example coy
print("="*25)
listangka = [i for i in range(1, 50)]
print(listangka)


# another one
listmu = [30, 60, 10, 55]
listku = [item for item in listmu if item >= 50]
print(listku)

# zip coba
# normal without comprehension
nama = ["Hadi", "Pujo", "Dadeng"]
usia = [23, 24, 23]
nampung = []
for n, u in range(len(nama)):
    nampung.append(n, u)

print(nampung)

nampungv2 = [[d_nama, d_usia] for d_nama, d_usia in zip(nama, usia)]
print(f"diluar nalar coy\n{nampungv2}")
