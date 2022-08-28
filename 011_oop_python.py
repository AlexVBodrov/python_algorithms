from random import randint

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"


class RandomPassword:
    # rnd = RandomPassword(psw_chars, min_length, max_length)
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwds) -> str:
        num_in_range = randint(self.min_length, self.max_length)
        simbol = self.psw_chars[randint(0, len(self.psw_chars) - 1)]
        return "".join(simbol for _ in range(num_in_range))


rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd(), rnd(), rnd()]


class ImageFileAcceptor:
    # acceptor = ImageFileAcceptor(extensions)
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, namefile, *args, **kwds):
        if namefile.split(".")[-1] in self.extensions:
            return True


filenames = [
    "boat.jpg",
    "web.png",
    "text.txt",
    "python.doc",
    "ava.8.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.png",
    "my.html",
    "data.shtml",
]
extensions = ("jpg", "bmp", "jpeg")
acceptor = ImageFileAcceptor(extensions)
image_filenames = filter((acceptor), filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]


from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get("login", "")
        self.password = request.get("password", "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True

class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string, *args, **kwds):
        return self.min_length <= len(string) <= self.max_length

class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string, *args, **kwds):
        return set(string) <= set(self.chars)
