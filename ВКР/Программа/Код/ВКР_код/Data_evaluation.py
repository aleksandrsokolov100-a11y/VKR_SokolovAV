import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk, messagebox


def plot_histograms(df):
    # Создаем новое окно для выбора столбца
    choice_window_plot_histograms = tk.Toplevel()
    choice_window_plot_histograms.title("Выбор столбца для гистограммы")

    tk.Label(choice_window_plot_histograms, text="Выберите фактор для построения:").pack(pady=10, padx=10)

    # Берем колонки
    columns = df.columns.tolist()

    if not columns:
        messagebox.showerror("Ошибка", "В данных нет числовых столбцов")
        choice_window_plot_histograms.destroy()
        return

    combobox = ttk.Combobox(choice_window_plot_histograms, values=columns, state="readonly")
    combobox.pack(pady=5, padx=10)
    combobox.current(0)

    def draw():
        selected_col = combobox.get()
        plt.figure(figsize=(12, 7))
        sns.histplot(df[selected_col], color='skyblue')
        plt.title(f'Распределение: {selected_col}')
        plt.xlabel(selected_col)
        plt.xticks(rotation=60)
        plt.ylabel('Частота')
        plt.grid(True, alpha=0.3)
        plt.show()

    tk.Button(choice_window_plot_histograms, text="Построить", command=draw).pack(pady=20)
    tk.Button(choice_window_plot_histograms, text="Закрыть окно", width=10,
              command=choice_window_plot_histograms.destroy).pack(pady=20)


def plot_correlation_matrix(df):
    # Матрица корреляции всех признаков
    plt.figure(figsize=(12, 7))
    # Выбираем только числовые колонки для корреляции
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr_matrix = numeric_df.corr()

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()


def plot_boxplots(df):
    # Диаграммы размаха для числовых метрик
    # Создание окна выбора
    select_window_plot_boxplots = tk.Toplevel()
    select_window_plot_boxplots.title("Выбор столбца для Boxplot")
    select_window_plot_boxplots.geometry("300x200")

    tk.Label(select_window_plot_boxplots, text="Выберите столбец:").pack(pady=10)

    # Список только числовых колонок
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    combobox = ttk.Combobox(select_window_plot_boxplots, values=numeric_cols, state="readonly")
    combobox.pack(pady=5)
    if numeric_cols:
        combobox.current(0)

    def show_plot():
        selected_col = combobox.get()
        if selected_col:
            plt.figure(figsize=(8, 6))
            sns.boxplot(y=df[selected_col])
            plt.title(f"Диаграмма размаха для {selected_col}")
            plt.show()

    tk.Button(select_window_plot_boxplots, text="Построить", command=show_plot).pack(pady=10)
    tk.Button(select_window_plot_boxplots, text="Закрыть окно", width=10,
              command=select_window_plot_boxplots.destroy).pack(pady=10)


def data_evaluation(df):
    # Основная функция оценки качества данных и вызова визуализаций
    # Создание окна результата
    eval_window = tk.Toplevel()
    eval_window.title("Оценка качества данных")
    eval_window.geometry("500x400")

    # Текстовое поле с прокруткой
    text_area = tk.Text(eval_window, wrap='word', font=('Consolas', 10))
    scrollbar = tk.Scrollbar(eval_window, command=text_area.yview)
    text_area.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    text_area.pack(side="left", fill="both", expand=True)

    # Сбор информации о данных
    info_str = "--- Общая информация ---\n"
    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str += buffer.getvalue()

    info_str += "\n--- Пропущенные значения ---\n"
    info_str += str(df.isnull().sum())

    info_str += "\n\n--- Статистическое описание ---\n"
    info_str += str(df.describe())

    # Вставка текста в окно
    text_area.insert("1.0", info_str)
    text_area.config(state="disabled")  # Запрет редактирования






