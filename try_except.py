def hitung(a, b):
    while True:
        try:
            a+b
        except:
            print("Pastikan anda tidak meng-input karakter")
            while True:
                try:
                    a = int(input("Masukan angka ke-1 = "))
                    while True:
                        try:
                            b = int(input("Masukan angka ke-2 = "))
                        except:
                            print("Masukan angka ke-2 dengan benar")
                        else:
                            break
                    break
                except:
                    print("Masukan angka ke-1 dengan benar")
        else:
            print(f"Hasil dari {a} + {b} = {a+b}")
            break
        finally:
            print("="*20)


hitung(1, 2)
hitung(1, 10)
hitung(1, "a")
