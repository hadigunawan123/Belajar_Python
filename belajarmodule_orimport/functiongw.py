def sayHello(nama="Nama default"):
    return f"Hello {nama}"


def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total+angka
    return total
