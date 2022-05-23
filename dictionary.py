# ======================Dictionary
customer = {"Name": "Hadi", "Age": 22, "Address": "Bintaroskuy"}
# name = customer["Name"] #example slicing
customer["Company"] = "Tokopedia"  # example insert new key and value
customer["Company"] = "Tokopediaku"  # example update
del customer["Address"]  # example delete key and value

for key in customer:
    # print(key) #hanya mengembalikan "Key" dari dictnya saja (Name enter Age enter Company)
    # isi value bisa dibaca: customer index ke key adalah customerindexName (Hadi), customerindexAge(22) dst yang nantinya disimpan ke var value
    value = customer[key]
    print(f"{key}:{value}")
# customer.items method will return tupple
print(customer.items())

# -----------------------
print("-----------------------")
for key in customer.items():
    print(f"{key[0]}:{key[1]}")

print("-----------------------")
for key, value in customer.items():
    print(f"{key}:{value}")
