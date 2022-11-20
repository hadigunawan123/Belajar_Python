'''
cancel kelas perkuliahan jika murid yang datang on time lebih kecil dari treshold (k), murid dianggap telat jika waktu datang > 0
'''


def angryProfessor(k, a):
    tidak_telat = 0
    for i in a:
        if i <= 0:
            tidak_telat += 1

    return 'Kelas tidak dicancel' if tidak_telat >= k else 'Kelas dicancel'


print(angryProfessor(3, [-1, -2, 0, 1, 2, 5]))
print(angryProfessor(5, [-1, -2, 0, 1, 2, 5]))
