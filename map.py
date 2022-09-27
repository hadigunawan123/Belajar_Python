def pengkalian(x):
    return x*2


angkaku = [202, 203, 213, 32, 213, 432]
# param 1 isi fungsi, param 2 isi iterable yang akan dikenakan fungsi si param 1
listjadi = list(map(pengkalian, angkaku))
print(listjadi)  # hasil = [angkaku[i]*2]
