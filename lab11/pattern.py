import psycopg2
from config import host, user, password, db_name

try:
    # устанавливаем соединение с базой данных
    conn = psycopg2.connect(database=db_name, 
                            user=user, 
                            password=password, 
                            host=host)
    
    
    #подключаем автокоммит чтобы данные загружались автоматически
    conn.autocommit = True
    
    # создаем объект курсора для работы с базой данных
    cur = conn.cursor()    
    
    choise = input("Выберите что будете вводить имя либо номер: ")
    
    if choise == "name":
        name = input("Введите имя или начало имени: ")
        
        # формируем SQL-запрос для поиска данных
        query = f"SELECT * FROM lab11 WHERE name LIKE '{name}%'"
    
        # выполняем запрос
        cur.execute(query)
    
        # получаем результаты и выводим их на экран
        rows = cur.fetchall()

        for row in rows:
            print(f"Имя: {row[1]} Номер: {row[2]}")
    else:
        phone = input("Введите номер или начало номера: ")
        
        # формируем SQL-запрос для поиска данных
        query = f"SELECT * FROM lab11 WHERE phone LIKE '{phone}%'"
    
        # выполняем запрос
        cur.execute(query)
    
        # получаем результаты и выводим их на экран
        rows = cur.fetchall()

        for row in rows:
            print(f"Имя: {row[1]} Номер: {row[2]}")


    

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
    
finally:
    if conn:
        #закрываем курсор
        cur.close()
        # закрываем соединение с базой данных
        conn.close()
        print("[INFO] PostgreSQL connection closed")