def contohTypeError(value):
    try:
        print("string concatination " + value)
    except TypeError:
        print("ada erorr tipe data")

contohTypeError(100)