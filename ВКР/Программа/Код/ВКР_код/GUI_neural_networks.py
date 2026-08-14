import tkinter as tk
from tkinter import filedialog
import Global_data
from tkinter import ttk
import pandas as pd
import pickle
from tkinter import messagebox
from sklearn.metrics import recall_score, f1_score, classification_report
import Neural_networks
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import GUI_functions_directory



def save_selected_model():
    #Словарь доступных моделей
    models = {
        "Модель наличия рака": Global_data.g_model_pipeline_presence_cancer,
        "Модель риска смерти": Global_data.g_risk_model,
        "Модель выживание 5 лет": Global_data.g_survival_model,
        "Модель типа рака": Global_data.g_cancer_model,
        "Модель типа мутации": Global_data.g_mutation_model
    }


    # Окно выбора модели
    select_model_window = tk.Toplevel()
    select_model_window.title("Выбор модели для сохранения")
    select_model_window.geometry("400x260")

    tk.Label(select_model_window, text="Выберите нейронную сеть для сохранения:").pack(pady=10)

    selected_model_name = tk.StringVar(value="Модель наличия рака")
    #selected_model_name = tk.StringVar(value=models)

    for model_name in models.keys():
        tk.Radiobutton(
            select_model_window,
            text=model_name,
            variable=selected_model_name,
            value=model_name
        ).pack(anchor="w")

    def confirm_save():
        model_name = selected_model_name.get()
        model = models[model_name]

        # Проверка на None
        if (model is None) or (model == 0):
            messagebox.showerror("Ошибка", "Нейронной сети не существует.")
            return

        # Выбор файла для сохранения
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pkl",
            filetypes=[("Pickle files", "*.pkl"), ("All files", "*.*")]
        )

        if not file_path:
            return

        try:
            with open(file_path, "wb") as f:
                pickle.dump(model, f)

            messagebox.showinfo("Успех", f"Нейронная сеть '{model_name}' успешно сохранена.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить модель: {e}")

    tk.Button(select_model_window, text="Сохранить", command=confirm_save).pack(pady=5)
    btn_exit = tk.Button(select_model_window, text="Закрыть", command=select_model_window.destroy)
    btn_exit.pack(expand=True)
    select_model_window.mainloop()





# Функция интерфейса для импорта модели нейронной сети из .pkl файла
def load_neural_model_interface():
    # Создание окна
    #load_neural_model_interface_root = tk.Tk()
    load_neural_model_interface_root = tk.Toplevel()
    load_neural_model_interface_root.title("Импорт модели нейронной сети")
    load_neural_model_interface_root.geometry("400x300")

    # Перечень доступных моделей (ключи для словаря)
    models = {
        "Модель наличия рака": Global_data.g_model_pipeline_presence_cancer,
        "Модель риска смерти": Global_data.g_risk_model,
        "Модель выживание 5 лет": Global_data.g_survival_model,
        "Модель типа рака": Global_data.g_cancer_model,
        "Модель типа мутации": Global_data.g_mutation_model
    }

    tk.Label(load_neural_model_interface_root, text="Выберите целевую модель для замены:").pack(pady=10)

    # Выпадающий список для выбора, в какую переменную сохранить
    selected_model_key = tk.StringVar()
    # combobox = ttk.Combobox(load_neural_model_interface_root, textvariable=selected_model_key, values=model_keys, state="readonly", width=35)
    for model_name in models.keys():
        tk.Radiobutton(
            load_neural_model_interface_root,
            text=model_name,
            variable=selected_model_key,
            value=model_name
        ).pack(anchor="w")


    def on_import_click():
        target_key = selected_model_key.get()


        # Вызов диалога выбора файла
        file_path = filedialog.askopenfilename(
            title="Выберите модель (.pkl)",
            filetypes=(("Pickle files", "*.pkl"), ("All files", "*.*"))
        )

        if not file_path:
            messagebox.showwarning("Внимание", "Файл не был выбран")
            return

        try:
            # Загрузка модели из файла
            with open(file_path, 'rb') as f:
                loaded_model = pickle.load(f)


            if(target_key == "Модель наличия рака"):
                Global_data.g_model_pipeline_presence_cancer = loaded_model
            elif(target_key == "Модель риска смерти"):
                Global_data.g_risk_model = loaded_model
            elif (target_key == "Модель выживание 5 лет"):
                Global_data.g_survival_model = loaded_model
            elif (target_key == "Модель типа рака"):
                Global_data.g_cancer_model = loaded_model
            elif (target_key == "Модель типа мутации"):
                Global_data.g_mutation_model = loaded_model
            #model_name = models_dict[target_key]
            #model = models[model_name]

            # Сохранение загруженной модели в аттрибут класса Global_data
            #attr_name = models_dict[target_key]
            #setattr(Global_data, attr_name, loaded_model)

            messagebox.showinfo("Успех", f"Модель загружена и сохранена в {target_key}")
            load_neural_model_interface_root.destroy()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить модель: {e}")

    # Кнопки управления
    btn_import = tk.Button(load_neural_model_interface_root, text="Выбрать файл и импортировать", command=on_import_click, bg="#e1e1e1")
    btn_import.pack(pady=20)

    btn_exit = tk.Button(load_neural_model_interface_root, text="Отмена", command=load_neural_model_interface_root.destroy)
    btn_exit.pack(pady=5)

    load_neural_model_interface_root.mainloop()

