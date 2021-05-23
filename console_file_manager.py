import os


def create_file(name: str, text=None):
    """ create new file """
    with open(name, "w", encoding='utf-8') as new_file:
        if text:
            new_file.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f"ОШИБКА !!! папка => {name} <= Уже была создана")


def delete_folder(name):
    try:
        os.rmdir(name)
    except FileNotFoundError:
        print(f"ОШИБКА !!! Не удается найти => {name} <= папку:")


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(*result, sep="\n")


if __name__ == "__main__":
    get_list()