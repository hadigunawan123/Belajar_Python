class Person:
    # __umur = 0 #__ = private, _protected
    def __init__(self, name="Default Name", umur=0):  # constructor
        self.__name = name
        self.__set_umur(umur)

    def get_name(self):
        return self.__name

    def get_umur(self):  # getter
        return self.__umur

    def __set_umur(self, umur):  # setter
        # if umur >= 0:
        #     self.__umur = umur
        # else:
        #     0
        self.__umur = umur if umur >= 0 else 0

    def perkenalanDiri(self):
        return "Halo nama saya " + self.__name + " dan umur saya " + str(self.__umur) + " tahun"

    # buat OPERATOR OVERLOADING untuk tanda "+" pada variabel "a" dibawah
    # __add__ beneran built in function/method dari python (INI YANG DINAMAKAN SPECIAL METHOD)
    def __add__(self, other):  # self = si pemanggil, kalau yg panggil "p" maka self=p, other=y
        new = Person(self.get_name() + other.get_name(),
                     self.get_umur() + other.get_umur())
        return new

    def __str__(self):
        return self.perkenalanDiri()


p = Person("Hadi Gunawan", -23)
y = Person("Ronaldo Louhenapessy", 22)
# coba objek person ditambah objek person yg lain
a = p + y
print(a.perkenalanDiri())
print(
    f"contoh overloading lg dgn mengubah 'perkenalanDiri jadi string'{str(a)}")  # "str"nya udah di overload diatas
# print(p.get_name())
# print(p.get_umur())
print(p.perkenalanDiri())
