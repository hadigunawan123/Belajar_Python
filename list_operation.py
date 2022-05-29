nama = []

nama.append("Hadi Gunawan")  # insert data di akhir
nama.extend("Hadi Gunawan")  # input jadi iterables
nama.insert(int(len(nama)/2), "insertditengah")  # insert ditengah
nama.insert(1, "insertdatakeindex-1")  # insert ke index 1
print(nama)
for index, value in enumerate(nama):
    print(index, " ", value)

print("\n", "="*20)
for i in nama:
    print(i)

# nama.remove("ygmaudiremove") #this only delete the first "founded" string if there's duplicate in the list
# nama.reverse() #reverse object di list either numeric/string
# print(dir(nama)) #<- untuk mengecek operasi apa sj yg tersedia di tipe data ini (in this case is list)
# print(dir(tuple)) #<- untuk mengecek operasi apa sj yg tersedia di tipe data ini (in this case is tuple)