# Функция тестирования моделей
def evaluate_models_interface():
    # Создание основного окна
    evaluate_models_interface_root = tk.Toplevel()
    evaluate_models_interface_root.title("Оценка качества нейронных сетей")
    evaluate_models_interface_root.geometry("450x300")
    # Интерфейсные элементы
    tk.Label(evaluate_models_interface_root, text="Выберите нейронную сеть для тестирования:", font=("Arial", 10)).pack(pady=10)

    model_options = [
        "Модель наличия рака",
        "Модель риска смерти",
        "Модель выживание 5 лет",
        "Модель типа рака",
        "Модель типа мутации"
    ]

    target_columns = [
        "Final_Prediction",
        "Mortality_Risk",
        "5_Year_Survival_Probability",
        "Cancer_Type",
        "Mutation_Type"
    ]


    models = {
        "Модель наличия рака": Global_data.g_model_pipeline_presence_cancer,
        "Модель риска смерти": Global_data.g_risk_model,
        "Модель выживание 5 лет": Global_data.g_survival_model,
        "Модель типа рака": Global_data.g_cancer_model,
        "Модель типа мутации": Global_data.g_mutation_model
    }


    # Выпадающий список для выбора, в какую переменную сохранить
    selected_model_name = tk.StringVar()
    # combobox = ttk.Combobox(load_neural_model_interface_root, textvariable=selected_model_key, values=model_keys, state="readonly", width=35)
    for model_name in models.keys():
        tk.Radiobutton(
            evaluate_models_interface_root,
            text=model_name,
            variable=selected_model_name,
            value=model_name
        ).pack(anchor="w")





    def run_testing():
        try:
            # Проверка наличия данных в Global_data
            if not hasattr(Global_data, 'df') or Global_data.df is None:
                messagebox.showerror("Ошибка", "Данные (Global_data.df) не загружены!")
                return


            current_name = selected_model_name.get()
            model = models[current_name]



            # Проверка наличия самой модели
            if model is None:
                messagebox.showerror("Ошибка", f"Модель '{current_name}' не инициализирована (None)!")
                return

            # 3. Разделение на X и y (согласно 2.txt через индекс)
            idx = model_options.index(current_name)
            target_col = target_columns[idx]

            if target_col not in Global_data.df.columns:
                messagebox.showerror("Ошибка", f"Столбец '{target_col}' не найден в данных!")
                return



            #df = Global_data.df.copy()
            df = Global_data.df.copy()
            y_true = df[target_col]
            X = df.drop(columns=[target_col])

            # Получение предсказаний
            y_pred = model.predict(X)
            if set(y_pred).issubset({0, 1}):
                y_pred = ["No" if x == 0 else "Yes" for x in y_pred]
            # Если предсказания непрерывные, считаем это регрессией
            is_regression_like = (
                np.issubdtype(np.array(y_pred).dtype, np.floating)
            )
            if is_regression_like:
                y_true_arr = np.array(y_true)
                y_pred_arr = np.array(y_pred, dtype=float)

                mse = mean_squared_error(y_true_arr, y_pred_arr)
                mae = mean_absolute_error(y_true_arr, y_pred_arr)
                rmse = np.sqrt(mse)
                r2 = r2_score(y_true_arr, y_pred_arr)

                result_window = tk.Toplevel(evaluate_models_interface_root)
                result_window.title(f"Отчет: {current_name}")
                result_window.geometry("500x400")

                text_area = tk.Text(result_window, wrap=tk.NONE, font=("Courier New", 10))
                text_area.pack(expand=True, fill='both', padx=10, pady=10)

                res_text = f"РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ\n"
                res_text += f"Модель: {current_name}\n"
                res_text += f"Целевой столбец: {target_col}\n"
                res_text += "-" * 40 + "\n"
                res_text += f"MSE:  {mse:.4f}\n"
                res_text += f"MAE:  {mae:.4f}\n"
                res_text += f"RMSE: {rmse:.4f}\n"
                res_text += f"R2:   {r2:.4f}\n"

                text_area.insert(tk.END, res_text)
                text_area.config(state=tk.DISABLED)
            else:
                # 4. Расчет метрик
                rec = recall_score(y_true, y_pred, average='weighted')
                f1 = f1_score(y_true, y_pred, average='weighted')
                report = classification_report(y_true, y_pred)

                # 5. Вывод результатов в новом окне
                result_window = tk.Toplevel(evaluate_models_interface_root)
                result_window.title(f"Отчет: {current_name}")
                result_window.geometry("500x400")

                text_area = tk.Text(result_window, wrap=tk.NONE, font=("Courier New", 10))
                text_area.pack(expand=True, fill='both', padx=10, pady=10)

                res_text = f"РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ\n"
                res_text += f"Модель: {current_name}\n"
                res_text += f"Целевой столбец: {target_col}\n"
                res_text += "-" * 40 + "\n"
                res_text += f"Weighted Recall:   {rec:.4f}\n"
                res_text += f"Weighted F1-Score: {f1:.4f}\n"
                res_text += "-" * 40 + "\n"
                res_text += "ДЕТАЛЬНЫЙ ОТЧЕТ (Scikit-Learn):\n"
                res_text += report

                text_area.insert(tk.END, res_text)
                text_area.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("Ошибка тестирования", f"Критическая ошибка: {e}")

    # Кнопки управления
    btn_start = tk.Button(evaluate_models_interface_root, text="Запустить тестирование", command=run_testing,
                          bg="#d1e7dd", width=25, font=("Arial", 9, "bold"))
    btn_start.pack(pady=20)

    btn_close = tk.Button(evaluate_models_interface_root, text="Закрыть окно", command=evaluate_models_interface_root.destroy, width=25)
    btn_close.pack(pady=5)

    evaluate_models_interface_root.mainloop()







