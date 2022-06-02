class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama:', self.nama, '\nmotor:',
              self.transmisi, '\ndaerah:', self.daerah)


class Gojek(Ojek):  # Gojek inherit ojek

    def cek_id_abang2(self):  # def cek_id_abang(self): (same name would be fine)
        print('cek aplikasi gojek')


ojek1 = Ojek('mario', 'manual', 'bandung selatan')
ojek2 = Gojek('jackson', 'automatic', 'tasikmalaya')

ojek1.cek_id_abang()

# sengaja di rename jd 2 biar keliatan bedanya method di Ojek dan Gojek
ojek2.cek_id_abang2()
# ojek1.cek_id_abang2() #ojek (lets say pangkalan) gabisa ngakses method turunannya (gojek)


# contoh 2
print("="*25)


class Mahasiswa:

    status = "Mahasiswa Unpam"  # variable global dalam class Mahasiswa

    def __init__(self, nama, prodi="Prodi default"):
        self.nama = nama
        self.prodi = prodi

    def keterangan(self):
        print(
            f"{self.nama} adalah seorang {self.status} yang ada di program studi {self.prodi}")


hadi = Mahasiswa("Hadi Gunawan", "Teknik Informatika")
print(hadi.keterangan())


class Nilai(Mahasiswa):

    def __init__(self, nama, prodi):  # <--atrr atau param
        super().__init__(nama, prodi)  # bisa dibaca = mahasiswa.__init__(nama, prodi)
        # dengan menggunakan super, py akan mencari class induk yg atribut/ paramnya sama persis
        self.nilai_update = []

    def input_nilai(self, tambah):
        return self.nilai_update.append(tambah)


indira = Nilai("Indira", "Teknik kimia")

print(indira.keterangan())
indira.input_nilai(80)
print(indira.nilai_update)  # tidak perlu parenthesis karna ada di fungsi init
