
class Video:
    def create(self, name: str):
        # метод сохраняет имя name в локальном атрибуте name объекта
        self.name = name
        
    def play(self):
        # метод выводит на экран строку "воспроизведение видео <name>"
        print(f'воспроизведение видео {self.name}')

        
class YouTube:
    videos = []
    
    @classmethod
    def add_video(cls, video):
        # для добавления нового видео (метод помещает объект video класса Video в список);
        cls.videos.append(video)
        
    @classmethod
    def play(cls, video_indx: int):
        # для проигрывания видео из списка по указанному индексу (индексация с нуля).
        cls.videos[video_indx].play()
        
v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python ООП")

YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)


class AppStore:
    lst_apps = []
    
    def add_application(self, app):
        # добавление нового приложения app в магазин;
        AppStore.lst_apps.append(app)
    
    def remove_application(self, app):
        # удаление приложения app из магазина;
        AppStore.lst_apps.remove(app)
    
    def block_application(self, app):
        # блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
        indx = AppStore.lst_apps.index(app)
        AppStore.lst_apps[indx].blocked = True
    
    def total_apps(self):
        # возвращает общее число приложений в магазине.
        return len(AppStore.lst_apps)
    
class Application:
    def __init__(self, name: str) -> None:
        self.name = name
        self.blocked = False
        


class Viber:
    
    msgs ={}
    
    @classmethod
    def add_message(cls, msg):
        # - добавление нового сообщения в список сообщений;
        cls.msgs[id(msg)] = msg
    
    @classmethod
    def remove_message(cls, msg):
        # - удаление сообщения из списка;
        key = id(msg)
        if key:
            cls.msgs.pop(key)
    
    @classmethod
    def set_like(cls, msg):
        #поставить/убрать лайк для сообщения msg (если лайка нет то он ставится, если уже есть, то убирается);
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, num):
        #(число) - отображение последних сообщений;
        for m in (cls.msgs.values())[-num:]:
            print(m)
    
    @classmethod
    def total_messages(cls):
        # - возвращает общее число сообщений.
        return len(cls.msgs)


class Message:
    def __init__(self, text) -> None:
        self.text = text
        self.fl_like = False

    
msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)




class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    server_ip = 1
    
    def __init__(self):
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.router = None

    def send_data(data):
        """для отправки информационного пакета data (объекта класса Data) 
        с указанным IP-адресом получателя (пакет отправляется роутеру и 
        сохраняется в его буфере - локальном свойстве buffer);
        """
    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было, 
        то возвращается пустой список) и очищает входной буфер;
        """
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.ip


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    def __init__(self) -> None:
        self.buffer = []
        self.servers = {}
    
    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        self.servers[server.ip] = server
        server.router = self
    
    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None
    
    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера 
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].buffer.append(d)
        self.buffer.clear()
    

class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """
    def __init__(self, msg, ip) -> None:
        self.data = msg
        self.ip = ip
        
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()