def command_create_presence_cancer_model():
    Global_data.g_model_pipeline_presence_cancer = Neural_networks.create_presence_cancer_model(Global_data.df)
    if Global_data.g_model_pipeline_presence_cancer is None:
        messagebox.showerror("Ошибка", "Модель не созданна!")
        return
    messagebox.showinfo("Успех", "Модель созданна")
    #print("Обученно")
    return

def command_create_risk_model_g_risk_model():
    Global_data.g_risk_model = Neural_networks.create_risk_model(Global_data.df, "Mortality_Risk")
    return

def command_create_risk_model_g_survival_model():
    Global_data.g_survival_model = Neural_networks.create_risk_model(Global_data.df, "5_Year_Survival_Probability")
    return

def command_create_categorical_model_g_cancer_model():
    Global_data.g_cancer_model = Neural_networks.create_categorical_model(Global_data.df, "Cancer_Type")
    return

def command_create_categorical_model_g_mutation_model():
    Global_data.g_mutation_model = Neural_networks.create_categorical_model(Global_data.df, "Mutation_Type")
    return




def create_neural_menu():
    create_neural_menu_root = tk.Tk()
    create_neural_menu_root.title("Меню создания нейронных сетей")
    create_neural_menu_root.geometry("500x500")

    welcome_label = tk.Label(
        create_neural_menu_root,
        text="Выберите кукую нецронную сеть, \nвы желаете обучить",
        font=("Arial", 16, "bold"),
        pady=20,
        justify="center"
    )
    welcome_label.pack()

    # Создание контейнера для кнопок
    button_frame = tk.Frame(create_neural_menu_root)
    button_frame.pack(pady=10)

    btn_load = tk.Button(
        button_frame,
        text="Создать нецронную сеть \nопределяющая наличие рака",
        width=30,
        command=command_create_presence_cancer_model
    )
    btn_load.pack(pady=5)

    btn_view = tk.Button(
        button_frame,
        text="Создать нецронную сеть \nопределяющая вероятность смерти",
        width=30,
        command=command_create_risk_model_g_risk_model
    )
    btn_view.pack(pady=5)

    btn_nn = tk.Button(
        button_frame,
        text="Создать нецронную сеть \nопределяющая вероятность \nвыживание в течении 5 лет",
        width=30,
        command=command_create_risk_model_g_survival_model
    )
    btn_nn.pack(pady=5)

    btn_ref = tk.Button(
        button_frame,
        text="Создать нецронную сеть \nопределяющая тип рака",
        width=30,
        command=command_create_categorical_model_g_cancer_model
    )
    btn_ref.pack(pady=5)

    btn_ref = tk.Button(
        button_frame,
        text="Создать нецронную сеть \nопределяющая тип мутации",
        width=30,
        command=command_create_categorical_model_g_mutation_model
    )
    btn_ref.pack(pady=5)

    btn_ref = tk.Button(
        button_frame,
        text="Закрыть окно",
        width=30,
        command=create_neural_menu_root.destroy
    )
    btn_ref.pack(pady=5)
    create_neural_menu_root.mainloop()






