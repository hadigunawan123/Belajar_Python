# class mahasiswa():
#     nama = "namadefault"

#     def belajar(self, kondisinya):
#         print(self.nama, "sedang belajar", kondisinya)

#     def tidur(self):  # bisa ditambah kondisi/param lain jk mau, kan ini sama dengan parameter pada function
#         print(self.nama, "sedang tidur")


# # main programnya
# hadi = mahasiswa() #instances yg turunan dr class mahasiswa
# helga = mahasiswa()

# hadi.nama = "Hadi Gunawan"
# helga.nama = "Helga amin"

# hadi.belajar("dengan giat")
# helga.tidur()


print("\n\n", "="*5, "UPDATE DARI YANG DI ATAS", "="*5, "\n\n")


class mahasiswa():
    # nama = "namadefault"
    __nilai = 0  # private
    jurusan = 'Seni Bertahan Hidup'  # public

    # fungsi tambahan
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim  # public
        # print("Ini adalah init (method pertama yg akan dijalankan saat class di panggil oleh instances)")

    def belajar(self, kondisinya):
        print(self.nama, "sedang belajar", kondisinya)

    def tidur(self):  # bisa ditambah kondisi/param lain jk mau, kan ini sama dengan parameter pada function
        print(self.nama, "sedang tidur")

    def uts(self, input_nilai):  # input nilai ini dengan input nilai UAS itu beda, karna beda scope
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if (self.__nilai/2) < 60:
            print(f"{self.nama} Tidak lulus")
        elif (self.__nilai/2) >= 60 and (self.__nilai/2) <= 100:
            print(f"{self.nama} Lulus")
        else:
            print(f"Nilai {self.nama} tidak valid")

    # membuat variable/attribute private bisa diakses keluar
    def total(self):
        print(self.nama, self.jurusan, 'total nilainya', self.__nilai)

    def total_nilai(self):
        print(self.__nilai)


# main programnya
# sesi pemanggilan fungsi
hadi = mahasiswa("Hadi Gunawan", 171011401000)  # ini instances
print(hadi)
print(hadi.nama)
print(hadi.nim)

hadi.belajar("dengan giat")
hadi.tidur()

print("="*20)
hadi.uts(100)
hadi.uas(100)
hadi.check_status()


# print(hadi.__nilai) #ini akan error karna var private tdk bisa diakses di publik spt ini

print("="*20)
# dibagian ini mecoba mengakses attribute __nilai(private) dgn fungsi total_nilai, hasilnya variable/attribute __nilai(private) bisa di tampilkan/di public
hadi.total()
hadi.total_nilai()
# kesimpulannya, variable/attribute private tidak bisa dipanggil secara langsung, tapi bisa di akses/ditampilkan dengan fungsi
