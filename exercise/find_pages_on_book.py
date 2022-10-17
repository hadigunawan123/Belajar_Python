def pageCount(total, pages):
    depan = pages//2
    belakang = (total-pages)//2

    if pages % 2 != 0 and total-pages == 1:
        belakang += 1

    if belakang < depan:
        return belakang
    else:
        return depan


total_halaman1 = 6
page_yang_dituju1 = 2

total_halaman2 = 5
page_yang_dituju2 = 4

print("Page 1 selalu ada di kanan, disebelah kirinya cover")
print("Page last bisa ada di kanan (GANJIL) atau kiri, kalau di kiri (GENAP) maka kanannya back cover")
print("KITA BISA PILIH BUKA BUKUNYA DARI KIRI (awal) ATAU KANAN (akhir), lalu AMBIL YANG PALING SEDIKIT FLIPPINGNYA")
print("="*15)
print(f"Total halaman = {total_halaman1}, mau ke halaman: {page_yang_dituju1}, MAKA KITA BUTUH FLIP BERAPA HALAMAN? JAWABAN : {pageCount(total_halaman1, page_yang_dituju1)}")
print("="*15)
print(f"Total halaman = {total_halaman2}, mau ke halaman: {page_yang_dituju2}, MAKA KITA BUTUH FLIP BERAPA HALAMAN? JAWABAN : {pageCount(total_halaman2, page_yang_dituju2)}")