def get_most_probable_value(column_name, df):
    # Возвращает наиболее вероятное значение столбца.
    # Для числовых - мода, если нет моды, медиана.
    # Для категориальных - мода.
    series = df[column_name].dropna()

    if len(series) == 0:
        return None

    mode_vals = series.mode()
    if len(mode_vals) > 0:
        return mode_vals.iloc[0]
    if pd.api.types.is_numeric_dtype(series):
        return series.median()


    return series.iloc[0]


def prepare_input_row(feature_columns, input_vars, df, all_columns):
    # Формирует одну строку данных для предсказания.
    # Все None заменяются наиболее вероятными значениями.
    data = {}
    for col in all_columns:
        val = input_vars[col].get()
        if val == "None":
            data[col] = get_most_probable_value(col, df)

    for col in feature_columns:
        val = input_vars[col].get()

        if val == "None":
            data[col] = get_most_probable_value(col, df)
        else:
            if col == "Age":
                try:
                    age_value = int(val)
                    if age_value < 30 or age_value > 90:
                        raise ValueError
                    data[col] = age_value
                except Exception:
                    raise ValueError("Поле Age должно быть числом от 30 до 90")
            else:
                # Пытаемся привести к нужному типу как в df
                if pd.api.types.is_numeric_dtype(df[col]):
                    try:
                        if pd.api.types.is_integer_dtype(df[col]):
                            data[col] = int(val)
                        else:
                            data[col] = float(val)
                    except Exception:
                        data[col] = val
                else:
                    data[col] = val

    return pd.DataFrame([data])


