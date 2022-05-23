# ======================Argument List/Parameter List
def jumlahkan(*list_angka):  # Argument list ditandai dengan asterisk di awal parameternya, argument list gk boleh lebih dari 1, argument list harus berada paling belakang kalau mau ada parameter lain (gabisa argument list dulu terus diikuti param biasa)
    total = 0
    # note, karna hasil dari argument yg dimasukan ke parameter list berbentuk "List", otomatis tdk bisa ditambah kaya biasa (total = a+b+c dst), harus pakai loop
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")


# argument yg masuk ke param biasa dalam case ini maka tidak akan di jumlahkan (tidak masuk ke var total(karna gk masuk ke "*list_angka"))
jumlahkan(5, 3, 30, 100)
