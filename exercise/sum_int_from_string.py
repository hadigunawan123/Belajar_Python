soal = 1234
# konversi numerik ke string
soal = str(soal)
hasil = 0
# memisahkan karakter
for i in soal:
    jumlah = hasil+int(i)
    print(str(hasil)+"+"+str(i)+"="+str(jumlah))
    hasil = jumlah

print(f"hasil : {str(hasil)}")
