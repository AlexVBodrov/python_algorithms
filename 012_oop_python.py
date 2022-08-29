class DigitRetrieve:
    # dg = DigitRetrieve()
    def __call__(self, string: str, *args, **kwds):
        if string.isdigit() or (string[0] == "-" and string[1:].isdigit()):
            return int(string)


# С помощью объектов класса DigitRetrieve должно выполняться преобразование чисел из списка строк следующим образом:
dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
# print(digits)
