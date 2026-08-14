import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi
from tkinter import messagebox

import Global_data

#-------------------------------------------------------------
# Объект соеденитель с БД
cursor = Global_data.cnx.cursor()
#-------------------------------------------------------------

def import_data_from_SQL():
        # Запрос
        command = "SELECT * from Lung_Cancer_Risk_and_Prediction_Dataset"
        # Отправка запроса
        cursor.execute(command)
        # Значения таблицы
        rows = cursor.fetchall()
        # Значение названий колонок таблицы
        name_columns = [desc[0] for desc in cursor.description]
        # Создание датафрэйма
        df = pd.DataFrame(rows, columns=name_columns)
        # Редоктирование последнего столбца от лишних мпецсимволов
        last_col = df.columns[-1]
        df[last_col] = df[last_col].astype(str).str.strip()
        # Удаление столбца id
        df = df.drop(df.columns[0], axis=1)
        df.columns = Global_data.name_columns_df
        return df

#def import_data_from_local_disc(path = r"C:\Users\aleks\Desktop\ВКР\Программа\Данные\Локальные", name_file = "lung_cancer_prediction.csv"):
def import_data_from_local_disc(path, name_file):
        # Создание обсолютного пути
        file_path = os.path.join(path, name_file)
        # Проверка наличия файла
        if not os.path.isfile(file_path):
                #print("Файл '{file}' не найден.")
                return ""
        df = pd.read_csv(file_path)
        return df

"""
Ниже приведена инструкция, по получению Kaggle.api
1) Заригистрируйтесь на сайте
2) Зайдите в настройки аккаунта
3) Прокрутите настройки до пункат API и выберите 'Create new token'
4) Перенисите скачанный файл json в следующую папку:
C:/Users/"users_name"/.kaggle
"""
def Сheck_kaggle_api_setup():
        # Путь к файлу Kaggle API на Windows
        kaggle_config_path = os.path.join(os.environ['USERPROFILE'], '.kaggle', 'kaggle.json')
        # Проверка сущиствования файла
        if not os.path.isfile(kaggle_config_path):
            #print(f"Файл {kaggle_config_path} не найден. Убедитесь, что Kaggle API установлен и настроен.")
            messagebox.showerror("Ошибка", f"Файл {kaggle_config_path} не найден. Убедитесь, что Kaggle API установлен и настроен.")
            return False
        try:
            # Проверка аутентифицироваться с помощью Kaggle API
            api = KaggleApi()
            api.authenticate()
            # print("Kaggle API настроен правильно. Аутентификация прошла успешно.")

            return True
        except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при аутентификации с Kaggle API: {e}")
                #print(f"Ошибка при аутентификации с Kaggle API: {e}")
                return False

#def import_data_from_kaggle(dataset_url = "https://www.kaggle.com/datasets/ankushpanday1/lung-cancer-risk-and-prediction-dataset"):
def import_data_from_kaggle(dataset_url):
        if(Сheck_kaggle_api_setup()):
                # Извлекаем имя пользователя и название датасета из URL
                dataset_parts = dataset_url.split('/')
                if len(dataset_parts) != 6:
                        # print("Некорректный URL")
                        messagebox.showerror("Ошибка", "Некорректный URL")
                        return False, ""
                username = dataset_parts[len(dataset_parts) - 2]
                dataset_name = dataset_parts[len(dataset_parts) - 1]

                # Аутентификация с Kaggle API
                api = KaggleApi()
                api.authenticate()

                # Проверка доступности датасета
                try:
                        api.dataset_download_files(f"{username}/{dataset_name}", path=".", unzip=True)
                except Exception as e:
                        messagebox.showerror("Ошибка", f"Ошибка в нименовании датасета или пользователя его выложевшего")
                        # print("Ошибка в нименовании датасета или пользователя его выложевшего")
                        return False, ""

                # Загрузка датасета
                try:
                        # Поиск загруженного CSV файла
                        csv_file = [f for f in os.listdir('.') if f.endswith('.csv')][0]
                        # Чтение данных в DataFrame
                        df = pd.read_csv(csv_file)
                        return True, df
                except Exception as e:
                        #print("Ошибка при загрузке датасета")
                        messagebox.showerror("Ошибка", "Ошибка при загрузке датасета")
                        return False, ""
        else:
                return False, ""





