class DigitRetrieve:
    # dg = DigitRetrieve()
    def __call__(self, string: str, *args, **kwds):
        if string.isdigit() or (string[0] == "-" and string[1:].isdigit()):
            return int(string)


# С помощью объектов класса DigitRetrieve должно выполняться преобразование чисел из списка строк следующим образом:
dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digit
s = list(map(dg, st))  # [123, None, None, 0, -5]
# print(digits)


# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# =>
"""<ul>
<li>Пункт меню 1</li>
<li>Пункт меню 2</li>
<li>Пункт меню 3</li>
</ul>"""


class RenderList:
    # render = RenderList(type_list)
    def __init__(self, type_list) -> None:
        if type_list != "ol":
            type_list = "ul"
        else:
            type_list = "ol"
        self.type_list = type_list

    def __call__(self, lst, *args, **kwds):
        lst_tag = f"{self.type_list}"
        render_str = f"<{lst_tag}>"
        for el in lst:
            render_str += f"<li>{el}</li>"
        render_str += f"</{lst_tag}>"
        return render_str


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)


class HandlerGET:
    # res = contact({"method": "GET", "url": "contact.html"})
    # должна возвращаться строка в формате: "GET: <данные из функции>"
    def __init__(self, func):
        self.func = func

    def get(self, func, request):
        return f"GET: {func(request)}"

    def __call__(self, request, *args, **kwargs):
        method = request.get("method", "GET")
        if method == "GET":
            return self.get(self.func, request)
        return None


@HandlerGET
def contact(request):
    return "Name User"


res = contact({"method": "GET", "url": "contact.html"})
print(res)  # GET: Name User
res = contact({"method": "POST", "url": "contact.html"})
print(res)  # None
res = contact({"url": "contact.html"})
print(res)  # GET: Name User
