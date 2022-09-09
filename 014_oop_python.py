class Handler:
    def __init__(self, methods=('GET', )):
        # здесь нужные строчки
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            # здесь нужные строчки
            method = request.get('method', 'GET')
            if method in self.methods:
                method_name = method.lower()
                return self.__getattribute__(method_name)(func, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        # - для имитации обработки GET-запроса
        return f'GET: {func(request)}'


    def post(self, func, request, *args, **kwargs):
        # - для имитации обработки POST-запроса
        return f'POST: {func(request)}'


class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        result = list(map(int, self.func().split(' ')))
        return result


input_dg = InputDigits(input)
res = input_dg()


class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        # здесь строчки программы
        self.__render = render

    def __call__(self, func, *args, **kwargs):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            # здесь строчки программы
            return list(map(self.__render, func(*args, **kwargs).split()))
        return wrapper


class RenderDigit:
    
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return None


render = RenderDigit()
input_dg =  InputValues(render)(input)  
res = input_dg()
print(res)  
