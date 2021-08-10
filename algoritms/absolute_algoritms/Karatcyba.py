# умножение n-значных чисел методом Каратцубы
# Вход: 2 числа, n-значных
# Допущение: n является степенью числа 2
# Выход x*y

# Допущение: n является степенью числа 2
num1 = 99902222
num2 = 99992222

rr = num1 * num2


def karatcuma(x, y):
    x = str(x)
    y = str(y)
    n = len(x)
    if n == 1:
        xy = int(x)*int(y)
        return xy
    else:
        # a, b := первая и вторая половины x
        # c, d := первая и вторая половины y
        a = int(x[:len(x) // 2])
        b = int(x[len(x) // 2:])
        c = int(y[:len(y) // 2])
        d = int(y[len(y) // 2:])
        # рекурсивно вычислить ac := a × c, ad := a × d, bc := b × c и bd := b × d
        ac = karatcuma(a, c)
        ad = karatcuma(a, d)
        bc = karatcuma(b, c)
        bd = karatcuma(b, d)
        # вычислить (10**n) * ac + (10**(n//2)) * (ad + bc) + bd,
        return (10**n) * ac + (10**(n//2)) * (ad + bc) + bd


print(rr)
print(karatcuma(num1, num2))

