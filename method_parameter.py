# ======================Method parameter, method parameter with default value
def say_Hello(firstName="nama depan", lastName="nama belakang"):
    # note default value harus diikuti dengan default value terus, usahain deafult value itu param last aja
    print(f"Hello {firstName} - {lastName}")


say_Hello("Hadi", "Gunawan")
say_Hello()
say_Hello(lastName="PickyPicks")
