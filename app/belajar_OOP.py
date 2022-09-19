# class Sapi:
#     //field -> apa yang dimiliki oleh class (kata benda/noun, ex: nama, umur)
#     //method -> fungsi yang dilakukan oleh si class (kata kerja/verb, ex:makan,minum,tidur)

class Segiempat:  # Membuat class (denah/blueprint)
    # field
    panjang = 0
    lebar = 0
    # method

    def hitungLuas(self):  # self akan berisi objek yg memanggil hitungLuas
        return self.panjang * self.lebar


def main():
    # membuat objek, (bisa dibilang rumah)
    s = Segiempat()  # ini objek dari Segiempat dengan nama "s"
    s.panjang = int(input())
    s.lebar = int(input())
    luas = s.hitungLuas()
    print(luas)


main()
