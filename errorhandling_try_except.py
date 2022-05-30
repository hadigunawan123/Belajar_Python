print("ini adalah program pembagian")

while True:
    try:
        # import panda
        penyebut = int(input("masukan angka penyebut: "))
        pembilang = int(input("masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError:  # jika insert string, maka error valueError
        print("yang anda masukan bukan angka\n")
    except ZeroDivisionError:  # jika insert 0, maka error zerodivisionerror
        print("angka pembilang yang anda masukan adalah nol, pilih yang lain ya bro\n")
    except ImportError:  # jika import module yg tdk ada/salah
        print("gak ada modulnya bro")
    except Exception as err:
        print(err)

"""
    type of exception errors:
    1. IOError
    2. ImportError
    3. ValueError
    4. Division by zero
    5. KeyboardInterupted
    6. EOFError
"""

print(f"berhasil, hasil pembagian adalah: {hasil}")
