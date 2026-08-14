import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import Global_data

def check_df_name_column(df):
    if (isinstance(df, pd.DataFrame)):
        return list(df.columns) == list(Global_data.name_columns_df)
    else:
        return False


# Функция начала процесса подготовки данных
def starting_data_preparation(df):
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Mortality_Risk'] = pd.to_numeric(df['Mortality_Risk'], errors='coerce')
    df['5_Year_Survival_Probability'] = pd.to_numeric(df['5_Year_Survival_Probability'], errors='coerce')
    df, Primary_cleaning_parameters = primary_data_cleaning_function(df)
    Global_data.df = df.copy()
    # Изменено недавно
    #df = Data_preparation(df)
    #Global_data.clear_df = df.copy()
    Global_data.clear_df = Data_preparation(df)
    return Primary_cleaning_parameters


# Функция очистки от явных неверных данных
def primary_data_cleaning_function(df):

    # Приведём к единому формату поля-пропуски
    df = df.where(pd.notnull(df), 'None')

    # Инициализация словаря, где будет сохранятся причина очистки и количество удалёных записей
    Primary_cleaning_parameters = {
        "duplicates_removed": 0,
        "invalid_input_removed": 0,
        "logical_inconsistency_removed": 0
    }
    initial_count = len(df)

    # 1) Удаление дубликатов
    df_cleaned = df.drop_duplicates()
    Primary_cleaning_parameters["duplicates_removed"] = initial_count - len(df_cleaned)


    # 2) Удаление записей с неправильным вводом (валидация по диапазонам и списку значений)
    # Определяем допустимые значения на основе предоставленного файла параметров
    pre_invalid_count = len(df_cleaned)

    mask = (df_cleaned['Age'] >= Global_data.min_year) & (df_cleaned['Age'] <= Global_data.max_year)


    # Проверка категориальных признаков
    for col, values in Global_data.valid_values.items():
        if col in df_cleaned.columns:
            mask &= df_cleaned[col].isin(values)


    # Проверка численных вероятностей смерти и выживания (это проценты, представленны от 0 до 1)
    prob_cols = ['Mortality_Risk', '5_Year_Survival_Probability']
    for col in prob_cols:
        if col in df_cleaned.columns:
            mask &= (df_cleaned[col] >= Global_data.risk_of_death_min) & (df_cleaned[col] <= Global_data.risk_of_death_max)

    df_cleaned = df_cleaned[mask]
    Primary_cleaning_parameters["invalid_input_removed"] = pre_invalid_count - len(df_cleaned)

    # 3) Удаление записей с логической противоречивостью
    pre_logical_count = len(df_cleaned)

    # Логическая проверка: Mortality Risk и Survival Probability не могут быть оба > 0.9 одновременно
    # Это не является строгим правилом, но така ситуация крайнее противоречивая, удаляем
    logical_mask = ~((df_cleaned['Mortality_Risk'] > 0.9) & (df_cleaned['5_Year_Survival_Probability'] > 0.9))

    # При стадии заболевания IV, вероятность 5-летнего выживания при НМРЛ (NSCLC) - 0.15, а при SCLC - 0.01
    logical_mask &= ~((df_cleaned['Stage_at_Diagnosis'] == 'IV') & (df_cleaned['Cancer_Type'] == 'NSCLC') & (
            df_cleaned['5_Year_Survival_Probability'] > 0.15))
    logical_mask &= ~((df_cleaned['Stage_at_Diagnosis'] == 'IV') & (df_cleaned['Cancer_Type'] == 'SCLC') & (
                df_cleaned['5_Year_Survival_Probability'] > 0.01))

    df_cleaned = df_cleaned[logical_mask]
    Primary_cleaning_parameters["logical_inconsistency_removed"] = pre_logical_count - len(df_cleaned)

    return df_cleaned, Primary_cleaning_parameters



def Data_preparation(df):

    # 1) Нормализация не требуется, данные с непривльным форматом были ранее отброшены

    # 2) Кодирование категориальных признаков
    # Странн много, кодируем их отдельно
    if 'Country' in df.columns:
        countries = sorted(df['Country'].unique())
        encoding_dict = {country: i for i, country in enumerate(countries)}
        Global_data.valid_values_country = encoding_dict
        #setattr(Global_data, "encoding_category_Country", encoding_dict)
        df['Country'] = df['Country'].map(encoding_dict)


    # Кодируем остальные категории
    for column, categories in Global_data.valid_values.items():
        if column in df.columns:
            # Правило кодирования => котирование формата 0,1,2...
            encoding_dict = {category: i for i, category in enumerate(categories)}
            # Применяем кодирование к датафрейму
            df[column] = df[column].map(encoding_dict)

    # 3. Масштабирование числовых признаков (от 0 до 1)
    # Выбираем числовые столбцы, исключая уже закодированные категории, и столбцы которые уже нормализованны в виде от 0 до 1
    cols_to_scale = ['Age']
    if cols_to_scale:
        scaler = MinMaxScaler()
        df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

    return df










