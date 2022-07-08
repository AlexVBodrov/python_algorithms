
def calculate():
    exit_ = ''
    while( exit_ != 'e'):
        num1 = input('input num1 =  ')
        sign = input('input operator =  ')
        num2 = input('input num2 =  ')
        try:
            print(eval(f'{num1} {sign} {num2}'))
        except (SyntaxError, ZeroDivisionError, Exception) as e:
            print(e)
        exit_ = input('for Exit input => "e" key, or some_key  for calulate ')


if __name__ ==  "__main__":
    calculate()
    # help(eval)
    # help('return')