def hello_world(nama):
    print(f"hello world by {nama}")


def tambah(angka1, angka2):
    hasil = angka1+angka2
    print(f"hasil dari {angka1} + {angka2} = {hasil}")
    return hasil


hello_world("hadi")
tambah(2, 5)


def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for index, peserta in enumerate(data_peserta):
        print(f"yuk absen adick2, nomor : {index + 1} adalah {peserta}")


anggota_boyband_korea = ["Ucup", "Sidique", "Rofique"]
say_hi(anggota_boyband_korea)


def perkalian(a=1, b=2):
    return a*b


print(perkalian(2, 3))
print(perkalian())


def pertambahan(c, d):
    total = c+d
    # print(f"hasilnya adalah = {total}") #aktifkan line ini jk ingin langsung di print
    return total


# gk ke print karna di fungsinya cuma return hasil, gk di print
pertambahan(1, 9999)
print(pertambahan(1, 100))

print("="*30)


def belajar(varnya="Python"):
    print(f"saya sedang belajar {varnya}")


belajar("C++")
belajar()
