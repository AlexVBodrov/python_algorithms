import os
import shutil
import datetime


def create_file(name: str, text=None):
    with open(name, "w", encoding='utf-8') as new_file:
        if text:
            new_file.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f"ОШИБКА !!! папка => {name} <= Уже была создана")


def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print(f"ОШИБКА !!! Не удается найти => {name} <= объект:")


def copy_file(name, new_name):
    try:
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
        else:
            shutil.copy(name, new_name)
    except FileExistsError:
        print("Error!! Can't COPY. File already create")


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(*result, sep="\n")


def save_info(message):
    current_time = datetime.datetime.now()
    result = f"{current_time} - {message}"
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())

if __name__ == "__main__":
    pass
