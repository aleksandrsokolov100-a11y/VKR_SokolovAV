import tkinter as tk
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog
import os


import Import_data
import Global_data
import Data_preparation


def load_data_from_SQL():
    Global_data.df = Import_data.import_data_from_SQL()
    if (isinstance(Global_data.df, pd.DataFrame)):
        messagebox.showinfo("Успех", "Данные загружены")
    else:
        messagebox.showerror("Ошибка", "Данные не были загружены")
    return


def get_file_data():
    """Функция для вызова диалога выбора файла и обработки пути."""
    file_path_full = filedialog.askopenfilename(
        title="Выберите CSV файл",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )

    if file_path_full:
        # Разделяем полный путь на директорию и имя файла
        path = os.path.dirname(file_path_full)
        name_file = os.path.basename(file_path_full)

        # Вывод результата для проверки
        #print(f'path = r"{path}"')
        #print(f'name_file = "{name_file}"')

        return path, name_file
    return None, None


def load_data_from_local_disk():
    load_data_from_local_disk_root = tk.Tk()
    load_data_from_local_disk_root.title("Выбор данных")
    load_data_from_local_disk_root.geometry("300x150")

    def on_button_click():
        path, name_file = get_file_data()
        if(path == None) and (name_file == None):
            messagebox.showerror("Ошибка", "Данные не были загружены")
            load_data_from_local_disk_root.destroy()
        else:
            try:
                Global_data.df = Import_data.import_data_from_local_disc(path, name_file)
                messagebox.showinfo("Успех", "Данные загружены")
                load_data_from_local_disk_root.destroy()
            except Exception as e:
                messagebox.showerror("Ошибка", "Данные не были загружены")
                load_data_from_local_disk_root.destroy()


    btn = tk.Button(load_data_from_local_disk_root, text="Выбрать CSV файл", command=on_button_click)
    btn.pack(expand=True)

    btn_exit = tk.Button(load_data_from_local_disk_root, text="Закрыть", command=load_data_from_local_disk_root.destroy)
    btn_exit.pack(expand=True)

    load_data_from_local_disk_root.mainloop()


def load_data_from_website():
    load_data_from_website_root = tk.Tk()
    load_data_from_website_root.title("Загрузка с сайта")
    load_data_from_website_root.geometry("350x100")

    tk.Label(load_data_from_website_root, text="Полная ссыслка на сайт").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry1 = tk.Entry(load_data_from_website_root, width=50)
    # entry1.focus_set()
    # Поддержка вставки по Ctrl+V
    entry1.bind("<Control-v>", lambda e: entry1.event_generate("<<Paste>>"))
    entry1.grid(row=1, column=0, padx=5, pady=5)


    # Обработчик кнопки "Ввод"
    def on_submit():
        try:
            url = entry1.get()
            #print(url)
            find_url, Global_data.df = Import_data.import_data_from_kaggle(url)
            if(find_url):
                messagebox.showinfo("Успех", "Данные загружены")
                load_data_from_website_root.destroy()
            else:
                entry1.delete(0, tk.END)
                messagebox.showerror("Ошибка", "Данные не были загружены")
        except Exception:
            messagebox.showerror("Ошибка", "Ошибка вода")
    # Кнопки
    btn_frame = tk.Frame(load_data_from_website_root)
    btn_frame.grid(row=3, column=0, columnspan=1, pady=10)
    tk.Button(btn_frame, text="Ввод", width=22, command=on_submit).pack(side="left", padx=10)
    tk.Button(btn_frame, text="Закрыть", width=12, command=load_data_from_website_root.destroy).pack(side="left", padx=10)



def messege_about_preparation_data():
    # Проверим, что данные имеют все требуемые столбцы и не более
    if(Data_preparation.check_df_name_column(Global_data.df)) and (len(Global_data.df.columns) == len(Global_data.name_columns_df)):
        messagebox.showinfo("Столбцы", "Загруженные данные сответствуют требованиям по столбцам")
        Global_data.data_status = True
    else:
        messagebox.showerror("Ошибка", "Загруженные данные не соответствуют требованиям по столбцам")
        return
    information_about_clean_data = Data_preparation.starting_data_preparation(Global_data.df)
    string_about_clean_data = "При проведении очистки данных были удаленны следующие записи:\n"
    string_about_clean_data = string_about_clean_data + "Удаленные дубликаты: " + str(information_about_clean_data["duplicates_removed"]) + "\n"
    string_about_clean_data = string_about_clean_data + "Удаленные строк с некоректной записью: " + str(information_about_clean_data["invalid_input_removed"]) + "\n"
    string_about_clean_data = string_about_clean_data + "Удаленные строк с ошибкой в логикой: " + str(information_about_clean_data["logical_inconsistency_removed"]) + "\n"
    string_about_clean_data = string_about_clean_data + "Записей осталось: " + str(len(Global_data.df)) + "\n"
    messagebox.showinfo("Очистка данных", string_about_clean_data)




def interface_load_data():
    interface_load_data_root = tk.Tk()
    interface_load_data_root.title("Предсказание рака легких")
    interface_load_data_root.geometry("500x400")

    # 1) Поле с приветственным текстом
    welcome_label = tk.Label(
        interface_load_data_root,
        text="Меню выбора метода загрузки данных",
        font=("Arial", 16, "bold"),
        pady=40,
        justify="center"
    )
    welcome_label.pack()

    # Создание контейнера для кнопок
    button_frame = tk.Frame(interface_load_data_root)
    button_frame.pack(pady=10)

    # 2) Кнопка "Загрузка данных с локального диска"
    btn_load = tk.Button(
        button_frame,
        text="Загрузка данных с локального диска",
        width=40,
        command=load_data_from_local_disk
    )
    btn_load.pack(pady=5)

    # 3) Кнопка "Загрузка данных из базы данных"
    btn_view = tk.Button(
        button_frame,
        text="Загрузка данных из базы данных",
        width=40,
        command=load_data_from_SQL
    )
    btn_view.pack(pady=5)

    # 4) Кнопка "Загрузка данных с сайта"
    btn_nn = tk.Button(
        button_frame,
        text="Загрузка данных с сайта",
        width=40,
        command=load_data_from_website
    )
    btn_nn.pack(pady=5)


    # 5) Кнопка "Подготовить данные"
    btn_ref = tk.Button(
        button_frame,
        text="Подготовить данные",
        width=40,
        command=messege_about_preparation_data
    )
    btn_ref.pack(pady=5)

    # 6) Кнопка "Закрыть окно"
    btn_6 = tk.Button(
        button_frame,
        text="Закрыть окно",
        width=25,
        command=interface_load_data_root.destroy
    )
    btn_6.pack(pady=5)

    interface_load_data_root.mainloop()















