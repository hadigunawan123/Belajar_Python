class RekeningBank:

    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def cetak_saldo(self):
        if self.saldo < 50000:
            print(
                f"saldo atas nama {self.nama} : Rp{self.saldo}\nSegera minta gajian ke atasan anda hehe")
        else:
            print(f"saldo atas nama {self.nama} : Rp{self.saldo}")

    def menabung(self):
        tambah = int(
            input("Masukkan jumlah nominal uang yang ingin ditabung = "))
        self.saldo += tambah
        print(
            f"Anda menabung {tambah}, saldo rekening anda saat ini adalah {self.saldo}")

    def menarik_uang(self):
        tarik = int(input("Masukkan jumlah nominal uang yang ingin ditarik = "))
        if self.saldo < tarik:
            print(
                f"saldo anda sekarang kurang dari {tarik}, saldo tersisa anda: Rp{self.saldo}\n\nPenarikan uang gagal!")
        else:
            self.saldo -= tarik
            print(
                f"Berhasil!, silahkan ambil uang dan struk anda \nSaldo anda tersisa {self.saldo}")


tabunganhadi = RekeningBank("Hadi", 1000000)
tabunganhadi.cetak_saldo()
tabunganhadi.menabung()
tabunganhadi.menarik_uang()
