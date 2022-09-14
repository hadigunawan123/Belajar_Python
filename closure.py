# 2. parameter "message" got a "TEST MESSAGE" value into him
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        # 4. this "message" param get the value from his higher function and printing it
        print(message)

    # 1. this is executed first and get value "None" when printed #3. this function is executed
    data_transmitter()


print(transmit_to_space("TEST MESSAGE"))

# This works well as the 'data_transmitter' function can access the 'message'. To demonstrate the use of the "nonlocal" keyword, consider this:


def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 2
        print(f"{number} inside")
    printer()
    print(number)


print_msg(10)
# Without the nonlocal keyword, the output would be "2 inside" & "10", however, with its usage, we get "2 inside" & "2", that is the value of the "number" variable gets modified.


print("="*15)  # exercise
# Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.


def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
