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
