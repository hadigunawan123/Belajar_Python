# ======================Return Value/Method Function(method yg mengembalikan nilai (return value))/mengembalikan hasil yg dibuat oleh sebuah method
def jumlahkan(*list_angka):  # Argument list ditandai dengan asterisk di awal parameternya
    total = 0
    for angka in list_angka:
        total = total + angka
    return total  # jika hanya ingin return 1 value


total = jumlahkan(10, 20, 30, 40, 50)

print(f"Total {total}")  # hasil = Total 150
# ---------------------------------


def jumlahkan(*list_angka):  # Argument list ditandai dengan asterisk di awal parameternya
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total)  # kita return tuple jika ingin 2 return value


list_angka, total = jumlahkan(10, 20, 30, 40, 50)

print(f"Total {list_angka} = {total}")
