import mysql.connector

#------------------------------------------------------------
# Данные
df = 0

# Очищенные данные:
clear_df = 0

# Статус готовности данных
# Статус изменится при выполнении операции подготовки данных к работе
data_status = False

#------------------------------------------------------------


#------------------------------------------------------------
# Именна колонок
name_columns_df = ["Country","Age","Gender","Smoking_Status","Second_Hand_Smoke","Air_Pollution_Exposure","Occupation_Exposure",
                   "Rural_or_Urban","Socioeconomic_Status","Healthcare_Access","Insurance_Coverage","Screening_Availability",
                   "Stage_at_Diagnosis","Cancer_Type","Mutation_Type","Treatment_Access","Clinical_Trial_Access","Language_Barrier",
                   "Mortality_Risk","5_Year_Survival_Probability","Delay_in_Diagnosis","Family_History","Indoor_Smoke_Exposure",
                   "Tobacco_Marketing_Exposure","Final_Prediction"]
#------------------------------------------------------------


#------------------------------------------------------------
# Параметры доступа к БД
host = "localhost"
port = 3306
user = "root"
password = "root"
database = "mydb"
# Подключение к БД
cnx = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
#------------------------------------------------------------


#------------------------------------------------------------
# Параметры для первичной очистки данных
# Диапозон лет
max_year = 90
min_year = 30

# Риск смерти и риск выживания в течении 5 лет (Проценты от 0 до 1)
risk_of_death_max = 1.0
risk_of_death_min = 0.0

# Возможное значений категориальных признаков
valid_values = {
        'Gender': ['Male', 'Female'],
        'Smoking_Status': ['Non-Smoker','Former Smoker','Smoker'],
        'Second_Hand_Smoke': ['No', 'Yes'],
        'Air_Pollution_Exposure': ['Low', 'Medium', 'High'],
        'Occupation_Exposure': ['No', 'Yes'],
        'Rural_or_Urban': ['Rural', 'Urban'],
        'Socioeconomic_Status': ['Low', 'Middle', 'High'],
        'Healthcare_Access': ['Poor', 'Limited', 'Good'],
        'Insurance_Coverage': ['No', 'Yes'],
        'Screening_Availability': ['No', 'Yes'],
        'Stage_at_Diagnosis': ['I', 'II', 'III', 'IV'],
        'Cancer_Type': ['NSCLC', 'SCLC'],
        'Mutation_Type': ['None', 'EGFR', 'ALK', 'KRAS'],
        'Treatment_Access': ['None', 'Partial', 'Full'],
        'Clinical_Trial_Access': ['No', 'Yes'],
        'Language_Barrier': ['No', 'Yes'],
        'Delay_in_Diagnosis': ['No', 'Yes'],
        'Family_History': ['No', 'Yes'],
        'Indoor_Smoke_Exposure': ['No', 'Yes'],
        'Tobacco_Marketing_Exposure': ['No', 'Yes'],
        'Final_Prediction – Lung Cancer': ['No', 'Yes'],
        'Final_Prediction': ['No', 'Yes']
    }
#------------------------------------------------------------



#------------------------------------------------------------
# Кодирование признаков
valid_values_country = 1
#------------------------------------------------------------

#------------------------------------------------------------
# Нейронные сети
g_model_pipeline_presence_cancer = 0
g_risk_model = 0
g_survival_model = 0
g_cancer_model = 0
g_mutation_model = 0
#------------------------------------------------------------


#------------------------------------------------------------
# Ссылка на папку со статьями
g_link_papers_folder = r"C:\Users\aleks\Desktop\ВКР\Программа\Данные\Локальные\Статьи"
g_name_file_catalog = r"list_of_scientific_articles.txt"

g_articles_data = []


#------------------------------------------------------------















