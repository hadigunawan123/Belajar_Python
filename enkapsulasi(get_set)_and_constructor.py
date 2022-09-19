# class Person:
#     __umur = 0 #__ = private, _ = protected

#     def get_umur(self): #getter
#         return self.__umur
#     def set_umur(self, umur): #setter
#         # if umur >= 0:
#         #     self.__umur = umur
#         # else:
#         #     0
#         self.__umur = umur if umur >= 0 else 0

# p = Person()
# # p.umur = 12 #if umur doesn't private'd, but problem is when p.umur = <0/negative
# # p.set_umur(-23) #value printed gonna be 0
# p.set_umur(23) #value printed gonna be 23
# print(p.get_umur())


# KODE DIATAS ADALAH ENKAPSULASI (GETTER AND SETTER) WITHOUT CONSTRUCTOR, KODE DIBAWAH PAKE CONSTRUCTOR

# this is constructor, method khusus yang bernama sama dgn classnya, dan dipanggil pertama kali saat kita buat objek dari class tsb
class Person:
    __umur = 0  # __ = private, _ = protected, kayanya ini juga udah gk dibutuhin semenjak constructor dibuat dibawah ini dengan deafult valuenya 0

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


p = Person("Hadi Gunawan", -23)
# p = Person(umur = 23) #jika mau umurnya aja yg diubah dari default
print(p.get_name())
print(p.get_umur())
