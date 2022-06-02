# args = jika argument bisa berapapun, kwargs juga sama. Tapi args mereturn tuple, kwargs dict
def jumlah(*args):
    # args mereturn tuple, tuple cant be summed, you need to iterable it, so its like ((1,2,3,4)) not (1,2,3,4)
    print(sum((args)))

    # sum(1,2,3) #error
jumlah(1, 2, 3, 4, 100)
print(sum([1, 2, 3]))  # gk error (list)


def contoh(*args, **kwargs):
    print(f"saya ingin membeli {args} dan {kwargs}")
    print(type(args))
    print(type(kwargs))


contoh("semangka", "stoberi", "modelinstagram",
       selebgram="bidadariOnicEsportsLOL")
