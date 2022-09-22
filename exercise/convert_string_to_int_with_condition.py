s = "abc def ghi 3.000 5.000 9.000"
splitted = s.split(" ")
print(splitted)
# because "list" cannot using "replace" method, so we need to loop it and put it in the new list using replace method
splitted_clean = [i.replace(".", "") for i in splitted]
print(splitted_clean)
price = [int(i) for i in splitted_clean if i.isdigit()]
print(price)
