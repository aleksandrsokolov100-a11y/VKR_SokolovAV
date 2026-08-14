import tkinter as tk
from tkinter import messagebox

import GUI_Base_menu
import Work_with_SQL


# Открыть окно регистрации покупателя
def user_registration_window():
    root = tk.Tk()
    # Подпись окна
    root.title("Регистрация нового пользователя")
    # Метки и поля ввода
    # Метки поля ввода ФИО
    tk.Label(root, text="ФИО:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    # Создание поля ввода для ФИО
    entry1 = tk.Entry(root, width=30)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    # Метки поля ввода пароля
    tk.Label(root, text="Пароль:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    # Создание поля ввода для пароля
    entry2 = tk.Entry(root, width=30, show="*")  # show="*" - ввод отборажается звёздочками
    entry2.grid(row=1, column=1, padx=5, pady=5)

    # Обработчик кнопки "Ввод"
    def on_submit():
        try:
            user = entry1.get()
            pwd = entry2.get()
            if (Work_with_SQL.check_user_name(user) == False) and (user != "") and (pwd != ""):
                Work_with_SQL.create_new_user(user, pwd)
                messagebox.showinfo("Успех", "Создан новый аккаунт пользователя")
                root.destroy()
            else:
                # Сбрасываем поля и показываем сообщение о наличии уже такого пользователя
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                messagebox.showerror("Ошибка", "Ошибка, пользователь с указенным именем уже существует или некоторые поля не были заполнены")
                root.destroy()
        except Exception:
            messagebox.showerror("Ошибка", "Ошибка вода")
    # Кнопки
    btn_frame = tk.Frame(root)
    btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(btn_frame, text="Ввод", width=12, command=on_submit).pack(side="left", padx=10)
    root.mainloop()


def create_authorization_window():
    # Корень древа окон
    root = tk.Tk()
    # Подпись окна
    root.title("Вход / Регистрация")
    # Метки и поля ввода
    # Метки поля ввода ФИО
    tk.Label(root, text="ФИО:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    # Создание поля ввода для ФИО
    entry1 = tk.Entry(root, width=30)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    # Метки поля ввода пароля
    tk.Label(root, text="Пороль:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    # Создание поля ввода для пароля
    entry2 = tk.Entry(root, width=30, show="*")  # show="*" - ввод отборажается звёздочками
    entry2.grid(row=1, column=1, padx=5, pady=5)

    # Обработчик кнопки "Ввод"
    def on_submit():
        try:
            user = entry1.get()
            pwd = entry2.get()
            result = Work_with_SQL.check_user_credentials(user, pwd)
            if result:
                root.destroy()
                GUI_Base_menu.base_menu()
            else:
                # Сбрасываем поля и показываем сообщение об ошибке
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                messagebox.showerror("Ошибка", "Ошибка входа")
        except Exception:
            messagebox.showerror("Ошибка", "Ошибка вода")



    # Кнопки
    btn_frame = tk.Frame(root)
    btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(btn_frame, text="Создать аккаунт", width=22, command=user_registration_window).pack(side="left", padx=10)
    tk.Button(btn_frame, text="Ввод", width=12, command=on_submit).pack(side="left", padx=10)
    root.mainloop()

