# -*- coding: utf-8 -*-
# Python 3.4.3
# Microsoft Windows XP
# NiNJA-IDE
"""
6. В программе генерируется случайное целое число от 0 до 100.
 Пользователь должен его отгадать не более чем за 10 попыток.
  После каждой неудачной попытки
  должно сообщаться больше или меньше введенное пользователем число,
   чем то, что загадано.
   Если за 10 попыток число не отгадано, то вывести загаданное число.
"""

# https://github.com/AlexVBodrov/self-education_of_Pyton/blob/main/guess_number_v1.py
# или
# https://github.com/AlexVBodrov/self-education_of_Pyton/blob/main/guess_number_v1.exe

import random
from tkinter import *
from tkinter import messagebox


def get_ask_number():
    global ask_number

    ask_number = random.randint(1, 100)
    return ask_number


ask_number = get_ask_number()
try_count = 10

def get_user_number():
    global try_count

    user_number = int(input_1.get())

    input_1.delete(0, END)
    if user_number == ask_number:
        messagebox.showinfo("Угадай число", "Поздравляю!! \n ВЫ Угадали, попробуйте снова")

        get_ask_number()
    elif user_number < ask_number:
        try_count -= 1
        lbl_result.config(text=f"Загадное число БОЛьШЕ вашего,\n попробуйте еще раз,"
                               f"\n осталось {try_count} попыток", font=("Arial Bold", 20))
        if try_count <= 0:
            lbl_result.config(text=" ")
            messagebox.showinfo("Угадай число", f"загаданно {ask_number},\n ВЫ проиграли, попробуйте снова")
            get_ask_number()
            try_count = 7

    else:
        try_count = try_count - 1
        lbl_result.config(text=f"Загадное число МЕНьШЕ вашего,\n попробуйте еще раз,"
                               f"\n осталось {try_count} попыток", font=("Arial Bold", 20))
        if try_count <= 0:
            lbl_result.config(text=" ")
            messagebox.showinfo("Угадай число", f"загаданно {ask_number},\n ВЫ проиграли, попробуйте снова")

            get_ask_number()
            try_count = 7
    return user_number

root = Tk()

root.minsize(470, 500)
root.title(" Угадай число")

lbl_head = Label(root, text="   Угадайте число от 1 до 100 :", font=("Arial Bold", 24))
lbl_head.grid(column=0, row=0)

input_1 = Entry(root, width=5, font=("Arial Bold", 24), justify=RIGHT)
input_1.grid(column=0, row=3)

btn_input = Button(root, text="Принять ответ", command=get_user_number, font="Arial 16")
btn_input.grid(column=0, row=4)

lbl_result = Label(root, text=" ", font=("Arial Bold", 20))
lbl_result.grid(column=0, row=5)


def answer_btn_2():
    messagebox.showinfo("Угадай число", f"загаданно {ask_number}")


btn_2 = Button(root, text="Показать ответ", command=answer_btn_2, font="Arial 16")
btn_2.grid(column=0, row=6)

root.mainloop()