def format_prediction_result(model_name, model, X_input, input_vars, feature_columns):

    # Выполняет предсказание и возвращает текст результата.
    result_text = []
    result_text.append(f"Выбранная модель: {model_name}\n")

    result_text.append("Использованные входные данные:\n")
    for col in feature_columns:
        result_text.append(f"{col}: {input_vars[col].get()}")
    #for col in X_input.columns:
    #    result_text.append(f"{col}: {X_input.iloc[0][col]}")
    result_text.append("")
    prediction = model.predict(X_input)

    # Если модель умеет predict_proba
    probabilities_text = ""
    if hasattr(model, "predict_proba"):
        try:
            proba = model.predict_proba(X_input)[0]
            classes = None

            if hasattr(model, "named_steps") and "classifier" in model.named_steps:
                classifier = model.named_steps["classifier"]
                if hasattr(classifier, "classes_"):
                    classes = classifier.classes_
            elif hasattr(model, "classes_"):
                classes = model.classes_

            probabilities_text += "\nВероятности классов:\n"
            if classes is not None:
                for cls, p in zip(classes, proba):
                    probabilities_text += f"{cls}: {p:.4f}\n"
            else:
                for i, p in enumerate(proba):
                    probabilities_text += f"Класс {i}: {p:.4f}\n"
        except Exception:
            pass

    result_text.append("Результат предсказания:")
    result_text.append(str(prediction[0]))

    if probabilities_text:
        result_text.append(probabilities_text)

    return "\n".join(result_text)


def prediction_interface():
    # Проверка наличия датафрейма
    if not hasattr(Global_data, "df") or Global_data.df is None or len(Global_data.df) == 0:
        messagebox.showerror("Ошибка", "Global_data.df не найден или пуст")
        return

    df = Global_data.df.copy()

    # Словарь моделей
    models = {
        "Модель наличия рака": Global_data.g_model_pipeline_presence_cancer,
        "Модель риска смерти": Global_data.g_risk_model,
        "Модель выживание 5 лет": Global_data.g_survival_model,
        "Модель типа рака": Global_data.g_cancer_model,
        "Модель типа мутации": Global_data.g_mutation_model
    }

    # Создание главного окна
    prediction_interface_root = tk.Toplevel()
    prediction_interface_root.title("Интерфейс предсказания")
    prediction_interface_root.geometry("550x700")

    # Скроллируемая область (прокрутка экрана)
    # ---
    main_frame = tk.Frame(prediction_interface_root)
    main_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scrollable_frame, text="Выберите значения признаков, учтите, \nчто значение none может существенно \nуменьшить точность", font=("Arial", 14, "bold")).pack(pady=10)
    # ---


    # Хранилище переменных интерфейса
    input_vars = {}

    # Определение типов колонок
    all_columns = list(df.columns)

    target_columns = [
        "Mortality_Risk",
        "5_Year_Survival_Probability",
    ]
    #feature_columns = [col for col in all_columns if col not in target_columns]
    feature_columns = [col for col in all_columns]

    # Создание полей для заполнения
    # ---
    for col in feature_columns:
        if col in ("Mortality_Risk", "5_Year_Survival_Probability"):
            var = tk.StringVar(value="None")
            input_vars[col] = var
            continue
        row_frame = tk.Frame(scrollable_frame)
        row_frame.pack(fill="x", padx=10, pady=4)

        tk.Label(row_frame, text=col, width=30, anchor="w").pack(side="left")

        if col == "Age":
            age_var = tk.StringVar(value="None")
            input_vars[col] = age_var

            age_values = ["None"] + [str(i) for i in range(30, 91)]
            combo = ttk.Combobox(row_frame, textvariable=age_var, values=age_values, state="readonly", width=25)
            combo.pack(side="left", padx=5)
            combo.current(0)
        else:
            values = df[col].dropna().astype(str).unique().tolist()
            values = sorted(values)
            values = ["None"] + values

            var = tk.StringVar(value="None")
            input_vars[col] = var

            combo = ttk.Combobox(row_frame, textvariable=var, values=values, state="readonly", width=25)
            combo.pack(side="left", padx=5)
            combo.current(0)
    # ---

    # Выбор модели
    model_frame = tk.Frame(scrollable_frame)
    model_frame.pack(fill="x", padx=10, pady=15)

    tk.Label(model_frame, text="Выберите нейронную сеть", width=30, anchor="w", font=("Arial", 11, "bold")).pack(side="left")

    selected_model_name = tk.StringVar()

    """
    for model_name in models.keys():
        tk.Radiobutton(
            prediction_interface_root,
            text=model_name,
            variable=selected_model_name,
            value=model_name
        ).pack(anchor="w")
    model_combo = ttk.Combobox(
        model_frame,
        textvariable=selected_model_name,
        values=list(models.keys()),
        state="readonly",
        width=30
    )
    """
    model_combo = ttk.Combobox(
        model_frame,
        textvariable=selected_model_name,
        values=list(models.keys()),
        state="readonly",
        width=30
    )
    model_combo.pack(side="left", padx=5)
    model_combo.current(0)






    def show_result_window(result_str):
        result_window = tk.Toplevel(prediction_interface_root)
        result_window.title("Результат предсказания")
        result_window.geometry("700x600")

        text_widget = tk.Text(result_window, wrap="word")
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        text_widget.insert("1.0", result_str)
        text_widget.config(state="disabled")

        close_btn = tk.Button(result_window, text="Закрыть", command=result_window.destroy)
        close_btn.pack(pady=10)

    def on_predict():
        try:
            #model_name = selected_model_name.get()
            #model = models.get(model_name, 0)
            model_name = selected_model_name.get()
            model = models[model_name]

            # Проверка наличия модели
            if model == 0 or model is None:
                messagebox.showerror("Ошибка", f"Нейронная сеть '{model_name}' не загружена")
                return
            # Подготовка данных
            X_input = prepare_input_row(feature_columns, input_vars, df, all_columns)


            # Предсказание
            result_str = format_prediction_result(model_name, model, X_input, input_vars, feature_columns)

            # Открытие нового окна
            show_result_window(result_str)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось выполнить предсказание:\n{e}")

    # Кнопки управления
    button_frame = tk.Frame(scrollable_frame)
    button_frame.pack(pady=20)

    predict_btn = tk.Button(button_frame, text="Предсказать", command=on_predict, width=20)
    predict_btn.pack(side="left", padx=10)

    close_btn = tk.Button(button_frame, text="Закрыть", command=prediction_interface_root.destroy, width=20)
    close_btn.pack(side="left", padx=10)

    prediction_interface_root.mainloop()









