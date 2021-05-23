from core import copy_file, create_folder, create_file
from core import delete_file, save_info, get_list, change_dir
import sys

save_info("Старт")

try:
    command = sys.argv[1]
except IndexError:
    print("Необходимо ввести команду, или help => справка")
else:

    if command == "list":
        get_list()
    elif command == "create_file":
        try:
            name = sys.argv[2]
        except IndexError:
            print("Ошибка! введите название файла")
        else:
            create_file(name)
    elif command == "create_dir":
        try:
            name = sys.argv[2]
        except IndexError:
            print("Ошибка! введите название папки")
        else:
            create_folder(name)
    elif command == "chdir":
        try:
            name = sys.argv[2]
        except IndexError:
            print("Ошибка! введите название папки")
        else:
            change_dir(name)
    elif command == "delete":
        try:
            name = sys.argv[2]
        except IndexError:
            print("Ошибка! введите название файла")
        else:
            delete_file(name)
    elif command == "copy":
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print("Ошибка! введите название файла")
        else:
            copy_file(name, new_name)
    elif command == "help":
        print("help  => справка")
        print("list  =>  список файлов")
        print("create_file name  => создать файл: name")
        print("create_dir name  => создать dir: name")
        print("delete name => удалить файл: name")
        print("copy name new_name => скопировать файл: name в файл new_name")

save_info("Конец")
