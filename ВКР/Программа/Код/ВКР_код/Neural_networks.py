import pandas as pd
import io
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neural_network import MLPRegressor


def create_presence_cancer_model(df):
    X = df.drop(columns=["Final_Prediction"])
    y = df["Final_Prediction"]

    # Кодируем целевую переменную
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Определяем типы колонок для предобработки
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = X.select_dtypes(include=['float64', 'int64']).columns.tolist()

    # Категориальные данные переводим в OneHot, числовые — масштабируем
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ])

    # Создание модели нейронной сети
    # 2 скрытых слоя по 64 и 32 нейрона
    mlp = MLPClassifier(
        hidden_layer_sizes=(64, 32),
        max_iter=1000,
        random_state=42,
        learning_rate_init=0.001
    )

    # Объединяем в Pipeline для удобства
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', mlp)
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model_pipeline.fit(X_train, y_train)

    #y_pred = model_pipeline.predict(X_test)
    #print("Отчет о качестве модели:")
    #print(classification_report(y_test, y_pred, target_names=le.classes_))

    return model_pipeline













def create_risk_model(df, target_column):
    # target_column может быть [0,1]
    X = df.drop([target_column], axis=1, errors='ignore')
    y = df[target_column]

    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', MLPRegressor(hidden_layer_sizes=(64, 32),
                                   activation='relu',
                                   solver='adam',
                                   alpha=0.01,
                                   random_state=42,
                                   max_iter=500))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model_pipeline.fit(X_train, y_train)

    return model_pipeline

# Использование для Mortality Risk:
# risk_model = Neural_networks.create_risk_model(Global_data.df, 'Mortality_Risk')
# Использование для 5-Year Survival:
# survival_model = Neural_networks.create_risk_model(Global_data.df, '5_Year_Survival_Probability')


def create_categorical_model(df, target_column):
    X = df.drop([target_column], axis=1, errors='ignore')
    y = df[target_column]

    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    # Архитектура для классификации (Softmax применяется автоматически)
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', MLPClassifier(hidden_layer_sizes=(128, 64),
                                     activation='relu',
                                     solver='adam',
                                     max_iter=1000,
                                     random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model_pipeline.fit(X_train, y_train)

    return model_pipeline

#сancer_model = create_categorical_model(df, "Cancer_Type")
#mutation_model = create_categorical_model(df, "Mutation_Type")

