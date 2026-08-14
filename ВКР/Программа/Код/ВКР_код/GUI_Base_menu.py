import tkinter as tk

import GUI_load_data
import GUI_viewing_data
import GUI_neural_networks
import GUI_functions_directory

def on_button_click(button_name):
    print(f"Кнопка '{button_name}' нажата")









def base_menu():
    base_menu_root = tk.Tk()
    base_menu_root.title("Предсказание рака легких")
    base_menu_root.geometry("500x400")

    # 1) Поле с приветственным текстом
    welcome_label = tk.Label(
        base_menu_root,
        text="Приветствуем в приложении для\nпредсказания рака лёгких",
        font=("Arial", 16, "bold"),
        pady=20,
        justify="center"
    )
    welcome_label.pack()

    # Создание контейнера для кнопок
    button_frame = tk.Frame(base_menu_root)
    button_frame.pack(pady=10)

    # 2) Кнопка "Загрузка данных"
    btn_load = tk.Button(
        button_frame,
        text="Загрузка данных",
        width=25,
        command=GUI_load_data.interface_load_data
    )
    btn_load.pack(pady=5)

    # 3) Кнопка "Просмотр данных"
    btn_view = tk.Button(
        button_frame,
        text="Просмотр данных",
        width=25,
        command=GUI_viewing_data.interface_viewing_data
    )
    btn_view.pack(pady=5)

    # 4) Кнопка "Нейронные сети"
    btn_nn = tk.Button(
        button_frame,
        text="Нейронные сети",
        width=25,
        command= GUI_neural_networks.base_neural_menu
    )
    btn_nn.pack(pady=5)

    # 5) Кнопка "Справочник"
    btn_ref = tk.Button(
        button_frame,
        text="Справочник",
        width=25,
        command=GUI_functions_directory.create_main_interface
    )
    btn_ref.pack(pady=5)
    base_menu_root.mainloop()















