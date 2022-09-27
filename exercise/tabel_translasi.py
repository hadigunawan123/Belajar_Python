string_input = str(input("Apa kota tempat anda tinggal? : ").lower())
# string_output = ""
# dict_for_translasi = {
#     "a":"4",
#     "i":"1",
#     "e":"3",
#     "o":"0"
# }
# for i in string_input:
#     after_translate = dict_for_translasi.get(i) #dict_for_translasi[i] will result error if i doesnt met in dict
#     string_output += after_translate if after_translate else i

# print(f"hasil translasi string: {string_output}")

print("="*20)
# pythonic way
sumber = "aieo"
tujuan = "4130"
# param 1= sumber, param 2=tujuan/after
tabel_translasi = str.maketrans(sumber, tujuan)
string_output2 = string_input.translate(tabel_translasi)
print(f"hasil translasi string: {string_output2}")
