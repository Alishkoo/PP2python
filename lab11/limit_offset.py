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

    limit = input("Enter limit :")
    offset = input("Enter offset :")
    
    # формируем SQL-запрос для получения данных с пагинацией
    query = f"SELECT * FROM lab11 LIMIT {limit} OFFSET {offset}"
    
    # выполняем запрос
    cur.execute(query)

    # получаем результаты и выводим их на экран
    rows = cur.fetchall()
    for row in rows:
        print(row)
      
    
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if conn:
        #закрываем курсор
        cur.close()
        # закрываем соединение с базой данных
        conn.close()
        print("[INFO] PostgreSQL connection closed")