import tkinter as tk
from tkinter import ttk, messagebox
import Functions_directory
import Global_data
import os





def open_article_window(filename):
    #Создает окно с текстом статьи
    full_path = os.path.join(Global_data.g_link_papers_folder, filename)

    if not os.path.exists(full_path):
        messagebox.showerror("Ошибка", f"Файл {filename} не найден")
        return

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        title = lines[0].strip() if len(lines) > 0 else "Без названия"
        tags = lines[1].strip() if len(lines) > 1 else ""
        content = "".join(lines[2:]) if len(lines) > 2 else "Нет содержания"

        # Создание окна
        detail_window = tk.Toplevel()
        detail_window.title(title)
        detail_window.geometry("500x400")

        tk.Label(detail_window, text=title, font=("Arial", 14, "bold")).pack(pady=5)
        tk.Label(detail_window, text=f"Теги: {tags}", font=("Arial", 10, "italic")).pack(pady=2)

        text_area = tk.Text(detail_window, wrap="word", padx=10, pady=10)
        text_area.insert("1.0", content)
        text_area.config(state="disabled")  # Только для чтения
        text_area.pack(fill="both", expand=True)

        tk.Button(detail_window, text="Закрыть", command=detail_window.destroy).pack(pady=5)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось прочитать статью: {e}")


def get_all_tags():
    tags = set()
    for article in Global_data.g_articles_data:
        for tag in article["tags"]:
            if tag:
                tags.add(tag)
    return sorted(tags)


def filter_articles_by_tag(selected_tag):
    if not selected_tag or selected_tag == "Все":
        return Global_data.g_articles_data
    return [article for article in Global_data.g_articles_data if selected_tag in article["tags"]]


def update_articles_list(listbox, selected_tag):
    listbox.delete(0, tk.END)
    filtered = filter_articles_by_tag(selected_tag)

    for article in filtered:
        listbox.insert(tk.END, article["title"])


def create_main_interface():
    #Functions_directory.load_articles_catalog()

    root_create_main_interface = tk.Toplevel()
    root_create_main_interface.title("Статьи")
    root_create_main_interface.geometry("300x400")

    welcome_label = tk.Label(
        root_create_main_interface,
        text="Выбор тега статьи:",
        font=("Arial", 10),
        pady=20,
        justify="center"
    )
    welcome_label.pack()
    # Получаем все теги
    tags = ["Все"] + get_all_tags()

    # Выпадающий список тегов
    selected_tag = tk.StringVar(value="Все")
    tag_menu = tk.OptionMenu(root_create_main_interface, selected_tag, *tags)
    tag_menu.pack(pady=10)

    # Список статей
    articles_listbox = tk.Listbox(root_create_main_interface, width=80, height=20)
    articles_listbox.pack(fill="both", expand=True, padx=10, pady=10)

    def on_tag_change(*args):
        update_articles_list(articles_listbox, selected_tag.get())

    selected_tag.trace_add("write", on_tag_change)

    def on_article_double_click(event):
        selection = articles_listbox.curselection()
        if selection:
            article_title = articles_listbox.get(selection[0])
            for article in filter_articles_by_tag(selected_tag.get()):
                if article["title"] == article_title:
                    open_article_window(article["filename"])
                    break

    articles_listbox.bind("<Double-Button-1>", on_article_double_click)

    update_articles_list(articles_listbox, "Все")

    root_create_main_interface.mainloop()

