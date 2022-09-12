from attr import has
# import functiongw
from functiongw import sayHello
from functiongw import jumlahkan

# hello = functiongw.sayHello("Hadi Gunawan")
# print(hello)
hello = sayHello("Hadi Gunawan")
print(hello)

hasil = jumlahkan(200, 300, 10, 20, 30)
print(hasil)

print(dir(sayHello))


# dibawah ini kode jika ingin import module tapi bukan di folder yg sama tapi tanpa deklarasi spesifik lokasi
# gw comment aja, contoh doang in case you need it
print("="*10)

# import sys
# print(sys.path)
# sys.path.append("/kumpulanmodulekamu")
# print(sys.path)
