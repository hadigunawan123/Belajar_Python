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


class Student(Person):  # class Student adalah turunan (INHERITANCE) dari class Person
    def __init__(self, name="Default Name", umur=0, id=7):  # Bisa nambahin param
        super().__init__(name, umur)  # <-- Constructor Person
        self.__id = id  # nambahin khusus buat Student

    def perkenalanDiri(self):  # nambahin khusus buat Student
        # inilah yg disebut METHOD OVERIDING (ngeoveride method parent)
        return super().perkenalanDiri() + " saya ber-id : " + str(self.__id)
        # patternnya gak perlu sama kaya parent, contoh:
        # return "Halo nama saya " + self.get_name() + " dan saya ber-id : " + str(self.__id)


def main():
    # p = Person("Hadi Gunawan", -23)
    # print(p.perkenalanDiri())
    s = Student("Dodi", 12)
    print(s.perkenalanDiri())


main()
