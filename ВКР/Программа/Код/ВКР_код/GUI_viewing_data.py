import tkinter as tk
import Global_data
import Data_evaluation

def interface_viewing_data():
    interface_load_data_root = tk.Tk()
    interface_load_data_root.title("Просмотр данных")
    interface_load_data_root.geometry("500x400")
    label = tk.Label(interface_load_data_root, text="Выберите тип визуализации:", font=('Arial', 12, 'bold'))
    label.pack(pady=20)
    tk.Button(interface_load_data_root, text="Гистограммы факторов", width=30,
              command=lambda: Data_evaluation.plot_histograms(Global_data.df)).pack(pady=5)

    tk.Button(interface_load_data_root, text="Матрица корреляции", width=30,
              command=lambda: Data_evaluation.plot_correlation_matrix(Global_data.df)).pack(pady=5)

    tk.Button(interface_load_data_root, text="Диаграммы размаха", width=30,
              command=lambda: Data_evaluation.plot_boxplots(Global_data.df)).pack(pady=5)

    tk.Button(interface_load_data_root, text="Оценка качества данных", width=30,
              command=lambda: Data_evaluation.data_evaluation(Global_data.df)).pack(pady=5)

    tk.Button(interface_load_data_root, text="Закрыть окно", width=25,
              command=interface_load_data_root.destroy).pack(pady=5)


    return








