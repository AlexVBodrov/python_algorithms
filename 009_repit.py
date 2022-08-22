class SmartPhone:
    # sm = SmartPhone(марка смартфона)
    def __init__(self, model) -> None:
        self.model = model  # - марка смартфона (строка);
        self.apps = []  # - список из установленных приложений (изначально пустой).

    def add_app(self, app):
        # - добавление нового приложения на смартфон (в конец списка apps);
        # При добавлении нового приложения проверять,
        # что оно отсутствует в списке apps
        # (отсутствует объект соответствующего класса).
        for obj in self.apps:
            if type(app) == type(obj):
                return False

        self.apps.append(app)

    def remove_app(self, app):
        # - удаление приложения по ссылке на объект app.
        self.apps.remove(app)


class VerifcationStrName:
    def __setattr__(self, key, value) -> None:
        if key == "name" and type(value) == str:
            super().__setattr__(key, value)


class AppVK(VerifcationStrName):
    # - класс приложения ВКонтаке;
    def __init__(self) -> None:
        self.name = "ВКонтакте"


class AppYouTube(VerifcationStrName):
    # - класс приложения YouTube;
    def __init__(self, memory_max=1024) -> None:
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone(VerifcationStrName):
    # - класс приложения телефона.
    def __init__(self, phone_list) -> None:
        self.name = "Phone"
        self.phone_list = phone_list


app_1 = AppVK()  # name = "ВКонтакте"
app_2 = AppYouTube(1024)  # name = "YouTube", memory_max = 1024
app_3 = AppPhone(
    {"dsadasd": 1234567890, "fdsaf": 98450647365, "fdasf": 112}
)  # name = "Phone", phone_list = словарь с контактами


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
