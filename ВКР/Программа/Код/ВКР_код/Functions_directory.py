import tkinter as tk
from tkinter import messagebox
import os
import Global_data


def load_articles_catalog():
    #Считывает каталог статей и сохраняет информацию в Global_data
    file_path = os.path.join(Global_data.g_link_papers_folder, Global_data.g_name_file_catalog)
    Global_data.g_articles_data = []

    if not os.path.exists(file_path):
        print(f"Файл каталога {file_path} не найден.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        # Текст структурирован по 3 строки на статью
        for i in range(0, len(lines), 3):
            if i + 2 < len(lines):
                title = lines[i]
                tags = [tag.strip() for tag in lines[i + 1].split(',')]
                filename = lines[i + 2]

                # Если в каталоге имя файла без расширения, добавляем .txt
                if not filename.endswith('.txt'):
                    filename += '.txt'

                Global_data.g_articles_data.append({
                    "title": title,
                    "tags": tags,
                    "filename": filename
                })
    except Exception as e:
        print(f"Ошибка при чтении каталога: {e}")








