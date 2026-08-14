import Authorization_interface
import Functions_directory

import GUI_Base_menu
"""
import GUI_functions_directory
import Import_data
import Global_data
import Data_preparation
import Data_evaluation
import Neural_networks
import GUI_neural_networks
import Work_with_SQL
"""

"""
Вродебы всё сделано
"""
# Функция подготовки
Functions_directory.load_articles_catalog()



Authorization_interface.create_authorization_window()
#GUI_Base_menu.base_menu()

#GUI_functions_directory.create_main_interface()
"""
Авторихация:
F1
P1
"""

#Global_data.df = Import_data.import_data_from_local_disc()
#Global_data.df = Import_data.import_data_from_local_disc()
#GUI_neural_networks.base_neural_menu()
#Data_preparation.starting_data_preparation(Global_data.df)


#GUI_functions_directory.create_main_interface()

#GUI_Base_menu.base_menu()

#Global_data.g_model_pipeline_presence_cancer = Neural_networks.create_and_train_presence_cancer_model(Global_data.df)
#Global_data.g_сancer_model = Neural_networks.create_categorical_model(Global_data.df, "Cancer_Type")

#GUI_neural_networks.save_selected_model()
#GUI_neural_networks.load_neural_model_interface()
#GUI_neural_networks.evaluate_models_interface()


#GUI_neural_networks.base_neural_menu()
#print(Global_data.df)
#print(Global_data.g_model_pipeline_presence_cancer)
#print(Global_data.g_cancer_model)


#print(Global_data.df)
#model_pipeline_presence_cancer = Neural_networks.create_presence_cancer_model(Global_data.df)
#risk_model = Neural_networks.create_risk_model(Global_data.df, 'Mortality_Risk')
#survival_model = Neural_networks.create_risk_model(Global_data.df, '5_Year_Survival_Probability')
#сancer_model = Neural_networks.create_categorical_model(Global_data.df, "Cancer_Type")
#mutation_model = Neural_networks.create_categorical_model(Global_data.df, "Mutation_Type")

#GUI_Base_menu.base_menu()



"""
Global_data.df = Import_data.import_data_from_local_disc()

Global_data.df, Primary_cleaning_parameters = Data_preparation.Starting_data_preparation(Global_data.df)

Data_evaluation.Data_evaluation_function(Global_data.clear_df)

print(Global_data.clear_df)
"""

#Global_data.df.to_csv('data_export.csv', index=False, encoding='utf-8-sig')
"""
Сделал интерфейс для загрузки и подготовки данных

Теперь надо сделать интерфейс для просмотра данных

"""



#Global_data.df = Import_data.import_data_from_SQL()
#Global_data.df = Import_data.import_data_from_local_disc()
#Is_conect, Global_data.df = Import_data.import_data_from_kaggle()
#print(Global_data.df)

#b = Data_preparation.starting_data_preparation(Global_data.df)




#Authorization_interface.create_authorization_window()