def base_neural_menu():
    base_neural_menu_root = tk.Tk()
    base_neural_menu_root.title("Меню работы с нейронными сетями")
    base_neural_menu_root.geometry("500x400")

    welcome_label = tk.Label(
        base_neural_menu_root,
        text="Выберите что вы хотите \nсделать с нейронными сетями",
        font=("Arial", 16, "bold"),
        pady=20,
        justify="center"
    )
    welcome_label.pack()

    # Создание контейнера для кнопок
    button_frame = tk.Frame(base_neural_menu_root)
    button_frame.pack(pady=10)

    btn_load = tk.Button(
        button_frame,
        text="Создать нецронную сеть",
        width=25,
        command=create_neural_menu
    )
    btn_load.pack(pady=5)

    btn_view = tk.Button(
        button_frame,
        text="Экспоритровать сеть",
        width=25,
        command=save_selected_model
    )
    btn_view.pack(pady=5)

    btn_nn = tk.Button(
        button_frame,
        text="Импортировать сеть",
        width=25,
        command=load_neural_model_interface
    )
    btn_nn.pack(pady=5)

    btn_ref = tk.Button(
        button_frame,
        text="Тестировать нейронную сеть",
        width=25,
        command=evaluate_models_interface
    )
    btn_ref.pack(pady=5)

    btn_ref = tk.Button(
        button_frame,
        text="Предсказание для пациента",
        width=25,
        command=prediction_interface
    )
    btn_ref.pack(pady=5)

    btn_ref = tk.Button(
        button_frame,
        text="Справочная информация",
        width=25,
        command=GUI_functions_directory.create_main_interface
    )
    btn_ref.pack(pady=5)

    btn_ref = tk.Button(
        button_frame,
        text="Закрыть окно",
        width=25,
        command=base_neural_menu_root.destroy
    )
    btn_ref.pack(pady=5)
    base_neural_menu_root.mainloop()






