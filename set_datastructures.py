# ======================Set
setname = {"Hadi", "Rofik", "Bapak"}
print(setname)
# we cannot rename (ubah) data di set dan tuple, in list we can
setname.add("Ema")  # in list we use append
setname.add("buatDiapus")
setname.remove("buatDiapus")
print(setname)

for i in setname:
    print(i)  # no index
