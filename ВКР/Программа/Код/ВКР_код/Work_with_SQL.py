import Global_data


#-------------------------------------------------------------
# Объект соеденитель с БД
cursor = Global_data.cnx.cursor()
#-------------------------------------------------------------

# Функция для поиска наличия указанного пользователя с указанным поролем
def check_user_credentials(fio, password):
    # Создание SQL запрос
    query = "SELECT user_id FROM Users WHERE fio = %s AND pass = %s"
    # Выполнение запроса с передачей параметров
    cursor.execute(query, (fio, password))
    # Извлечение одной записи (если она есть)
    result = cursor.fetchone()
    # Если результат не пустой, значит пользователь найден
    if result:
        return True
    else:
        return False

# Функция для поиска наличия указанного пользователя с указанным поролем
def check_user_credentials(fio, password):
    # Создание SQL запрос
    query = "SELECT user_id FROM Users WHERE fio = %s AND pass = %s"
    # Выполнение запроса с передачей параметров
    cursor.execute(query, (fio, password))
    # Извлечение одной записи (если она есть)
    result = cursor.fetchone()
    # Если результат не пустой, значит пользователь найден
    if result:
        return True
    else:
        return False


def check_user_name(fio):
    # Создание SQL запрос
    query = "SELECT user_id FROM Users WHERE fio = %s"
    # Выполнение запроса с передачей параметров
    cursor.execute(query, (fio,))
    # Извлечение одной записи (если она есть)
    result = cursor.fetchone()
    # Если результат не пустой, значит пользователь найден
    if result:
        return True
    else:
        return False

def create_new_user(fio, password):
    # Создание SQL запрос
    query = "INSERT INTO Users (user_id, fio, pass) SELECT IFNULL(MAX(user_id), 0) + 1, %s, %s FROM Users"
    # Выполнение запроса с передачей параметров
    cursor.execute(query, (fio, password))
    Global_data.cnx.commit()
    return









