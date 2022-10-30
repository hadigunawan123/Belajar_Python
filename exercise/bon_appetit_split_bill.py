def bonAppetit(bill, k, b):
    # "//" agar hasilnya integer, bukan float
    anna_paid = (sum(bill) - bill[k])//2
    print("Bon Appetit" if anna_paid == b else abs(anna_paid-b))
    # print(bill,k,b) # bill = [3,10,2,9], k = 1, b = 12
    # so yang ditagih ke ana itu 12, padahal ana cuma makan makanan dengan index != 1 (so 3+2+9 = 14)
    # nah 14 // 2 kan harusnya 7, kalau b = 7 maka code akan print "Bon Appetit", namun karna yg ditagih
    # ke ana gk sesuai, maka kita print selisihnya, kita abs karna biar gk minus (kita cuma mau tau selisih)


bill = [3, 10, 2, 9]
k = 1
b = 12
bonAppetit(bill, k, b)
