import random
import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
from tkinter import *


# Функция для старта новой игры
def new_game():
    global secret_number
    secret_number = random.randint(1, 100)  # Генерация случайного числа
    result_label.config(
        text="Попробуй угадать число от 1 до 100!")  # Обновляем подсказку
    guess_entry.delete(0, tk.END)  # Очищаем поле ввода


# Функция для проверки числа
def check_guess():
    try:
        guess = int(guess_entry.get())  # Ввод пользователя
        if guess < secret_number:
            result_label.config(text="Мое число больше!")
            guess_entry.delete(0, tk.END)  #Отчистка после попытки
        elif guess > secret_number:
            result_label.config(text="Мое число меньше!")
            guess_entry.delete(0, tk.END)  ##Отчистка после попытки
        else:
            messagebox.showinfo("Поздравляю!",
                                f"Ты угадал число: {secret_number}!")
            new_game()  # Начинаем новую игру
    except ValueError:
        result_label.config(text="Введите корректное число!",
                            foreground="red")  # Если ввод некорректный
        guess_entry.delete(0, tk.END)  ##Отчистка после попытки


# Создаем главное окно
root = tk.Tk()
root.grid = "NSEW"
root.title("Угадай число")
root.geometry("500x225+700+300")
root.resizable(1, 1)
root.configure(bg="lightblue")
################################################################

# выбранная тема
selected_theme = StringVar()
style = ttk.Style()

# изменение текущей темы
def change_theme(event=None):
    style.theme_use(selected_theme.get())

# выпадающий список с темами
ttk.Label(text="Выберите тему:", font="Helvetica 13").pack(anchor=NW, padx=10, pady=5)
theme_combobox = ttk.Combobox(root, textvariable=selected_theme, values=style.theme_names(), state="readonly")
theme_combobox.pack(anchor=NW, padx=10, pady=5)
theme_combobox.bind("<<ComboboxSelected>>", change_theme)

# Установим начальную тему
selected_theme.set(style.theme_use())

# Настраиваем интерфейс
instruction_label = tk.Label(root,
                             text="Добро пожаловать в игру 'Угадай число'!")
instruction_label.pack(fill="x")
instruction_label.pack()

guess_entry = ttk.Entry(root, font=("Arial", 19))  # Поле ввода
guess_entry.pack(fill="x")
guess_entry.pack()

check_button = ttk.Button(
    root,
    text="Проверить",
    cursor="hand2",
    command=check_guess,
)  # Кнопка проверки
check_button.pack(fill="x")
check_button.pack()

result_label = tk.Label(root,
                        text="Попробуй угадать число от 1 до 100!",
                        foreground="green")
result_label.pack(fill="x")
result_label.pack()

new_game_button = ttk.Button(root,
                             text="Новая игра",
                             cursor="hand2",
                             command=new_game)  # Кнопка новой игры
new_game_button.pack(fill="x")
new_game_button.pack()

style_button = ttk.Button(text="Темы")
style_button.pack

# Запускаем первую игру
new_game()

# Запускаем главный цикл интерфейса
root.mainloop()
