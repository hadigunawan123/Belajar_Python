# *args (Non Keyword Arguments)
# **kwargs (Keyword Arguments)
# We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.

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


print("="*25)


def foo(first, second, third, *therest):  # *args
    print("First: %s" % (first))
    print("Second: %s" % (second))
    print("Third: %s" % (third))
    print("And all the rest... %s" % (list(therest)))


foo(1, 2, 3, 4, 5, 6, 7)


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print("angka pertama =  %d" % (result))


print("="*25)
# more example
def math(*args,**kwargs):
    output = 0
    if kwargs['option'] =='tambah':
        for angka in args:
            output += angka
    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args:
            output *= angka
    elif kwargs['option'] == 'bagi':
        output = args[0]
        for angka in args:
            output /= angka
    return output

hasil1 = math(1,2,3,4,5,6,option = 'tambah')
hasil2= math(1,2,3,4,5,6,option = 'kali')
hasil3 = math(1,2,3,4,5,6,option = 'bagi')
print(f"Jumlah = {hasil1}")
print(f"Kali = {hasil2}")
print(f"bagi = {hasil3}")


#more example
def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n  # sum += n

    print("Sum:", sum)


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)


def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(ASDASDASDADA="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com",
      Country="Wakanda", Age=25, Phone=9876543210)


print("="*25)
# exercise
# Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) The foo function must return the amount of extra arguments received. The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.


def foo(a, b, c, *args):
    return len(args)


def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
